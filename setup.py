#!/usr/bin/env python3

"""Test, build, or install the Sitewatch package.

Run tests:
  python setup.py test

Build and install:
  python setup.py build && python setup.py install
"""

from distutils.util import convert_path
from setuptools import setup

VER_FILEPATH = convert_path('boilerplate/version.txt')  # changeme
with open(VER_FILEPATH) as file:
    __version__ = file.read()

setup(
    name='Boilerplate Python3 Project',   # changeme
    description='A boilerplate Python3 project',    # changeme
    url='https://github.com/texruska-boilerplate/python3',    # changeme
    author='Steven Burnett',
    license='GPLv3',
    author_email='texruska@users.noreply.github.com',
    packages=['boilerplate'], # changeme
    setup_requires=['pytest-runner'],
    tests_require=[
        'coverage',
        'pytest',
        'pytest-cov',
        'pytest-pylint'
    ],
    version=__version__,
    zip_safe=False
)
