#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate structure and public boundaries, never execute literary meaning."""
import json
from pathlib import Path
import re
import tempfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
TAGS = set('projection purpose contract input authority precondition step candidate validate commit reject invariant test given when then assert ref'.split())
PINS = {'.code-constitution': '220dc9c286ae06f8b6ed60cdda75112eed0408ed',
        '.licensing-policy': '6e4c2627717c079827ed4aa9044a5346b3ea3ddb'}
SECRET = re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{30,}|AIza[A-Za-z0-9_-]{30,}|https?://(?:docs|drive)\.google\.com/[^\s]+', re.I)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(root):
    manifest = json.loads((root / 'manifest/publication.json').read_text())
    actual = {str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()
              and not any(part in {'.git', '.warden'} or part in PINS for part in p.relative_to(root).parts)}
    require(set(manifest['paths']) == actual, 'publication path inventory differs')
    require(manifest['gitlinks'] == PINS, 'unexpected policy pin')
    ids, refs, xml_count = {}, [], 0
    for name in sorted(actual):
        p = root / name
        text = p.read_text(encoding='utf-8')
        # The validator necessarily contains its own detection vocabulary.
        if name != 'tools/check-methodology.py':
            require(not SECRET.search(text), f'publication boundary: {name}')
        require(name == 'tools/warden.mjs' or p.suffix not in {'.cpp', '.hpp', '.ts', '.tsx', '.mjs', '.wasm'}, f'implementation code: {name}')
        if p.suffix == '.json':
            json.loads(text)
        if p.suffix == '.xml':
            require('<!DOCTYPE' not in text and '<!ENTITY' not in text, f'XML declarations: {name}')
            doc = ET.fromstring(text)
            require(doc.tag == 'projection' and doc.get('version') and doc.get('status') in {'illustrative', 'planned'}, f'projection header: {name}')
            require(doc.find('purpose') is not None and doc.find('contract') is not None and doc.find('test') is not None, f'incomplete projection: {name}')
            xml_count += 1
            for item in doc.iter():
                require(item.tag in TAGS, f'unknown element: {name}: {item.tag}')
                ident = item.get('id')
                if ident:
                    require(re.fullmatch(r'[a-z][a-z0-9.-]+', ident) and ident not in ids, f'invalid/duplicate ID: {ident}')
                    ids[ident] = name
                for attr in ('covers', 'ref'):
                    if item.get(attr):
                        refs.append((name, item.get(attr)))
                if item.tag == 'test':
                    require(ident and item.get('covers') and all(item.find(t) is not None for t in ('given', 'when', 'then')), f'incomplete test: {name}')
        if p.suffix == '.md':
            for target in re.findall(r'\]\(([^)]+)\)', text):
                if re.match(r'(?:https?://|mailto:|#)', target):
                    continue
                require((p.parent / target.split('#')[0]).exists(), f'broken local link: {name}: {target}')
    for name, ident in refs:
        require(ident in ids, f'unresolved reference: {name}: {ident}')
    require(xml_count >= 20, 'missing implementation case projections')
    return len(actual), xml_count, len(ids), len(refs)


def rejection_checks():
    import shutil
    with tempfile.TemporaryDirectory(prefix='spider-method-') as temp:
        copy = Path(temp) / 'copy'
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns('.git', *PINS))
        target = copy / 'CONTRACTS.xml'
        original = target.read_text()
        for bad in (original.replace('id="spider.retry"', 'id="spider.command"'),
                    original.replace('covers="spider.command"', 'covers="missing.contract"'),
                    original.replace('<then>', '<unknown>')):
            target.write_text(bad)
            try:
                check(copy)
            except (ValueError, ET.ParseError):
                pass
            else:
                raise ValueError('negative structural check unexpectedly passed')
        target.write_text(original)
        (copy / 'unreviewed.md').write_text('Unlisted input')
        try:
            check(copy)
        except ValueError:
            return 4
        raise ValueError('unlisted publication path unexpectedly passed')


if __name__ == '__main__':
    files, xml, ids, refs = check(ROOT)
    negatives = rejection_checks()
    print(f'PASS methodology: {files} files, {xml} XML projections, {ids} IDs, {refs} references; {negatives} rejection checks')
    print('Scope: structure/public inventory only; English contracts and product acceptance remain human review.')
