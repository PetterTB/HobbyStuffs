# import the opencv library 
from PIL import ImageTk
import tkinter as tk
from ImageProvider import ImageProvider

from ImageProvider import ImageProvider

im = ImageProvider()
gui = tk.Tk()

c1 = tk.Canvas(gui, width=1000, height=500)
c1.pack(expand=True)

im.get_pil_image().show()

bmpimg = ImageTk.PhotoImage(im.get_pil_image())

c1.create_image(0, 0, image=bmpimg, anchor=tk.NW)

gui.mainloop()
