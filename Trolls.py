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

i = 1
coords = None

while(True):

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
        if(random.randint(0,10) == 10):
            coords=s.find_random_map_point()
        else:
            coords = s.find_similar_map_point(coords)
        m.left_click(coords[0], coords[1])
        for i in range(10):
            if check_creatures_present():
                pyautogui.press('space')
                break
            time.sleep(1)
    i += 1
