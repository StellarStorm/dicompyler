#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# util.py
"""Several utility functions that don't really belong anywhere."""
# Copyright (c) 2009 Aditya Panchal
# This file is part of dicompyler, relased under a BSD license.
#    See the file license.txt included with this distribution, also
#    available at http://code.google.com/p/dicompyler/

from __future__ import with_statement
import imp, os, sys

def GetResourcePath(resource):
    """Return the specified item from the resources folder."""

    if main_is_frozen():
        return os.path.join((os.path.join(get_main_dir(), 'resources')), resource)
    else:
        return os.path.join((os.path.join(os.getcwd(), 'resources')), resource)

# from http://www.py2exe.org/index.cgi/HowToDetermineIfRunningFromExe
def main_is_frozen():
   return (hasattr(sys, "frozen") or # new py2exe
           hasattr(sys, "importers") # old py2exe
           or imp.is_frozen("__main__")) # tools/freeze

def get_main_dir():
   if main_is_frozen():
       return os.path.dirname(sys.executable)
   return os.path.dirname(sys.argv[0])
   
def get_credits():
    """Read the credits file and return the data from it."""
    
    developers = []
    artists = []
    with open('credits.txt', 'rU') as cf:
        credits = cf.readlines()
        for i, v in enumerate(credits):
            if (v == "Lead Developer\n"):
                developers.append(credits[i+1].strip())
            if (v == "Developers\n"):
                for d in credits[i+1:len(credits)]:
                    if (d.strip() == ""):
                        break
                    developers.append(d.strip())
            if (v == "Artists\n"):
                for a in credits[i+1:len(credits)]:
                    if (a.strip() == ""):
                        break
                    artists.append(a.strip())
    return {'developers':developers, 'artists':artists}
