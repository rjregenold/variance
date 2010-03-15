'''
This module contains the various model classes used
in the application.

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

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pref(Base):
    __tablename__ = 'prefs'
    
    key = Column(String, primary_key=True)
    value = Column(String)
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return "<Pref('%s', '%s')>" % (self.key, self.value)
    
class Prefs(object):
    imgDir = None
    startup = False
    period = None