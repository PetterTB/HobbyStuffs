import pyautogui
import time
import random

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
    pyautogui.click()

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

tick = 8
while(tick):
    tick += 1
    time.sleep(random.random() + 0.5)

    if (tick % 10 == 0):
        loot()
        next()

    if (tick % 15 == 0):
        heal()

