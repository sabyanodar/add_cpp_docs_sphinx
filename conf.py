import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'add cpp'
author = 'Sabyasachi Paul'
release = '1.0'

extensions = ['myst_parser']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

html_theme = 'sphinx_rtd_theme'
html_static_path = []

latex_documents = [
    ('index', 'add_cpp.tex', 'add cpp Documentation',
     'Sabyasachi Paul', 'manual'),
]


latex_engine = 'pdflatex'
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '11pt',
}
