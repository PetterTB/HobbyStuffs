from PIL import ImageGrab
import os
import time
from CaveHunter import CaveHunter
from Mouse import Mouse
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
        try:
            c = CaveHunter(Mouse())
            c.hunt_floor(1000)
        except:
            print("Oi, Exception!")

    
if __name__ == '__main__':
    main()