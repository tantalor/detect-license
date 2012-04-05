#!/usr/bin/python

import re
import urllib


RE_YEAR_AND_AUTHOR = re.compile('Copyright.*(\d{4})\s([\w\s-]*\w)', flags=re.IGNORECASE)
RE_MIT = re.compile('The MIT License', flags=re.IGNORECASE)


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
      if RE_MIT.search(line):
        license['type'] = 'MIT License'
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
    if 'type' in license:
      print "Type: %s" % license['type']
  else:
    print "Failed to detect a license"
