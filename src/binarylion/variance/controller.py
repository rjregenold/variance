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

from binarylion.variance import AppFacade, proxy, view, service, enum

from puremvc.interfaces import ICommand
from puremvc.patterns.command import SimpleCommand, MacroCommand
import os
        
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
        self.facade.registerMediator(view.AppPanelMediator(appPanel))
        self.facade.registerMediator(view.PeriodPanelMediator(appPanel.periodPanel))
        self.facade.registerMediator(view.ImageDirPanelMediator(appPanel.imageDirPanel))
        self.facade.registerMediator(view.ActionsPanelMediator(appPanel.actionsPanel))
        
class CommandInitCommand(SimpleCommand, ICommand):
    '''Command that registers other commands.'''
    def execute(self, note):
        self.facade.registerCommand(AppFacade.DATABASE_READY, DatabaseReadyCommand)
        self.facade.registerCommand(AppFacade.APPLY_CHANGES, ApplyChangesCommand)
        self.facade.registerCommand(AppFacade.INSTALL_STARTUP_SERVICE, InstallStartupServiceCommand)
        self.facade.registerCommand(AppFacade.REMOVE_STARTUP_SERVICE, RemoveStartupServiceCommand)
    
class ModelInitCommand(SimpleCommand, ICommand):
    '''Command that registers proxies.'''
    def execute(self, note):
        self.facade.registerProxy(proxy.EnvProxy())
        self.facade.registerProxy(proxy.PrefsProxy())
        
class DatabaseReadyCommand(SimpleCommand, ICommand):
    def execute(self, note):
        self.facade.retrieveProxy(proxy.PrefsProxy.NAME).load()
        self.facade.sendNotification(AppFacade.ENVIRONMENT_READY)
    
class ApplyChangesCommand(SimpleCommand, ICommand):
    def execute(self, note):
        print 'Saving changes'
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        prefs.save()
        
class InstallStartupServiceCommand(SimpleCommand, ICommand):
    def execute(self, note):
        print 'Installing startup service'
        windowsService = service.WindowsService()
        targetPath = os.path.join(os.getcwd(), enum.STARTUP_APP_NAME)
        windowsService.installStartup(targetPath, os.getcwd(), enum.SHORTCUT_NAME)
        
class RemoveStartupServiceCommand(SimpleCommand, ICommand):
    def execute(self, note):
        print 'Removing startup service'
        windowsService = service.WindowsService()
        windowsService.removeStartup(enum.SHORTCUT_NAME)
        
### Startup service commands ###

class ServiceStartupCommand(SimpleCommand, ICommand):
    def execute(self, note):
        # Register proxies
        self.facade.registerProxy(proxy.EnvProxy())
        self.facade.registerProxy(proxy.PrefsProxy())
        # Register commands
        self.facade.registerCommand(AppFacade.INIT_ENVIRONMENT, SetupEnvironmentCommand)
        self.facade.registerCommand(AppFacade.DATABASE_READY, DatabaseReadyCommand)
        self.facade.registerCommand(AppFacade.ENVIRONMENT_READY, ServiceEnvironmentReadyCommand)
        # Kick things off
        self.facade.sendNotification(AppFacade.INIT_ENVIRONMENT)
        
class ServiceEnvironmentReadyCommand(SimpleCommand, ICommand):
    def execute(self, note):
        prefs = self.facade.retrieveProxy(proxy.PrefsProxy.NAME)
        startupService = service.StartupService(prefs.prefs().imgDir, int(prefs.prefs().period))
        startupService.run()