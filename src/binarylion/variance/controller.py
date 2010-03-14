'''
This module contains the commands used by the application.

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

from binarylion.variance import AppFacade, proxy, view

from puremvc.interfaces import ICommand
from puremvc.patterns.command import SimpleCommand, MacroCommand
        
class StartupCommand(MacroCommand, ICommand):
    def initializeMacroCommand(self):
        self.addSubCommand(ModelInitCommand)
        self.addSubCommand(ViewInitCommand)
        self.addSubCommand(CommandInitCommand)
        self.addSubCommand(SetupEnvironmentCommand)
        
class SetupEnvironmentCommand(SimpleCommand, ICommand):
    def execute(self, note):
        env = self.facade.retrieveProxy(proxy.EnvProxy.NAME)
        env.setup()
        
class ViewInitCommand(SimpleCommand, ICommand):
    '''Command that registers mediators.'''
    def execute(self, note):
        appPanel = note.getBody()
        self.facade.registerMediator(view.ActionsPanelMediator(appPanel.actionsPanel))
        
class CommandInitCommand(SimpleCommand, ICommand):
    '''Command that registers other commands.'''
    def execute(self, note):
        self.facade.registerCommand(AppFacade.APPLY_CHANGES, ApplyChangesCommand)
    
class ModelInitCommand(SimpleCommand, ICommand):
    '''Command that registers proxies.'''
    def execute(self, note):
        self.facade.registerProxy(proxy.EnvProxy())
        self.facade.registerProxy(proxy.PrefsProxy())
    
class ApplyChangesCommand(SimpleCommand, ICommand):
    def execute(self, note):
        print 'Saving changes'
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        print prefs.getImgDir()
        prefs.save()