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

Contains the application facade.

@author: RJ Regenold
'''

import puremvc.patterns.facade
from binarylion.variance import controller, components

class AppFacade(puremvc.patterns.facade.Facade):
    '''The application facade.'''
    STARTUP = 'startup'
    @staticmethod
    def getInstance():
        return AppFacade()
    def __init__(self):
        self.initializeFacade()
    
    def initializeFacade(self):
        super(AppFacade, self).initializeFacade()
        self.initializeController()
        
    def initializeController(self):
        super(AppFacade, self).initializeController()
        # register startup command
        super(AppFacade, self).registerCommand(AppFacade.STARTUP, controller.StartupCommand)