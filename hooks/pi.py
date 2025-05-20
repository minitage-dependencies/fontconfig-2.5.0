#!/usr/bin/env python

# Copyright (C) 2009, Makina Corpus <freesoftware@makina-corpus.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

__docformat__ = 'restructuredtext en'

import shutil
import os

def h(o, b):
    """
    Generate fontconfig, replace in location.
    copy the defaul fonts in destination
    """
    bd = b['buildout']['directory']
    l = b['part']['location']
    pf = b['part']['fonts-path']
    cf = os.path.join(bd, 'fonts')
    shutil.copytree(cf, pf)

    f = open(os.path.join(l, 'etc', 'fonts', 'fonts.conf'), 'w')
    f.write(b['fontconfig']['fontsconf'])
    f.flush()
    f.close()


# vim:set et sts=4 ts=4 tw=80:
