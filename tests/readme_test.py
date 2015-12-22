from __future__ import absolute_import
from __future__ import unicode_literals

import io

import yaml


def test_readme_contains_all_hooks():
    readme_contents = io.open('README.md', encoding='utf8').read()
    hooks = yaml.load(io.open('hooks.yaml', encoding='utf8').read())
    for hook in hooks:
        assert '`{0}`'.format(hook['id']) in readme_contents
