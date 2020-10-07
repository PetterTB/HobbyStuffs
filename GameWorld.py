""" The interface (and prolly impl) of our model of the gameworld.

Should contain subclasses that model different parts of the game world.
    (e.g. hp, position, enemies, etc)
"""

from PIL import Image
from ImageProvider import ImageProvider
from mapper import MapPoint, FullMap, Minimap
from positions import Positions


class GameWorld:

    def __init__(self):
        self._img_provider = ImageProvider()
        self.latest_input_image = self._img_provider.get_pil_image()

        self.minimap = Minimap()

    def update(self):
        self.latest_input_image = self._img_provider.get_pil_image()

        map_box = Positions.get("cam_minimap_ul") + Positions.get("cam_minimap_lr")
        self.minimap.update(self.latest_input_image.crop(map_box))
