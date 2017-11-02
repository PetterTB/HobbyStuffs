import pyautogui
import os
import time
import random
from Looter import Looter
from Mouse import Mouse
from ScreenGrab import ScreenGrab

m = Mouse()
l = Looter(m)

while(True):

    s = ScreenGrab()
    s.set_map_bb()
    s.grab_screen()
    coords = s.find_random_map_point()
    m.left_click(coords[0], coords[1])

    for i in range(3):
        time.sleep(1 + random.random())
        pyautogui.press('space')
        time.sleep(6 + random.random())
        pyautogui.press('2')
        l.loot_all_squares_around_char()