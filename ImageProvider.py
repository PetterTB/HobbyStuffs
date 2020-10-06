import cv2
from PIL import Image


class ImageProvider:
    """Singleton for image access.

    Initializing camera takes a few seconds. Do that once.
    """

    def __init__(self):
        # Defines camera object. 1 means second webcam.
        self.vid = cv2.VideoCapture(1)
        # Display the resulting frame
        # cv2.imshow('frame', frame)
        # cv2.waitKeyEx(1)

    def __del__(self):
        self.vid.release()

    def get_pil_image(self):
        r, frame = self.vid.read()
        return Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))