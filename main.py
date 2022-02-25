# import the opencv library
from PIL import ImageTk
from PIL import ImageGrab
import tkinter as tk
import GameWorld
import positions
import datetime
import time

import matplotlib

import mapper


def dec2hex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


class MainApp:

    def donothing(self):
        pass

    def __init__(self):
        self.world = GameWorld.GameWorld()
        self.world.update()

        self.gui = tk.Tk()

        self.frame1 = tk.Frame(self.gui, width=700, height=550)
        self.frame1.pack(side="left")

        self.c1 = tk.Canvas(self.frame1, width=700, height=550)
        self.c1.pack(expand=True)

        self.frame_world = tk.Frame(self.gui, width=500, height=300)
        self.frame_world.pack(side="right")

        self.c2 = tk.Canvas(self.frame_world, width=300, height=300)
        self.c2.pack(expand=True)

        self.pos_text = tk.Text(self.frame_world, width=20, height=5)
        # self.pos_text.config(anchor=tk.NE)
        self.pos_text.pack()

        menubar = tk.Menu(self.gui)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.donothing)
        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Actions", menu=helpmenu)

        self.gui.config(menu=menubar)

        self.do_one_tick()
        self.gui.mainloop()

    def do_one_tick(self):
        positions.Positions()
        self.world.update()
        self.world.latest_input_image.save("tmp/window.bmp")

        self.c1.delete()
        self.bmpimg = ImageTk.PhotoImage(self.world.latest_input_image)
        self.c1.create_image(0, 0, image=self.bmpimg, anchor=tk.NW)
        self.c1.pack(expand=True)

        self.mini = ImageTk.PhotoImage(self.world.minimap.latest_minimap)

        # print("mini: ", self.mini.width(), self.mini.height())
        self.c2.create_image(0, 0, image=self.mini, anchor=tk.NW)
        self.mini2 = ImageTk.PhotoImage(self.world.minimap.latest_result_map)
        # self.c2.create_image(self.mini.width(), self.mini.height(), image = self.mini2, anchor = tk.SW)
        self.c2.create_image(0, self.mini.height(), image=self.mini2, anchor=tk.NW)

        self.pos_text.insert(1.0, str(self.world.minimap.pos) + "\n")

        self.gui.after(50, self.do_one_tick)




if __name__ == '__main__':
    MainApp()
