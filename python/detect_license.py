import re


RE_YEAR_AND_AUTHOR = re.compile('Copyright.*(\d{4})\s([\w\s-]*\w)', flags=re.IGNORECASE)
RE_MIT = re.compile('The MIT License', flags=re.IGNORECASE)


def detect_license(filename=None):
  if filename:
    reader = open(filename, 'r')
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
  import sys
  if len(sys.argv) < 2:
    print "Usage: %s license-file" % sys.argv[0]
    sys.exit()
  filename = sys.argv[1]
  license = detect_license(filename=filename)
  if license:
    if 'author' in license:
      print "Author: %s" % license['author']
    if 'year' in license:
      print "Year: %s" % license['year']
    if 'type' in license:
      print "Type: %s" % license['type']
  else:
    print "Failed to detect a license"
