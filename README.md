Detect License
==============

Tools for detecting the type, author, and year of a software license.

Note that the author of a license may be different than the author of the software.
For example, GPLv2 licenses are commonly attributed to the Free Software Foundation, Inc.

Example
-------

    detect-license$ ./python/detect_license.py --url https://raw.github.com/mojombo/jekyll/master/LICENSE
    Author: Tom Preston-Werner
    Year: 2008
    Type: MIT License

Supported Licenses
------------------

 * MIT License
 * GNU General Public License (GPL)
 * Affero General Public License (AGPL)

Supported Languages
-------------------

 * Python
