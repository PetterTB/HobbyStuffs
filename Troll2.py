import pyautogui
import time
import random
from bp import get_bb_items, get_bp_bbs
from ScreenShot import get_screen_shot

centre_x = 740
centre_y = 320
pos_around_char = []

def heal():
    pyautogui.press("1")
    pyautogui.press("2")

def next():
    pyautogui.press("space")

def left_click(x, y):
    pyautogui.moveTo(x, y, 0.1)
    time.sleep(0.1)
    autogui.click()

def check_loot():

    items = get_bb_items(get_screen_shot())
    bbs = get_bp_bbs()

    items.reverse()
    bbs.reverse()

    for item, bb in zip(items, bbs):
        if item["name"] in ["worthless"]:
            print("found worthless item!")
            pyautogui.moveTo((bb[0] + bb[2])/2, (bb[1] + bb[3])/2, 0.1)
            time.sleep(0.1)
            pyautogui.dragTo(centre_x, centre_y , button='left')

def loot():
    pyautogui.keyDown('alt')
    left_click(centre_x + 40, centre_y - 40)
    left_click(centre_x + 40, centre_y)
    left_click(centre_x + 40, centre_y + 40)
    left_click(centre_x, centre_y - 40)
    left_click(centre_x, centre_y + 40)
    left_click(centre_x - 40, centre_y - 40)
    left_click(centre_x - 40, centre_y)
    left_click(centre_x - 40, centre_y + 40)
    pyautogui.keyUp('alt')

    check_loot()

tick = 8
while(tick):
    tick += 1
    time.sleep(random.random() + 0.5)

    if (tick % 10 == 0):
        loot()
        next()

    if (tick % 15 == 0):
        heal()

