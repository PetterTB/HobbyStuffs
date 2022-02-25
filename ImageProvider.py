import cv2
from PIL import Image
from positions import Positions

import debugcontrol


class ImageProvider:
    """Singleton for image access.

    Initializing camera takes a few seconds. Do that once.
    """

    def __init__(self):

        self.reapeat_window = debugcontrol.Debugcontrol.get("repeat_window_bmp")

        self.vid = None

        if not self.reapeat_window:
            self._init_video()

    def _init_video(self):
        print("starting cam")
        # Defines camera object. 1 means second webcam.
        self.vid = cv2.VideoCapture(1)
        # Display the resulting frame
        # cv2.imshow('frame', frame)
        # cv2.waitKeyEx(1)
        print("started cam")

    def get_pil_image(self):
        if self.reapeat_window:
            return Image.open("window.bmp")

        r, frame = self.vid.read()
        ul = Positions.get("cam_tibia_window_ul")
        lr = Positions.get("cam_tibia_window_lr")

        return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).crop(ul + lr)


