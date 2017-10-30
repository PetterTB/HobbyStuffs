import pyautogui
import os
import time


class CharWalker:


    def __init__(self):

        self.dirs = ['up']*30
        self.dirs.extend(['down']*30)

        self.current_dirs = self.dirs

    def walk(self):

        if not self.current_dirs:
            self.current_dirs = self.dirs

        return self.current_dirs.pop()

def FirstRook():

    walker = CharWalker()

    while(True):

        time.sleep(1)
        pyautogui.press('space')
        pyautogui.press(walker.walk())