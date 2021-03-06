'''
This module contains the various wx components
that make up the user interface of the application.

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

import wx
from binarylion.variance import enum

# The app border size
APP_BORDER = 10
# The standard component border size
COMPONENT_BORDER = 5

class WxApp(wx.App):
    '''The wx app.'''
    appFrame = None
    def OnInit(self):
        self.appFrame = AppFrame(parent=None, title='Variance by Binary Lion Studios', size=(500, 300))
        self.appFrame.Show()
        return True
    
class AppFrame(wx.Frame):
    '''The application frame that contains all the various configuration panels.'''
    appPanel = None
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.createChildren()
        self.SetIcon(wx.Icon('variance.ico', wx.BITMAP_TYPE_ICO))
    def createChildren(self):
        self.appPanel = AppPanel(parent=self)
        self.Panel = self.appPanel
        self.Fit()
        
class AppPanel(wx.Panel):
    periodPanel = None
    actionsPanel = None
    imageDirPanel = None
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.createChildren()
    def createChildren(self):
        self.periodPanel = PeriodPanel(parent=self)
        self.imageDirPanel = ImageDirPanel(parent=self)
        self.actionsPanel = ActionsPanel(parent=self)
        
        rootSizer = wx.BoxSizer(wx.VERTICAL)
        vbox = wx.BoxSizer(wx.VERTICAL)        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(self.periodPanel, 0)
        hbox.Add((10,0), 1)
        hbox.Add(self.imageDirPanel, 0)
        
        vbox.Add(hbox, 0, wx.EXPAND)
        vbox.Add(self.actionsPanel, 1, wx.ALIGN_BOTTOM | wx.EXPAND)
        
        rootSizer.Add(vbox, 1, wx.EXPAND | wx.ALL, border=APP_BORDER)
        
        self.SetSizerAndFit(rootSizer)
    def showPrefsSaved(self):
        dialog = wx.MessageDialog(self, message='Your preferences have been saved.', caption='Preferences saved', style=wx.OK | wx.ICON_INFORMATION)
        dialog.ShowModal()
        dialog.Destroy()
        
class PeriodPanel(wx.Panel):
    '''This panel contains the options for how often to change the wallpaper.'''
    radioBox = None
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.createChildren()
    def createChildren(self):
        self.radioBox = wx.RadioBox(self, majorDimension=1, label='Change my wallpaper:', choices=enum.PERIOD_VALUES.toStringList())
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(self.radioBox, 0)
        
        self.SetSizerAndFit(vbox)
        
class ImageDirPanel(wx.Panel):
    '''This panel contains the directory selector to pick the image directory.'''
    imageDir = None
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.createChildren()
    def createChildren(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        label = wx.StaticText(self, label='Select image directory:')
        self.imageDir = wx.DirPickerCtrl(self, path='', message='Please select the directory that contains your wallpaper images.')
        self.imageDir.SetMinSize((300, 25))
        
        vbox.Add(label, 0)
        vbox.Add(self.imageDir, 0)
        
        self.SetSizerAndFit(vbox)
        
class ActionsPanel(wx.Panel):
    okButton = None
    startupCheckbox = None
    '''This panel contains the action buttons.'''
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        self.createChildren()
    def createChildren(self):
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.startupCheckbox = wx.CheckBox(self, label='Start Variance when windows starts')

        self.okButton = wx.Button(self, wx.ID_APPLY, '&Apply changes')
        self.okButton.SetDefault()
        
        hbox.Add(self.startupCheckbox, 0, wx.ALIGN_BOTTOM)
        hbox.Add((10,0), 1)
        hbox.Add(self.okButton, 0, wx.ALIGN_BOTTOM)
        
        self.SetSizerAndFit(hbox)