import pyautogui
import os
import time
import random
from Looter import Looter


l = Looter()

while(True):

    time.sleep(1 + random.random())
    pyautogui.press('space')
    time.sleep(3 + random.random())
    l.loot()