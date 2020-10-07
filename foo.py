# import the opencv library 
from PIL import ImageTk
import tkinter as tk
from ImageProvider import ImageProvider

from ImageProvider import ImageProvider

im = ImageProvider()
im.get_pil_image().save("foo.png")

