
from puremvc.patterns.facade import Facade

class AppFacade(Facade):
    '''The application facade.'''
    STARTUP = 'startup'
    APPLY_CHANGES = 'apply changes'
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
        # FIXME: This is pretty nasty. Find a way to avoid the circular references.
        from binarylion.variance.controller import StartupCommand
        # register startup command
        super(AppFacade, self).registerCommand(AppFacade.STARTUP, StartupCommand)