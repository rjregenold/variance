'''
Created on Mar 14, 2010

@author: rregenol
'''

from binarylion.variance import AppFacade

if __name__ == '__main__':
    app = AppFacade.getInstance()
    app.sendNotification(AppFacade.SERVICE_STARTUP)