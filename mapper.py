from PIL import Image

import unittest
import math
# Used for position finding.
import cv2 as cv
# from matplotlib import pyplot as plt for disabled debug printing.

MINIMAP_CENTRE = (1778, 103)


class MapPoint:
    """ Represents a point on the tibia map.

        position p is given in pixel coords of the tibian map files.
    """

    def __init__(self, point, floor=0):
        self.p = point
        self.x = point[0]
        self.y = point[1]
        self.floor = floor

    def __eq__(self, other):
        return self.p == other.p and self.floor == other.floor

    def __hash__(self):
        return self.floor * 1000 + self.y * 100 + self.x


class FullMap:
    """ Class handling the use of the known minimaps of the game.

    Levels go from -8 to +7.

    All points on map are assumed to be of type "MapPoint".
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
        """Find path from start to dest. Returns list of MapPoints, or None.
                Only supports same level paths.
                todo: fix level changes.
                todo: cleanup code (extract into separate class?)

        start and dest assumed to be MapPoints.
        """

        open_set = [start]

        costs = {start: 0}
        came_from = {}

        while open_set:
            open_set.sort(key=lambda x: costs[x])
            node = open_set.pop(0)

            # Found the path!
            if node == dest:
                path = []
                path_node = dest
                while path_node in came_from.keys():
                    path.append(path_node)
                    path_node = came_from[path_node]
                return path

            for next_node, step_cost in self.get_neighbors_and_cost(node):
                if self.get_walkable(next_node.p):
                    cost = step_cost + costs[node] + self.euclide_dist(next_node.p, dest.p)
                    if cost < self.get_cost(costs, next_node):
                        if next_node not in open_set:
                            open_set.append(next_node)
                        came_from[next_node] = node
                        costs[next_node] = cost
        return None

    def get_neighbors_and_cost(self, point):
        """ point is assumed to be a MapPoint.
        """

        res = []

        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0),
                     (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for n in neighbors:
            step_cost = 4
            if n in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                step_cost = 1

            p = MapPoint(((point.x + n[0]), (point.y + n[1])), point.floor)
            res.append((p, step_cost))
        return res

    def get_cost(self, costs, node):
        if node not in costs.keys():
            return 100000000
        return costs[node]

    def euclide_dist(self, p1, p2):
        x = p2[0] - p1[0]
        y = p2[1] - p1[1]
        return math.sqrt(x * x + y * y)

    def get_walkable(self, node):

        pixel = self.map_path_img.getpixel(node)

        yellow = (255, 255, 0)
        white = (250, 250, 250)

        if pixel == yellow or pixel == white:
            return False
        else:
            return True

    def find_position(self, image):
        """ Uses minimap image to find char position.
                Minimap is assumed to be at second largest magnification.
                returns position of centre of minimap (character).
        """
        mmap = image.crop((MINIMAP_CENTRE[0] - 50, MINIMAP_CENTRE[1] - 50,
                           MINIMAP_CENTRE[0] + 50, MINIMAP_CENTRE[1] + 50))

        # todo: make this relative. Use less of the minimap?
        mmap = mmap.resize((80, 80), Image.ANTIALIAS)

        pos_minimap = self.find_position_from_minimap(mmap)

        return pos_minimap[0] + 40, pos_minimap[1] + 40

    def find_position_from_minimap(self, minimap):
        minimap.save("tmp.png", "png")

        img = cv.imread(self.map, 1)
        template = cv.imread('tmp.png', 1)

        h, w, channels = template.shape[:]

        res = cv.matchTemplate(img, template, eval("cv.TM_CCOEFF"))  # TM_CCOEFF chosen by simple testing.
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        """ Old debugging outputs.
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


class MapTest(unittest.TestCase):

    def test_simple_find_pos(self):
        pos = FullMap().find_position_from_minimap(Image.open("mapper_test1.png"))
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
