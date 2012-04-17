Detect License
==============

Tools for detecting the type, author, and year of a software license.

Note that the author of a license may be different than the author of the software.
For example, GPLv2 licenses are commonly attributed to the Free Software Foundation, Inc.

This project was motivated by Thomas Fuchs' _[Why I’d like a “license type” setting for GitHub projects
]([http://mir.aculo.us/2012/04/05/why-id-like-a-license-type-setting-for-github-projects/)_, 5 April 2012.

Installing
----------

    $ (sudo) python setup.py install

Usage
-----

    $ detect_license.py --help
    usage: detect_license.py [-h] [-f FILENAME] [-u URL]

    Detect license

    optional arguments:
      -h, --help            show this help message and exit
      -f FILENAME, --filename FILENAME
      -u URL, --url URL


Examples
--------

Jekyll's MIT license,

    $ detect_license.py --url https://raw.github.com/mojombo/jekyll/master/LICENSE
    Author: Tom Preston-Werner
    Year: 2008
    Type: MIT

jQuery's GPLv2 license,

    $ detect_license.py --url https://raw.github.com/jquery/jquery/master/GPL-LICENSE.txt
    Author: Free Software Foundation
    Year: 1991
    Type: GPLv2

Supported Licenses
------------------

 * MIT License
 * GNU General Public License (GPL)
 * Affero General Public License (AGPL)

Requirements
------------

 * Python 2.5 (or better)
