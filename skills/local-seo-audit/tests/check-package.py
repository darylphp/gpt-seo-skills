#!/usr/bin/env python3
"""Validate source structure without network calls or business mutations."""
from pathlib import Path
from io import BytesIO
import hashlib
import json
import re
import zipfile

root = Path(__file__).resolve().parents[1]
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

skill = (root / 'SKILL.md').read_text()
front = re.match(r'\A---\n(.*?)\n---\n', skill, re.S)
check(front is not None, 'Missing YAML frontmatter')
if front:
    values = dict(re.findall(r'^(name|description): (.+)$', front[1], re.M))
    check(values.get('name') == root.name == 'local-seo-audit', 'Skill/folder name mismatch')
    check(0 < len(values.get('description', '')) < 200, 'Description must fit the shared platform limit')
    check(set(re.findall(r'^(\w+):', front[1], re.M)) == {'name', 'description'}, 'Unexpected frontmatter key')

runtime = [root / 'SKILL.md', *sorted((root / 'references').glob('*.md'))]
check(len(runtime) == 9, 'Expected entry point and eight references')
register = (root / 'references/source-register.md').read_text()
registered = set(re.findall(r'^\| ([GP]\d+) \|', register, re.M))
for path in root.rglob('*.md'):
    text = path.read_text()
    check('\u2014' not in text, f'Em dash: {path.relative_to(root)}')
    for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if re.match(r'^[a-z]+:', link) or link.startswith('#'):
            continue
        target = path.parent / link.split('#')[0]
        check(target.exists(), f'Broken local link: {path.relative_to(root)} -> {link}')
    if path in runtime:
        for ident in re.findall(r'\b[GP]\d{2}\b', text):
            check(ident in registered, f'Unregistered source: {ident} in {path.name}')
    if path in runtime:
        check(not re.search(r'\bTODO\b|\[insert |\[needs confirmation\]', text, re.I), f'Unfinished runtime instruction: {path.name}')

expected = re.findall(r'^## (\d+)\.', (root / 'references/output-template.md').read_text(), re.M)
check(expected == list(map(str, range(1, 11))), 'Template requires ten ordered sections')
for path in (root / 'examples').glob('*output.md'):
    text = path.read_text()
    check(re.findall(r'^## (\d+)\.', text, re.M) == expected, f'Example section order: {path.name}')
    check(len(re.findall(r'^Implementation approval:', text, re.M)) == 1, f'Example approval line: {path.name}')

archive = BytesIO()
with zipfile.ZipFile(archive, 'w') as zipped:
    for path in runtime:
        zipped.writestr('local-seo-audit/' + path.relative_to(root).as_posix(), path.read_bytes())
with zipfile.ZipFile(archive) as zipped:
    check(len(zipped.namelist()) == 9, 'Runtime archive count')
    check(all(n.startswith('local-seo-audit/') and '..' not in n.split('/') for n in zipped.namelist()), 'Unsafe runtime archive layout')
    check('local-seo-audit/SKILL.md' in zipped.namelist(), 'Runtime archive entry point')

manifest = {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in runtime}
print(json.dumps({'runtime_sha256': manifest, 'errors': errors}, indent=2))
raise SystemExit(bool(errors))
