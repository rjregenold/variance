'''
Created on Mar 14, 2010

@author: rregenol
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