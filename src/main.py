'''
Main module that bootstraps the application.

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

# TODO: Look at python gettext for localization
# TODO: Think about rating system. Allow user to thumbs up/down a wallpaper, etc...
# TODO: Replace print stmts with python logging

from binarylion.variance import AppFacade, components
        
if __name__ == '__main__':
    app = AppFacade.getInstance()
    wxApp = components.WxApp(False)
    app.sendNotification(AppFacade.STARTUP, wxApp.appFrame.appPanel)
    wxApp.MainLoop()