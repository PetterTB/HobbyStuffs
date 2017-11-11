import pyautogui
import os
import time
import random
from Looter import Looter, LooterMock
from GameInput import GameInput, GameInputMock
from ScreenGrab import ScreenGrab, ScreenGrabStub
import unittest

from ScreenPositions import pos_minimap_floor_down, pos_minimap_floor_up
from ScreenPositions import pos_around_char

class CaveHunter:

    def __init__(self, input):
        self.m = input
        self.l = Looter(self.m)
        self.s = ScreenGrab()
        self.s.set_map_bb()

        self.up_down_pixel = (255, 255, 0)

    def hunt_floor(self, seconds):

        start = time.time()
        end = start + seconds

        met_mobs_last = False
        c = 0
        self.s.grab_screen()
        coords = self.s.find_random_map_point()
        walk_counter = 0

        while time.time() < end:

            time.sleep(1 + random.random())

            creatures_present = self.check_creatures_present()
            print("Creatures present?: ", creatures_present)

            if met_mobs_last:
                self.l.loot_all_squares_around_char()

            met_mobs_last = creatures_present
            if creatures_present:
                c+=1
                self.attack_mob()
                self.cast_and_eat(c)
                walk_counter = 0
            else:
                if walk_counter<=0:
                    coords = self.simple_map_walk(coords)
                    walk_counter = 5
                else:
                    walk_counter-=1

    def cast_and_eat(self, c):
        if c % 15 == 0:
            print("Eating.")
            self.m.press_key('1')
        if c % 3 == 0:
            print("Healing.")
            time.sleep(0.3)
            self.m.press_key('2')

    def attack_mob(self):
        self.m.press_key('space')
        # Kill creature sleep.
        time.sleep(2 + random.random())

    def simple_map_walk(self, last_coords):

        self.s.grab_screen()
        s = "Walking to map point: "
        coords = (0,0)
        if (random.randint(0, 10) == 10):
            coords = self.s.find_random_map_point()
            s += "random point: " + str(coords)
        else:
            coords = self.s.find_similar_map_point(last_coords)
            s += "similar point: " + str(coords)
        self.m.left_click(coords[0], coords[1])
        return coords

    def check_creatures_present(self):
        self.s.b_box = (0, 0) + (1176, 91)
        self.s.grab_screen()
        returnval = self.s.is_creature_present()
        self.s.set_map_bb()
        return returnval

    def go_up_with_rope(self):

        up = self.find_up()
        self.m.left_click_pos(up)

        for pos in pos_around_char:
            self.m.press_key('4')
            self.m.left_click_pos(pos)
            time.sleep(0.4)

    def go_down(self):
        down = self.find_up(return_down=True)
        self.m.left_click_pos(down)
        time.sleep(25)

    def is_up_pixel(self, pos):
        """This function should be somewhere else. Here for now. =(
        Might be kinda ugly-ly written. This is why."""

        self.m.left_click_pos(pos_minimap_floor_down)
        self.s.grab_screen()
        self.m.left_click_pos(pos_minimap_floor_up)
        if self.s.get_pixel_from_img(pos) == self.up_down_pixel:
            return True
        else:
            return False

    def find_up(self, return_down=False):

        x_max = self.s.get_max_x()
        y_max = self.s.get_max_y()

        result_list = []

        for x in x_max:
            for y in y_max:
                if self.s.get_pixel_from_img((x,y)) == self.up_down_pixel:
                    print("Found hole/rope candidate.")
                    is_up = self.is_up_pixel()
                    print("     is_up: ", is_up)
                    if is_up and (not return_down):
                        result_list.append(self.s.make_absolute_coords((x,y)))
                    if (not is_up) and return_down:
                        result_list.append(self.s.make_absolute_coords((x, y)))

        if not result_list:
            return None
        result_list = sorted(result_list,
                             key=lambda x: (abs(x[0]-1250)+abs(x[1]-80)))
        print("List of up/down hole candidates: ", result_list)
        return result_list[0]

class TestCaveHunter(unittest.TestCase):

    def setUp(self):
        self.hunter = CaveHunter(GameInputMock())
        self.hunter.l = LooterMock()
        self.hunter.s = ScreenGrabStub()
        self.hunter.s.test_files = [r'C:\dev\HobbyStuffs\Archive_input\test_wasps.png']*200

    def test_hunt_for_time(self):
        self.hunter.hunt_floor(0)

    def test_find_up(self):
        pass


if __name__ == "__main__":
    unittest.main()
