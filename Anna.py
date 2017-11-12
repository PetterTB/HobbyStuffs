from PIL import ImageGrab
import os
import time
from CaveHunter import CaveHunter
from GameInput import GameInput
import argparse


def screen_grab(path):

    i = 0
    while(True)
        box = ()
        im = ImageGrab.grab(box)
        save = path + str(i) + ".png"
        im.save(save, 'PNG')
        time.sleep(3)
        i += 1

def parse_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--record_to', default = None,
                        help = "Recore and store to location.")
    parser.add_argument('--hunt', default = None, help = "Which hunting style?")

    args = parser.parse_args()
    return args

def hunt_wasps():

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


def main():

    args = parse_args()
    if args.hunt == "wasp":
        hunt_wasps()



if __name__ == '__main__':
    main()