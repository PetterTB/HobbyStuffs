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


    time.sleep(1 + random.random())
    pyautogui.press('space')
    time.sleep(6 + random.random())
    if i%2 == 0:
        pyautogui.press('2')
    s2 = ScreenGrab()
    s2.b_box = (0,0) + (1176,91)
    if not s2.is_creature_present():
        l.loot_all_squares_around_char()
        s = ScreenGrab()
        s.set_map_bb()
        s.grab_screen()
        coords = s.find_random_map_point()
        m.left_click(coords[0], coords[1])
