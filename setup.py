#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import untangle

from distutils.core import setup


if sys.argv[-1] == "test":
    os.system("python tests/tests.py")
    sys.exit()

setup(
    name='untangle',
    version=untangle.__version__,
    description='Convert XML documents into Python objects',
    long_description=open('README.md').read(),
    author='Christian Stefanescu',
    author_email='chris@0chris.com',
    url='https://github.com/stchris/untangle',
    packages= [
        'untangle',
    ],
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
		#'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
		#'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.0',
        # 'Programming Language :: Python :: 3.1',
    ),
)
