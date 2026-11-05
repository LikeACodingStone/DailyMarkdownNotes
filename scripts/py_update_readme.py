#!/usr/bin/env python3
"""Regenerate topic navigation. Run with Python 3; no dependencies required.

Add new public topic folders to TOPICS. Content outside the generated markers
is preserved. Git-ignored files and attachment/hidden folders are excluded.
"""
from pathlib import Path
import argparse
import os
import re
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ('Linux', 'Windows', 'Git_Repo', 'Android', 'Programming', 'Tools',
          'Japanese', 'AI', 'Inbox')
ATTACHMENT_DIRS = ('_resources', '_assets')
# Obsidian decodes link targets like decodeURI, which leaves %26 %2C %2B encoded, so a
# link to "A & B.md" written with %26 opens an empty new note. Keep these characters
# literal; GitHub reads them fine too.
LINK_SAFE = '/;:@&=+$,'
START ='<!-- BEGIN AUTO NAVIGATION -->'
END = '<!-- END AUTO NAVIGATION -->'


def list_notes(folder, parts):
    """Yield the notes under folder as 'Topic/sub/name.md'.

    Each folder is listed once and every entry is classified from that listing.
    Per-note stat/resolve calls are network round trips when the vault is on an
    SMB share, so they are avoided. Hidden entries, attachment folders and
    symlinks are skipped without being entered.
    """
    try:
        with os.scandir(folder) as scan:
            entries = list(scan)
    except (FileNotFoundError, NotADirectoryError, PermissionError):
        return
    for entry in entries:
        name = entry.name
        if name.startswith('.') or name in ATTACHMENT_DIRS or entry.is_symlink():
            continue
        if entry.is_dir():
            yield from list_notes(entry.path, parts + (name,))
        elif os.path.normcase(name).endswith('.md'):
            yield '/'.join(parts + (name,))


def navigation(root):
    print("Scanning Markdown notes...", flush=True)
    real_root = Path(os.path.realpath(root))
    candidates = []
    for topic in TOPICS:
        folder = root / topic
        # Do not follow a topic folder that is a symlink pointing out of the vault.
        if Path(os.path.realpath(folder)).is_relative_to(real_root):
            candidates.extend(list_notes(folder, (topic,)))
    print(f"Checking Git ignore rules for {len(candidates)} notes...", flush=True)
    # --no-index also excludes ignored files that were previously tracked.
    result = subprocess.run(
        ['git', 'check-ignore', '--no-index', '-z', '--stdin'], cwd=root,
        input=''.join(name + '\0' for name in candidates).encode(),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=10,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.decode(errors='replace'))
    ignored = set(result.stdout.decode().split('\0'))
    lines = [START, '']
    for topic in TOPICS:
        names = sorted((n for n in candidates if n.startswith(topic + '/')
                        and n not in ignored), key=str.casefold)
        if not names:
            continue
        lines.extend([f'## {topic}', ''])
        for name in names:
            label = re.sub(r'([\\\[\]])', r'\\\1', Path(name).stem)
            lines.append(f'- [{label}]({quote(name, safe=LINK_SAFE)})')
        lines.append('')
    lines.append(END)
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check without writing')
    args = parser.parse_args()
    path = ROOT / 'README.md'
    original = path.read_text(encoding='utf-8')
    if original.count(START) != 1 or original.count(END) != 1:
        raise SystemExit('README must contain exactly one pair of navigation markers.')
    start = original.index(START)
    end = original.index(END)
    if end < start:
        raise SystemExit('Navigation markers are in the wrong order.')
    updated = original[:start] + navigation(ROOT) + original[end + len(END):]
    if updated == original:
        print('README 已是最新。')
        return
    if args.check:
        raise SystemExit('README 需要更新：python3 scripts/update_readme.py')
    path.write_text(updated, encoding='utf-8')
    print('README 导航已更新。')


if __name__ == '__main__':
    main()
