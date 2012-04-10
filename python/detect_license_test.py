#!/usr/bin/python

from detect_license import detect_license
import unittest


class DetectLicenseTestCase(unittest.TestCase):
  
  def test_mit_type(self):
    license = detect_license(reader = ['The MIT License', 'Blah blah blah.'])
    self.assertEquals(license['type'], 'MIT')
  
  def test_gpl_type(self):
    license = detect_license(reader = ['GNU GENERAL PUBLIC LICENSE', 'Blah blah blah.'])
    self.assertEquals(license['type'], 'GPL')
  
  def test_gpl2_type(self):
    license = detect_license(reader = ['GNU GENERAL PUBLIC LICENSE', 'Version 2, June 1991'])
    self.assertEquals(license['type'], 'GPL')
    self.assertEquals(license['version'], '2')
  
  def test_agpl3_type(self):
    license = detect_license(reader = ['GNU AFFERO GENERAL PUBLIC LICENSE', 'Version 3, 19 November 2007'])
    self.assertEquals(license['type'], 'AGPL')
    self.assertEquals(license['version'], '3')

  def test_year_and_author(self):
    license = detect_license(reader = ['Copyright 2012 Joe Programmer'])
    self.assertEquals(license['author'], 'Joe Programmer')
    self.assertEquals(license['year'], '2012')


if __name__ == '__main__':
  unittest.main()
