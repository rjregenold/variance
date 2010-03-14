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

from binarylion.variance import model

import os
from puremvc.interfaces import IProxy
from puremvc.patterns.proxy import Proxy
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
session = None

class EnvProxy(Proxy, IProxy):
    NAME = 'env proxy'
    def __init__(self):
        Proxy.__init__(self, EnvProxy.NAME)
    def setup(self):
        root = 'data'
        if not os.path.exists(root):
            os.makedirs(root)
        dbfile = os.path.join(root, 'data.db')
        engine = create_engine('sqlite:///%s' % dbfile, echo=True)
        Session.configure(autoflush=True, autocommit=False, bind=engine)
        session = Session()
        if not os.path.exists(dbfile):
            model.Base.metadata.create_all(Session().bind)
        
class PrefsProxy(Proxy, IProxy):
    '''The prefs proxy.'''
    NAME = 'prefs proxy'
    def __init__(self):
        Proxy.__init__(self, PrefsProxy.NAME)
    def getImgDir(self):
        return session.query(model.Pref.value).filter_by(key='imgDir')
    def save(self):
        print 'Would save prefs'
        session = Session()
        imgDir = model.Pref('imgDir', r'C:\Documents and Settings\rregenol\My Documents\My Pictures\wallpaper')
        try:
            session.add(imgDir)
        except exc.IntegrityError:
            print 'Already set'
        session.commit()