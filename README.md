Detect License
==============

Tools for detecting the type, author, and year of a software license.

Note that the author of a license may be different than the author of the software.
For example, GPLv2 licenses are commonly attributed to the Free Software Foundation, Inc.

Examples
--------

Jekyll's MIT license,

    detect-license$ ./lib/detect_license.py --url https://raw.github.com/mojombo/jekyll/master/LICENSE
    Author: Tom Preston-Werner
    Year: 2008
    Type: MIT

jQuery's GPLv2 license,

    ./lib/detect_license.py --url https://raw.github.com/jquery/jquery/master/GPL-LICENSE.txt
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
