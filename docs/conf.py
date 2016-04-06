# -*- coding: utf-8 -*-
#
# django-controlcenter documentation build configuration file, created by
# sphinx-quickstart on Mon Mar  7 19:08:51 2016.

import sys
import os
import datetime

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'django-controlcenter'
copyright = ('{}, Django-controlcenter developers and contributors'
             .format(datetime.date.today().year))
version = '0.1.2'
release = '0.1.2'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = 'alabaster'
htmlhelp_basename = 'django-controlcenterdoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'django-controlcenter.tex',
     'Django-controlcenter Documentation', 'Murad Byashimov', 'manual'),
]
man_pages = [
    (master_doc, 'django-controlcenter', 'Django-controlcenter Documentation',
     ['Django-controlcenter developers and contributors'], 1)
]
texinfo_documents = [
    (master_doc, 'django-controlcenter', 'Django-controlcenter Documentation',
     'Django-controlcenter developers and contributors',
     'django-controlcenter', 'One line description of project.',
     'Miscellaneous'),
]
RTD_NEW_THEME = True