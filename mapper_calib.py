import tkinter as tk
import mapper
import ImageProvider
from positions import Positions
import numpy
import time
import math


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def _get_mean_rgb(im):
    """Probably a bad solution, but mehh."""
    w, h = im.size
    pixels = []
    for x in range(w):
        for y in range(h):
            pixels.append(im.getpixel((x, y)))

    r = [x[0] for x in pixels]
    g = [x[1] for x in pixels]
    b = [x[2] for x in pixels]

    new_rgb = (sum(r) / len(r), sum(g) / len(g), sum(b) / len(b))
    return new_rgb


class MapperCalib:

    map_calib_file = "runData/mapper_calib.txt"

    def __init__(self):
        self.gui = tk.Tk()

        self.gui.geometry("2000x2000")

        self.colors = dict(mapper.Minimap.automap_colors)
        self.colors_to_check = list(self.colors.keys())
        self.corrected_colors = dict()
        self.provider = ImageProvider.ImageProvider()

        self.gui.after(50, self.check_one_color)

        self.gui.mainloop()

    def check_one_color(self):
        if len(self.colors_to_check) == 0:
            self.save_answer()
            return

        color_to_check = self.colors_to_check.pop()

        self.gui.configure(bg=_from_rgb(self.colors[color_to_check]))
        self.gui.update()

        time.sleep(0.5)

        image = self.provider.get_pil_image()
        image.save("runData/" + color_to_check + ".bmp")
        map_box = Positions.get("cam_minimap_ul") + Positions.get("cam_minimap_lr")

        new_rgb = (_get_mean_rgb(image.crop(map_box)))
        self.corrected_colors[color_to_check] = new_rgb

        print(color_to_check)
        print("old rgb:", self.colors[color_to_check])
        print("new rgb:", new_rgb)

        self.gui.after(50, self.check_one_color)

    def save_answer(self):
        with(open(MapperCalib.map_calib_file, 'w')) as f:
            f.write(str(self.corrected_colors))

if __name__ == '__main__':
    MapperCalib()
