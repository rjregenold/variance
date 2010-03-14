'''
Created on Mar 14, 2010

@author: rregenol
'''

import binarylion.variance

from puremvc.patterns.mediator import Mediator
from puremvc.interfaces import IMediator

import wx

class ActionsPanelMediator(Mediator, IMediator):
    '''The actions panel mediator.'''
    NAME = 'actions panel mediator'
    def __init__(self, viewComponent):
        Mediator.__init__(self, ActionsPanelMediator.NAME, viewComponent)
        # Add event listeners
        self.viewComponent.okButton.Bind(wx.EVT_BUTTON, self.onOkClicked)
    def onOkClicked(self, e):
        self.sendNotification(binarylion.variance.AppFacade.APPLY_CHANGES)