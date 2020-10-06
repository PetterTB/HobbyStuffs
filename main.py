# import the opencv library
from PIL import ImageTk
import tkinter as tk
import GameWorld

class MainApp:

    def __init__(self):

        self.world = GameWorld.GameWorld()

        self.gui = tk.Tk()
        self.c1 = tk.Canvas(self.gui, width=1200, height=600)
        self.c1.pack(expand=True)

        self.do_one_tick()
        self.gui.mainloop()

    def do_one_tick(self):

        self.world.update()

        self.bmpimg = ImageTk.PhotoImage(self.world.latest_input_image)
        self.c1.create_image(0, 0, image=self.bmpimg, anchor=tk.NW)



        self.gui.after(50, self.do_one_tick)


if __name__ == '__main__':
    MainApp()
