import os
import pyautogui
import random
import unittest
import time


class MouseMock:

    def __init__(self):
        pass

    def left_click(self, x,y):
        print("mouse.left_click",x,y)

    def left_click_pos(self, pos):
        print("mouse.left_click_pos",pos)

    def right_click(self, x,y):
        print("mouse.left_click", x, y)

    def drag(self,from_x, from_y, to_x,to_y):
        print("mouse.drag", from_x, from_y, to_x, to_y)

class Mouse:

    def __init__(self):
        pass

    def left_click(self, x,y):
        pyautogui.moveTo(x,y, 0.1)
        time.sleep(0.1)
        pyautogui.click()

    def left_click_pos(self, pos):
        self.left_click(pos[0],pos[1])

    def right_click(self, x,y):
        pyautogui.moveTo(x,y, 0.1)
        time.sleep(0.1)
        pyautogui.click(button='right')

    def drag(self,from_x, from_y, to_x,to_y):
        pyautogui.moveTo(from_x, from_y, 0.1)
        time.sleep(0.1)
        pyautogui.dragTo(to_x,to_y, button='left')

class TestMouse(unittest.TestCase):

    def setUp(self):
        self.m = Mouse()
    def test_naively(self):

        self.m.left_click(100,100)
        self.m.right_click(100,100)
        self.m.left_click(200,200)
        self.m.drag(300,300,510,510)
        return
    def test_click_pos(self):
        #m=Mouse()
        self.m.left_click_pos((100,100))

if __name__ == '__main__':
    unittest.main()