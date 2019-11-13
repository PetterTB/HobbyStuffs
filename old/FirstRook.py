import pyautogui
import os
import time
import random


class CharWalker:


    def __init__(self):

        self.dirs = ['left']*30
        self.dirs.extend(['right']*30)

        self.current_dirs = list(self.dirs)

    def walk(self):

        if not self.current_dirs:
            self.current_dirs = list(self.dirs)

        return self.current_dirs.pop()

def FirstRook():

    while(True):

        time.sleep(2 + random.random())
        pyautogui.press('space')
        time.sleep(1 + random.random())
        pyautogui.press('1')