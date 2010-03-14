'''
Created on Mar 13, 2010

@author: rregenol
'''
import puremvc.patterns.facade

class AppFacade(puremvc.patterns.facade.Facade):
    
    def __init__(self):
        self.initializeFacade()
    
    def initializeFacade(self):
        super(AppFacade, self).initializeFacade()
        self.initializeController()
        
    def initializeController(self):
        super(AppFacade, self).initializeController()
        