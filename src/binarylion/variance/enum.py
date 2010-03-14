'''
Created on Mar 14, 2010

@author: rregenol
'''

class PREF_KEYS(object):
    IMG_DIR = 'imgDir'
    PERIOD = 'period'
    STARTUP = 'startup'
    
class PERIOD(object):
    EVERY_LOG_IN = '-1'
    
class PERIOD_VALUES(object):
    items = ({'label': 'Every time I log in', 'value': -1}, {'label': 'Every hour', 'value': 60}, {'label': 'Every 30 minutes', 'value': 30})
    @staticmethod
    def toStringList():
        return [item['label'] for item in PERIOD_VALUES.items]
    @staticmethod
    def getValue(index):
        return PERIOD_VALUES.items[index]['value']
    @staticmethod
    def getIndex(value):
        index = 0
        for item in PERIOD_VALUES.items:
            if int(value) == item['value']: return index
            index += 1
        return 0