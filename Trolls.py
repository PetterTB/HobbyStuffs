import pyautogui
import os
import time
import random
from Looter import Looter
from Mouse import Mouse

m = Mouse()
l = Looter(m)

while(True):

    time.sleep(1 + random.random())
    pyautogui.press('space')
    time.sleep(3 + random.random())
    l.loot_all_squares_around_char()