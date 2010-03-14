'''
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

components.py
This module contains the various wx components
that make up the user interface of the application.

@author: RJ Regenold
'''

import wx

COMPONENT_BORDER = 5

class WxApp(wx.App):
    '''The wx app.'''
    appFrame = None
    def OnInit(self):
        self.appFrame = AppFrame()
        self.appFrame.Show()
        return True
    
class AppFrame(wx.Frame):
    '''The application frame that contains all the various configuration panels.'''
    periodPanel = None
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='Variance by Binary Lion Studios', size=(500, 300))
        self.periodPanel = PeriodPanel(self)
        self.arrangePanels()
    def arrangePanels(self):
        '''Arranges the high level panels.'''
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.periodPanel, 1)
        vbox.Add(hbox, 1)
        self.SetAutoLayout(True)
        self.SetSizer(vbox)
        self.Layout()
        
class PeriodPanel(wx.Panel):
    '''This panel contains the options for how often to change the wallpaper.'''
    radioBox = None
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.createChildren()
    def createChildren(self):
        self.radioBox = wx.RadioBox(self, majorDimension=1, label='Change my wallpaper:', choices=['Every time I log in', 'Every hour', 'Every 30 minutes'])
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.radioBox, 0, wx.TOP | wx.LEFT, COMPONENT_BORDER)
        self.SetAutoLayout(True)
        self.SetSizer(vbox)
        self.Layout()