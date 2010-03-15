'''
Setup script to create distributables.

@author: RJ Regenold | Binary Lion Studios, LLC
'''

# <plagiarism>
# Source: http://www.py2exe.org/index.cgi/WinShell
import time
import sys 

# ModuleFinder can't handle runtime changes to __path__, but win32com uses them 
try:
    # if this doesn't work, try import modulefinder
    import py2exe.mf as modulefinder
    import win32com
    for p in win32com.__path__[1:]:
        modulefinder.AddPackagePath("win32com", p)
    for extra in ["win32com.shell"]: #,"win32com.mapi"
        __import__(extra)
        m = sys.modules[extra]
        for p in m.__path__[1:]:
            modulefinder.AddPackagePath(extra, p)
except ImportError:
    # no build path setup, no worries.
    pass
# </plagiarism>

import py2exe
from distutils.core import setup

setup(
      windows=[{'script': 'main.py', 'icon_resources': [(1, 'assets/variance.ico')]},
               {'script': 'startup.py', 'icon_resources': [(1, 'assets/startup.ico')]}],
      options = {'py2exe': { 
                            'packages': ['sqlalchemy'], 
                            'dll_excludes': ['MSVCP90.dll'], 
                            'bundle_files': 1
        }},
      zipfile = None
)