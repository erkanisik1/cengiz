#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    
    pisitools.insinto("/usr/share/doc/sounds-icons", "README")
    pisitools.insinto("/usr/share/doc/suonds-icons", "COPYING")
    pisitools.insinto("/usr/share/sounds/sounds-icons", "*")
    
    
    
