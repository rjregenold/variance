'''
This module contains various constants used throughout
the application.

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

STARTUP_APP_NAME = 'startup.exe'
SHORTCUT_NAME = 'Variance'
SHORTCUT_EXT = 'lnk'
# According to http://support.microsoft.com/default.aspx?scid=97142
SPI_SETDESKWALLPAPER = 20 
# Valid image extensions
VALID_IMG_EXT = ('.jpg', '.png', '.gif', '.bmp')
# Temp directory envrionment variable name
ENV_TMP = 'TMP'
# Temp bitmap image name
TMP_IMG_NAME = 'tmp.bmp'

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