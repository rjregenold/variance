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

controller.py
This module contains the commands used by the application.

@author: RJ Regenold
'''

import puremvc.patterns.command
import puremvc.interfaces
        
class StartupCommand(puremvc.patterns.command.MacroCommand, puremvc.interfaces.ICommand):
    def initializeMacroCommand(self):
        self.addSubCommand(ModelInitCommand)
        self.addSubCommand(ViewInitCommand)
        self.addSubCommand(CommandInitCommand)
        
class ViewInitCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    '''Command that registers mediators.'''
    def execute(self, note):
        appFrame = note.getBody()
        
class CommandInitCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    '''Command that registers other commands.'''
    def execute(self, note):
        pass
    
class ModelInitCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    '''Command that registers proxies.'''
    def execute(self, note):
        pass