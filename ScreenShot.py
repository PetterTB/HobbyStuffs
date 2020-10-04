from PIL import ImageGrab
from PIL import Image

def get_screen_shot():
    """ Needs to be gotten from Tibia SS folder instead..
            Or from webcam.
            Or from monitor output.
            Or something.
    """
    return ImageGrab.grab()