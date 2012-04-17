#!/usr/bin/python

from distutils.core import setup

setup(
  name='detect_license',
  description='Detects the type, author, and year of a software license.',
  author='John Tantalo',
  author_email='john.tantalo@gmail.com',
  url='http://github.com/tantalor/detect_license',
  packages=['detect_license'],
  scripts=['detect_license/detect_license.py']
)
