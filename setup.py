#!/usr/bin/env python

# Note: Based on https://github.com/kennethreitz/requests/blob/master/setup.py
# See: http://docs.python.org/2/distutils/setupscript.html

import os
import sys

import nway-dbify

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'nway-dbify',
]

requires = []
with open('requirements.txt') as fin:
    lines = fin.readlines()
for l in lines:
    requires.append(l.strip())

setup(
    name='nway-dbify',
    version=nway-dbify.__version__,
    description='nway-dbify - Nesoni helper/plugin to get nway results into a DB',
    long_description=open('README.rst').read(),
    author='Mitchell Stanton-Cook',
    author_email='m.stantoncook@gmail.com',
    url='https://github.com/mscook/nway-dbify',
    packages=packages,
    scripts = ['nway-dbify/nway-dbify'],
    package_data={'': ['LICENSE']},
    package_dir={'nway-dbify': 'nway-dbify'},
    include_package_data=True,
    install_requires=requires,
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ),
)
