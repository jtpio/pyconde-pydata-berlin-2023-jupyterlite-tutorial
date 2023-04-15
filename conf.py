# -*- coding: utf-8 -*-
extensions = [
    'myst_parser',
    'jupyterlite_sphinx'
]

jupyterlite_dir = "."
jupyterlite_contents = "content"

master_doc = 'README'
source_suffix = '.md'

# General information about the project.
project = 'PyConDE & PyData Berlin 2023 - JupyterLite Tutorial'
author = 'Jeremy Tuloup'

exclude_patterns = []
highlight_language = 'python'
pygments_style = 'sphinx'

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']

html_css_files = [
    'custom.css'
]