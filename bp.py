from PIL import ImageGrab
from PIL import Image
from items import get_item_for_image

from pos_manual import POS_MANUAL

def get_bp_bbs():
    loot_bp = POS_MANUAL["loot_bp"]
    spacing_pixels = 6

    bp_bbs = []
    for row in range(5):
        for col in range(4):
            sideways_diff = col*40 + col*spacing_pixels
            vertical_diff = row*40 + row*spacing_pixels

            bp_bbs.append((loot_bp['x'] + sideways_diff,
                          loot_bp['y'] + vertical_diff,
                          loot_bp['x'] + sideways_diff + 40,
                          loot_bp['y'] + vertical_diff + 40))
    return bp_bbs

def get_bb_items(screen_image):
    """ Returns the 20 images of the item slot in the bp.
            Numbered as they are filled in the bp.
    """
    bp = []
    it = 1
    for screen_bb in get_bp_bbs():
        el = screen_image.crop(screen_bb)
        el = el.crop((2,2,38,38))
        bp.append(el)

        # print for debug.
        el.save("latest_bp\\" + str(it) + ".png")
        it += 1

    bp_items = []

    for bp_im in bp:
        bp_items.append(get_item_for_image(bp_im))

    return bp_items
#im = ImageGrab.grab()
#save ="foo.png"
#im.save(save, 'PNG')

if __name__ == "__main__":

    im = Image.open("images_test.png")
    bp = get_bb_items(im)

    for item in bp:
        print(item["name"], item["value"])

