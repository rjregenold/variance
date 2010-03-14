'''
This module contains the mediators for the application.

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

from binarylion.variance import AppFacade, proxy, enum

from puremvc.patterns.mediator import Mediator
from puremvc.interfaces import IMediator

import wx

class PeriodPanelMediator(Mediator, IMediator):
    NAME = 'period panel mediator'
    def __init__(self, viewComponent):
        Mediator.__init__(self, PeriodPanelMediator.NAME, viewComponent)
        # Add event listeners
        self.viewComponent.radioBox.Bind(wx.EVT_RADIOBOX, self.onPeriodChange)
    def listNotificationInterests(self):
        return [
            AppFacade.ENVIRONMENT_READY
        ]
    def handleNotification(self, note):
        if note.getName() == AppFacade.ENVIRONMENT_READY:
            self.setDefaultValue()
    def setDefaultValue(self):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        print prefs.prefs().period
        index = enum.PERIOD_VALUES.getIndex(prefs.prefs().period)
        print index
        self.viewComponent.radioBox.SetSelection(index)
    def onPeriodChange(self, e):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        prefs.prefs().period = enum.PERIOD_VALUES.items[self.viewComponent.radioBox.GetSelection()]['value']
        print prefs.prefs().period

class ActionsPanelMediator(Mediator, IMediator):
    '''The actions panel mediator.'''
    NAME = 'actions panel mediator'
    def __init__(self, viewComponent):
        Mediator.__init__(self, ActionsPanelMediator.NAME, viewComponent)
        # Add event listeners
        self.viewComponent.okButton.Bind(wx.EVT_BUTTON, self.onOkClicked)
    def onOkClicked(self, e):
        self.sendNotification(AppFacade.APPLY_CHANGES)