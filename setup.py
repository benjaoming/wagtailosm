#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://wagtailosm.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

import wagtailosm

setup(
    name='wagtailosm',
    version=wagtailosm.__version__,
    description='Open Street Map integration for Wagtail',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Benjamin Bach',
    author_email='benjamin@overtag.dk',
    url='https://github.com/benjaoming/wagtailosm',
    packages=[
        'wagtailosm',
    ],
    package_dir={'wagtailosm': 'wagtailosm'},
    include_package_data=True,
    install_requires=[
        'django-osm-field',
    ],
    license='MIT',
    zip_safe=False,
    keywords='wagtailosm',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
