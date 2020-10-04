from PIL import ImageGrab
from PIL import Image


box = ()
im = ImageGrab.grab(box)
save ="foo.png"
im.save(save, 'PNG')

from mapper import FullMap

print(FullMap().find_position(im))