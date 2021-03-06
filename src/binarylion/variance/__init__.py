'''
Contains the application facade.

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

from puremvc.patterns.facade import Facade

class AppFacade(Facade):
    '''The application facade.'''
    STARTUP = 'startup'
    SERVICE_STARTUP = 'service startup'
    DATABASE_READY = 'database ready'
    INIT_ENVIRONMENT = 'init environment'
    ENVIRONMENT_READY = 'env ready'
    APPLY_CHANGES = 'apply changes'
    PREFS_SAVED = 'prefs saved'
    INSTALL_STARTUP_SERVICE = 'install startup service'
    REMOVE_STARTUP_SERVICE = 'remove startup service'
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
        # FIXME: Not a fan of this. Find a way to avoid the circular references.
        from binarylion.variance.controller import StartupCommand, ServiceStartupCommand
        # register startup command
        super(AppFacade, self).registerCommand(AppFacade.STARTUP, StartupCommand)
        super(AppFacade, self).registerCommand(AppFacade.SERVICE_STARTUP, ServiceStartupCommand)