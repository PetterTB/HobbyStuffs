from PIL import ImageGrab
import os
import time
from CaveHunter import CaveHunter
from GameInput import GameInput
import argparse


def screenGrab():
    #box = (157, 346, 796, 825)
    box = ()
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
            '.png', 'PNG')

def parse_args():
    pass

def main():
    while(True):

        c = CaveHunter(GameInput())
        c.hunt_floor(100)
        c.go_down()
        c.hunt_floor(100)
        c.go_down()
        c.hunt_floor(100)
        c.go_up_with_rope()
        c.hunt_floor(50)
        c.go_up_with_rope()


if __name__ == '__main__':
    main()