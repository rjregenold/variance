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

from binarylion.variance import model, enum

import os, winshell
from puremvc.interfaces import IProxy
from puremvc.patterns.proxy import Proxy
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()

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
        if not os.path.exists(dbfile):
            session = Session()
            model.Base.metadata.create_all(session.bind)
            session.add(model.Pref(enum.PREF_KEYS.IMG_DIR, winshell.my_documents()))
            session.add(model.Pref(enum.PREF_KEYS.STARTUP, 'True'))
            session.add(model.Pref(enum.PREF_KEYS.PERIOD, enum.PERIOD.EVERY_LOG_IN))
            session.commit()
        
class PrefsProxy(Proxy, IProxy):
    '''The prefs proxy.'''
    NAME = 'prefs proxy'
    def __init__(self):
        Proxy.__init__(self, PrefsProxy.NAME, model.Prefs)
    def getImgDir(self):
        pref = Session().query(model.Pref).filter(model.Pref.key==enum.PREF_KEYS.IMG_DIR).first()
        return pref.value
    def save(self):
        print 'Would save prefs'
        session = Session()
        for pref in session.query(model.Pref).all():
            if pref.key == enum.PREF_KEYS.IMG_DIR:
                pref.value = self.prefs().imgDir
            elif pref.key == enum.PREF_KEYS.STARTUP:
                pref.value = self.prefs().startup
            elif pref.key == enum.PREF_KEYS.PERIOD:
                pref.value = self.prefs().period
            session.add(pref)
        try:
            session.commit()
        except exc.IntegrityError:
            print 'Something bad happened.'
    def prefs(self):
        return self.data