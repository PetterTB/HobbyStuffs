import pyautogui
import time
import random
from loot import get_bb_items, get_bp_bbs
from ScreenShot import get_screen_shot

def check_loot():

    items = get_bb_items(get_screen_shot())
    bbs = get_bp_bbs()

    items.reverse()
    bbs.reverse()

    for item, bb in zip(items, bbs):
        print(f'found: {item["name"]}')

check_loot()
