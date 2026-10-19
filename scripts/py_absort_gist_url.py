#!/usr/bin/env python3
"""Read a Gist URL from a gist_code note and copy its Markdown link."""
import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def gist_markdown(filename, root=ROOT):
    """Return a Markdown link from the note's Share as Gist metadata."""
    folder = (Path(root) / 'gist_code').resolve()
    name = filename.strip()
    if not name:
        raise ValueError('Enter a filename inside gist_code.')
    if not name.lower().endswith('.md'):
        name += '.md'
    path = (folder / name).resolve()
    if not path.is_relative_to(folder):
        raise ValueError('The file must be inside gist_code.')
    if not path.is_file():
        raise FileNotFoundError(f'File not found: {path}')
    content = path.read_text(encoding='utf-8-sig')
    frontmatter = re.match(r'\A---\s*\n(.*?)\n---\s*(?:\n|$)', content, re.S)
    if not frontmatter:
        raise ValueError('No Gist metadata found. Share this note using Share as Gist first.')
    # Share as Gist writes a block-style gists list. Ignore links in the body.
    lines = frontmatter.group(1).splitlines()
    in_gists = False
    urls = []
    for line in lines:
        if re.fullmatch(r'gists:\s*', line):
            in_gists = True
            continue
        if in_gists and re.match(r'^[^\s#-]', line):
            break
        if in_gists:
            match = re.match(r'''^\s+(?:-\s+)?url:\s*['"]?(https://gist\.github\.com/[A-Za-z0-9_-]+/[a-fA-F0-9]+)['"]?\s*(?:#.*)?$''', line)
            if match and match.group(1) not in urls:
                urls.append(match.group(1))
    if not urls:
        raise ValueError('No valid GitHub Gist URL found in the gists metadata.')
    if len(urls) > 1:
        raise ValueError('Multiple Gist URLs found; cannot choose one: ' + ', '.join(urls))
    label = re.sub(r'([\\\[\]])', r'\\\1', path.stem)
    return f'[{label}]({urls[0]})'


def copy_to_clipboard(text):
    """Copy using the operating system's clipboard utility."""
    if sys.platform == 'win32':
        command = ['powershell.exe', '-NoProfile', '-NonInteractive', '-Command',
                   '[Console]::InputEncoding = [System.Text.Encoding]::UTF8; '
                   'Set-Clipboard -Value ([Console]::In.ReadToEnd())']
    elif sys.platform == 'darwin':
        command = ['pbcopy']
    elif os.environ.get('WAYLAND_DISPLAY') and shutil.which('wl-copy'):
        command = ['wl-copy']
    elif os.environ.get('DISPLAY') and shutil.which('xclip'):
        command = ['xclip', '-selection', 'clipboard']
    elif os.environ.get('DISPLAY') and shutil.which('xsel'):
        command = ['xsel', '--clipboard', '--input']
    else:
        raise RuntimeError('No clipboard tool or desktop session found. On Linux, install wl-clipboard, xclip or xsel.')
    result = subprocess.run(command, input=text.encode('utf-8'),
                            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=10)
    if result.returncode:
        raise RuntimeError(result.stderr.decode('utf-8', errors='replace').strip()
                           or f'Clipboard command exit code: {result.returncode}')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('filename', nargs='?', help='Filename inside gist_code; .md is optional')
    args = parser.parse_args(argv)
    try:
        filename = args.filename
        if filename is None:
            print('Enter a filename inside gist_code (.md is optional), then press Enter:', flush=True)
            filename = input().strip()
        link = gist_markdown(filename)
    except (OSError, ValueError, EOFError) as error:
        print(f'FAILURE: {error}', flush=True)
        return 1
    print(f'Generated link:\n{link}', flush=True)
    try:
        copy_to_clipboard(link)
    except (OSError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f'COPY FAILED: {error}\nCopy the link above manually.', flush=True)
        return 1
    print('SUCCESS: Markdown link copied to clipboard.', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
