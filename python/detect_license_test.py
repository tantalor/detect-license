#!/usr/bin/python

from detect_license import detect_license
import unittest


class DetectLicenseTestCase(unittest.TestCase):
  
  def test_license_type(self):
    license = detect_license(reader = ['The MIT License', 'Blah blah blah.'])
    self.assertEquals(license['type'], 'MIT License')
    
  def test_year_and_author(self):
    license = detect_license(reader = ['Copyright 2012 Joe Programmer'])
    self.assertEquals(license['author'], 'Joe Programmer')
    self.assertEquals(license['year'], '2012')


if __name__ == '__main__':
  unittest.main()
