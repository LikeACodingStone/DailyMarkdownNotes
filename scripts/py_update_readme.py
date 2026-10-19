#!/usr/bin/env python3
"""Regenerate topic navigation. Run with Python 3; no dependencies required.

Add new public topic folders to TOPICS. Content outside the generated markers
is preserved. Git-ignored files and attachment/hidden folders are excluded.
"""
from pathlib import Path
import argparse
import re
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ('Linux', 'Windows', 'Git_Repo', 'Android', 'Programming', 'Tools',
          'Japanese', 'AI', 'Inbox')
START = '<!-- BEGIN AUTO NAVIGATION -->'
END = '<!-- END AUTO NAVIGATION -->'


def navigation(root):
    print("Scanning Markdown notes...", flush=True)
    candidates = []
    for topic in TOPICS:
        for path in (root / topic).rglob('*.md'):
            rel = path.relative_to(root)
            if path.is_symlink() or any(
                part.startswith('.') or part in ('_resources', '_assets')
                for part in rel.parts
            ):
                continue
            if not path.resolve().is_relative_to(root.resolve()):
                continue
            candidates.append(rel.as_posix())
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
            lines.append(f'- [{label}]({quote(name, safe="/")})')
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
