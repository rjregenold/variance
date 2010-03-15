'''
Setup script to create Windows executables.

Copyright 2010 Binary Lion Studios, LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

@author: RJ Regenold
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