#!/usr/bin/python

import re
import urllib


RE_YEAR_AND_AUTHOR = re.compile('Copyright.*(\d{4})\s([\w\s-]*\w)', flags=re.IGNORECASE)
RE_MIT = re.compile('The MIT License', flags=re.IGNORECASE)
RE_GPL = re.compile('GNU GENERAL PUBLIC LICENSE', flags=re.IGNORECASE)
RE_AGPL = re.compile('GNU AFFERO GENERAL PUBLIC LICENSE', flags=re.IGNORECASE)
RE_VERSION = re.compile('Version (\d+)', flags=re.IGNORECASE)

MIT_LICENSE = 'MIT License'
GPL = 'GPL'
AGPL = 'AGPL'

def detect_license(filename=None, url=None, reader=None):
  if filename:
    reader = open(filename, 'r')
  elif url:
    reader = urllib.urlopen(url)
  if reader:
    license = dict()
    for line in reader:
      year_and_author = RE_YEAR_AND_AUTHOR.search(line)
      if year_and_author:
        (year, author) = year_and_author.groups()
        license['year'] = year
        license['author'] = author
      if 'type' not in license:
        if RE_MIT.search(line):
          license['type'] = MIT_LICENSE
        if RE_GPL.search(line):
          license['type'] = GPL
        if RE_AGPL.search(line):
          license['type'] = AGPL
      if 'version' not in license and 'type' in license:
        version_match = RE_VERSION.search(line)
        if version_match:
          (version,) = version_match.groups()
          license['type'] = 'v'.join([license['type'], version])
          license['version'] = version
  return license


if __name__ == '__main__':
  import argparse
  parser = argparse.ArgumentParser(description='Detect license')
  parser.add_argument('-f', '--filename') 
  parser.add_argument('-u', '--url')
  args = parser.parse_args()
  license = detect_license(**vars(args))
  if license:
    if 'author' in license:
      print "Author: %s" % license['author']
    if 'year' in license:
      print "Year: %s" % license['year']
    print "Type: %s" % license.get('type', 'Unknown')
  else:
    print "Failed to detect a license"
