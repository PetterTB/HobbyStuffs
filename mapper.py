from PIL import ImageGrab
from PIL import Image

import unittest
import random

import math

# Used for position finding.
import cv2 as cv
import numpy as np

# from matplotlib import pyplot as plt

MINIMAP_CENTRE = (1778, 103)


class MapPoint():
    def __init__(self, point, floor=0):
        self.p = point
        self.x = point[0]
        self.y = point[1]
        self.floor = floor

    def __eq__(self, other):
        return self.p == other.p and self.floor == other.floor

    def __hash__(self):
        return self.floor*1000+self.y*100+ self.x


class FullMap():
    """ All points on map are assumed to be of type "MapPoint".
    """

    def __init__(self):
        self.map = "maps/floor-07-map.png"
        self.map_path = "maps/floor-07-path.png"

        self.map_img = Image.open(self.map)
        self.map_img = self.map_img.convert("RGB")
        self.map_path_img = Image.open(self.map_path)
        self.map_path_img = self.map_path_img.convert("RGB")

        # from level -8 to level 7
        self.maps = {}
        self.path_maps = {}

        for x in range(0, 15):
            floor = -x + 7
            path_str = str(x)
            if len(path_str) == 1:
                path_str = "0" + path_str
            self.maps[floor] = Image.open(f"maps/floor-{path_str}-map.png").convert("RGB")
            self.path_maps[floor] = Image.open(f"maps/floor-{path_str}-path.png").convert("RGB")

    def find_path(self, start, dest):
        """Params are given in map pixel coords.
        """

        open_set = [start]

        costs = {start: 0}
        came_from = {}

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while open_set:
            open_set.sort(key=lambda x: costs[x])
            node = open_set.pop(0)

            if node == dest:
                print("Found res!")
                path = []
                path_node = dest
                while path_node in came_from.keys():
                    path.append(path_node)
                    path_node = came_from[path_node]
                #self.print_pixels(path)
                return path

            for next_node, step_cost in self.get_neighbors_and_cost(node):
                if self.get_walkable(next_node.p):
                    cost = step_cost + costs[node] + self.euclide_dist(next_node.p, dest.p)
                    if cost < self.get_cost(costs, next_node):
                        if next_node not in open_set:
                            open_set.append(next_node)
                        came_from[next_node] = node
                        costs[next_node] = cost

    def get_neighbors_and_cost(self, point):
        """ point is assumed to be a MapPoint.
        """

        res = []

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for n in neighbors:
            stepCost = 4
            if n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                stepCost = 1

            p = MapPoint(((point.x + n[0]), (point.y + n[1])), point.floor)
            res.append((p, stepCost))
        return res

    def get_cost(self, costs, node):
        if node not in costs.keys():
            return 100000000
        return costs[node]

    def euclide_dist(self, p1, p2):
        x = p2[0] - p1[0]
        y = p2[1] - p1[1]
        return math.sqrt(x * x + y * y)

    def print_pixels(self, pixels):

        x_vals = [x[0] for x in pixels]
        y_vals = [x[1] for x in pixels]

        bbox = (min(x_vals) - 1, min(y_vals) - 1, max(x_vals) + 1, max(y_vals) + 1)
        im = self.map_img.copy()

        for p in pixels:
            im.putpixel(p, (255, 0, 0))

        im = im.crop(bbox)

        im.show()

        im.save("mapper_foo.png")

    def get_walkable(self, node):

        pixel = self.map_path_img.getpixel(node)

        yellow = (255, 255, 0)
        white = (250, 250, 250)

        if pixel == yellow or pixel == white:
            return False
        else:
            return True

    def find_position(self, image):
        """ Uses minimap to find char position.
                This assumes that the minimap is at the second largest magnification.
        """
        mmap = image.crop((MINIMAP_CENTRE[0] - 50, MINIMAP_CENTRE[1] - 50,
                           MINIMAP_CENTRE[0] + 50, MINIMAP_CENTRE[1] + 50))

        mmap = mmap.resize((80, 80), Image.ANTIALIAS)

        pos_minimap = self.find_position_from_minimap(mmap)

        return (pos_minimap[0] + 40, pos_minimap[1] + 40)

    def find_position_from_minimap(self, minimap):
        """ Character is assumed to be positioned in the centre of the minimap.
                Answer given in pixel coords in the tibia maps.
        """

        minimap.save("tmp.png", "png")

        img = cv.imread(self.map, 1)
        template = cv.imread('tmp.png', 1)

        h, w, channels = template.shape[:]

        # Choice of method TM_CCOEFF is fairly arbitrary.
        res = cv.matchTemplate(img, template, eval("cv.TM_CCOEFF"))
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        """
        i = Image.open(self.map)
        i = i.crop((top_left[0], top_left[1], top_left[0] + w, top_left[1] + h))
        i.show()

        cv.rectangle(img, top_left, bottom_right, 255, 2)
        plt.subplot(121), plt.imshow(res)
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img)
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.show()
        """

        return top_left


class MiniMap():
    DIRECTION = (random.randint(-1, 1), random.randint(-1, 1))

    def get_minimap_move_pos(self, image):
        centre = MINIMAP_CENTRE

        if random.randint(1, 10) == 3:
            self.DIRECTION = (random.randint(-1, 1), random.randint(-1, 1))

        pos = (centre[0] + self.DIRECTION[0] * 5), (centre[1] + self.DIRECTION[1] * 5)
        if image.getpixel(pos) == (153, 102, 51):
            return pos

        for dist in range(10):
            for tries in range(dist):
                x = pos[0] + random.randint(0, dist)
                y = pos[1] + random.randint(0, dist)
                if image.getpixel((x, y)) == (153, 102, 51):
                    return (x, y)

        self.DIRECTION = (random.randint(-1, 1), random.randint(-1, 1))
        return centre


class MapTest(unittest.TestCase):

    def test_simple_find_pos(self):
        pos = FullMap().find_position_from_minimap(Image.open("test_map1.png"))
        self.assertEqual(pos, (868, 647))

    def test_find_path(self):
        # import cProfile
        # import re
        f = FullMap()

        # Profile.run('FullMap().find_path((650, 714), (960, 685))')
        p1 = MapPoint((650, 714), 0)
        p2 = MapPoint((650, 715), 0)

        res = FullMap().find_path(p1, p2)

    def test_get_walkable(self):
        f = FullMap()
        self.assertFalse(f.get_walkable((909, 733)))
        self.assertTrue(f.get_walkable((920, 740)))


if __name__ == "__main__":
    unittest.main()
