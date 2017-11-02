import pyautogui
import os
import time
import random
from Looter import Looter
from Mouse import Mouse
from ScreenGrab import ScreenGrab

m = Mouse()
l = Looter(m)

def check_creatures_present():
    s2 = ScreenGrab()
    s2.b_box = (0,0) + (1176,91)
    s2.grab_screen()
    return s2.is_creature_present()

while(True):

    i = 0;
    time.sleep(1 + random.random())
    pyautogui.press('space')
    time.sleep(6 + random.random())
    if i%3 == 0:
        pyautogui.press('2')
    if not check_creatures_present():
        l.loot_all_squares_around_char()

    while not check_creatures_present():
        s = ScreenGrab()
        s.set_map_bb()
        s.grab_screen()
        coords = s.find_random_map_point()
        m.left_click(coords[0], coords[1])
        time.sleep(10)
    i += 1
