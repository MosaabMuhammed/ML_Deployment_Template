#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io, os
from pathlib import Path
from setuptools import find_packages, setup

# Package meta-data.
NAME            = 'regression_model'
DESCRIPTION     = 'Train and deploy regression model.'
URL             = 'YOUR GITHUB PROJCET'
EMAIL           = 'your_email@email.com'
AUTHOR          = 'Your name'
REQUIRES_PYTHON = '>=3.6.0'

# What packages are required for this module to be executed?
here = os.path.abspath(os.path.dirname(__file__))
def list_reqs(fname=f'{here}/requirements.txt'):
    with open(fname) as fd:
        return fd.read().splitlines()

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
# Trove Classifier for that!

# Import the README and use it as the long-description.
# NOTE: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the packages's __version__.py module as a dictionary.
ROOT_DIR = Path(__file__).resolve().parent
PACKAGES_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGES_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'regression_model': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers.
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)