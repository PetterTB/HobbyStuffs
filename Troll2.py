import pyautogui
import time
import random
from bp import get_bb_items, get_bp_bbs
from ScreenShot import get_screen_shot
from mapper import MiniMap

centre_x = 740
centre_y = 320
pos_around_char = []

def heal():
    pyautogui.press("1")
    pyautogui.press("2")

def next():
    pyautogui.keyDown("ctrl")
    pyautogui.press("space")
    pyautogui.keyUp("ctrl")

def left_click(x, y):
    pyautogui.moveTo(x, y, 0.1)
    time.sleep(0.1)
    pyautogui.click()

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

tick = 4
while(tick):
    tick += 1
    time.sleep(random.random() + 0.5)

    if (tick % 5 == 0):
        next()

    if (tick % 15 == 0):
        loot()
        heal()
        pos = MiniMap().get_minimap_move_pos(get_screen_shot())
        print("Moving to! : ", pos)
        left_click(pos[0], pos[1])

