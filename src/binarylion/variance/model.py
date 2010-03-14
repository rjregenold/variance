'''
This module contains the application proxies.

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

from binarylion.variance import vo

from puremvc.interfaces import IProxy
from puremvc.patterns.proxy import Proxy

class PrefsProxy(Proxy, IProxy):
    '''The prefs proxy.'''
    NAME = 'prefs proxy'
    def __init__(self):
        Proxy.__init__(self, PrefsProxy.NAME, vo.Prefs())
    def save(self):
        print 'Would save prefs'