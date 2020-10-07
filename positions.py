""" Code for screen positions.

Both for positions in webcam-coords, and screen-coords"""


class Positions:
    p = {}  # p["example"] = (0,1)
    position_file = "positions.txt"

    def __init__(self):
        self.refresh()

    @staticmethod
    def refresh():
        with open(Positions.position_file) as f:
            s = f.read()
            if s:
                Positions.p = eval(s)

    @staticmethod
    def add_element(element, x, y):
        Positions.p[element] = (x, y)
        with open(Positions.position_file, 'w') as f:
            f.write(str(Positions.p))

    @staticmethod
    def get(position_key):
        try:
            return Positions.p[position_key]
        except KeyError as e:
            print("Tried to get key : " + position_key + " from " + str(Positions.p))
            raise e


Positions.refresh() # Always read from file on startup.

if __name__ == '__main__':
    print("Positions!: " + str(Positions().p))
    print("Adding value! input key, x, y")
    key = input()
    x = int(input())
    y = int(input())

    Positions.add_element(key, x, y)
    print("After addition: " + str(Positions().p))