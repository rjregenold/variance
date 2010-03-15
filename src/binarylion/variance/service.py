'''
Created on Mar 14, 2010

@author: rregenol
'''

import ctypes, Image, os, random, time, winshell
from win32com.client import Dispatch
from binarylion.variance import enum

class WindowsService(object):
    def __init__(self):
        pass
    def installStartup(self, targetPath, workingDir, name):
        path = self.__getFullpath__(name)
        if not os.path.exists(path):
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.TargetPath = targetPath
            shortcut.WorkingDirectory = workingDir
            shortcut.save()
    def removeStartup(self, name):
        path = self.__getFullpath__(name)
        if os.path.exists(path):
            os.unlink(path)
    def __getFullpath__(self, name):
        startup = winshell.startup()
        return os.path.join(startup, '%s.%s' % (name, enum.SHORTCUT_EXT))
    
class StartupService(object):
    imgDir = None
    period = None
    imageService = None
    wallpaperService = None
    def __init__(self, imgDir, period):
        self.imgDir = imgDir
        self.period = period
        self.imageService = ImageService()
        self.wallpaperService = WallpaperService()
    def run(self):
        # FIXME: Get rid of this cast
        if self.period == int(enum.PERIOD.EVERY_LOG_IN):
            print 'Changing wallpaper once'
            self.__updateWallpaper__()
        else:
            while True:
                print 'Changing wallpaper'
                self.__updateWallpaper__()
                print 'Will change again in %d seconds' % (self.period * 60,)
                time.sleep(self.period * 60)
    def __updateWallpaper__(self):
        # First, pick a random image
        img = self.__findRandomImage__(self.imgDir)
        # Next, convert that image into a bitmap
        bmp = self.imageService.toBitmap(img)
        # Now set it as the wallpaper
        self.wallpaperService.update(bmp)
        # And clean house
        os.unlink(bmp)
    def __findRandomImage__(self, path):
        imgs = []
        # root, dirs, files
        for w in os.walk(path):
            imgs = imgs + [os.path.join(w[0], name) for name in filter(lambda x: os.path.splitext(x)[1] in enum.VALID_IMG_EXT, w[2])]
        # TODO: Add error checking if len of imgs is zero
        return imgs[random.randrange(len(imgs))]
            
class ImageService(object):
    def __init__(self):
        pass
    def toBitmap(self, path):
        '''
        Converts an image into a bitmap, writes it to the
        tmp directory, and returns the path
        '''
        tmpDir = os.environ.get(enum.ENV_TMP)
        tmpPath = os.path.join(tmpDir, enum.TMP_IMG_NAME)
        # TODO: Add error checking for failed convert. Possibly
        # write failed image path to database so the app doesn't
        # try to use that image again
        Image.open(path).save(tmpPath)
        return tmpPath 

class WallpaperService(object):
    def __init__(self):
        pass
    def update(self, sourcePath):
        ctypes.windll.user32.SystemParametersInfoA(enum.SPI_SETDESKWALLPAPER, 0, sourcePath, 0)