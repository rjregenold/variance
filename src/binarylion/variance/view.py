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

class AppPanelMediator(Mediator, IMediator):
    NAME = 'app panel mediator'
    def __init__(self, viewComponent):
        Mediator.__init__(self, AppPanelMediator.NAME, viewComponent)
    def listNotificationInterests(self):
        return [
            AppFacade.PREFS_SAVED
        ]
    def handleNotification(self, note):
        if note.getName() == AppFacade.PREFS_SAVED:
            self.viewComponent.showPrefsSaved()

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
            self.setDefaultValues()
    def setDefaultValues(self):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        print prefs.prefs().period
        index = enum.PERIOD_VALUES.getIndex(prefs.prefs().period)
        print index
        self.viewComponent.radioBox.SetSelection(index)
    def onPeriodChange(self, e):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        prefs.prefs().period = enum.PERIOD_VALUES.items[self.viewComponent.radioBox.GetSelection()]['value']
        print prefs.prefs().period
        
class ImageDirPanelMediator(Mediator, IMediator):
    NAME = 'image dir panel mediator'
    def __init__(self, viewComponent):
        Mediator.__init__(self, ImageDirPanelMediator.NAME, viewComponent)
        # Add event listeners
        self.viewComponent.imageDir.Bind(wx.EVT_DIRPICKER_CHANGED, self.onImageDirChanged)
    def listNotificationInterests(self):
        return [
            AppFacade.ENVIRONMENT_READY
        ]
    def handleNotification(self, note):
        if note.getName() == AppFacade.ENVIRONMENT_READY:
            self.setDefaultValues()
    def setDefaultValues(self):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        self.viewComponent.imageDir.SetPath(prefs.prefs().imgDir)
    def onImageDirChanged(self, e):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        prefs.prefs().imgDir = self.viewComponent.imageDir.GetPath()

class ActionsPanelMediator(Mediator, IMediator):
    '''The actions panel mediator.'''
    NAME = 'actions panel mediator'
    def __init__(self, viewComponent):
        Mediator.__init__(self, ActionsPanelMediator.NAME, viewComponent)
        # Add event listeners
        self.viewComponent.startupCheckbox.Bind(wx.EVT_CHECKBOX, self.onStartupToggled)
        self.viewComponent.okButton.Bind(wx.EVT_BUTTON, self.onOkClicked)
    def listNotificationInterests(self):
        return [
            AppFacade.ENVIRONMENT_READY,
            AppFacade.PREFS_SAVED
        ]
    def handleNotification(self, note):
        if note.getName() == AppFacade.ENVIRONMENT_READY:
            self.setDefaultValues()
        elif note.getName() == AppFacade.PREFS_SAVED:
            self.onPrefsSaved(note.getBody())
    def setDefaultValues(self):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        print prefs.prefs().startup
        self.viewComponent.startupCheckbox.SetValue(prefs.prefs().startup)
    def onStartupToggled(self, e):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        prefs.prefs().startup = self.viewComponent.startupCheckbox.IsChecked()
        print prefs.prefs().startup
    def onOkClicked(self, e):
        self.sendNotification(AppFacade.APPLY_CHANGES)
    def onPrefsSaved(self, prefs):
        if(prefs.startup):
            self.facade.sendNotification(AppFacade.INSTALL_STARTUP_SERVICE)
        else:
            self.facade.sendNotification(AppFacade.REMOVE_STARTUP_SERVICE)