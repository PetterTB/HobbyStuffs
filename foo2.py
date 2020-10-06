# import the opencv library 
import cv2
from PIL import Image
import tkinter as tk

# define a video capture object
vid = cv2.VideoCapture(1)

# Capture the video frame
# by frame
ret, frame = vid.read()

# Display the resulting frame
cv2.imshow('frame', frame)

# the 'q' button is set as the
# quitting button you may use any
# desired button of your choice

gui = tk.Tk()

c1 = tk.Canvas(gui, width=600, height=300)

gui.update(expand = True, fill = tk.BOTH)

input()

print("Do we get here?")

# After the loop release the cap object
vid.release()
# Destroy all the windows 
cv2.destroyAllWindows()