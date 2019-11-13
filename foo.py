from PIL import ImageGrab
from PIL import Image


box = ()
im = ImageGrab.grab(box)
save ="foo.png"
im.save(save, 'PNG')

