""" General debugcontrol symbols for system.

Ugly hack, but yknow.."""


class Debugcontrol:
    p = {}  # p["example"] = valgfri
    position_file = "debugcontrol.txt"

    def __init__(self):
        with open(Debugcontrol.position_file) as f:
            s = f.read()
            if s:
                Debugcontrol.p = eval(s)

    @staticmethod
    def add_element(element, x, y):
        Debugcontrol.p[element] = (x, y)
        with open(Debugcontrol.position_file, 'w') as f:
            f.write(str(Debugcontrol.p))

    @staticmethod
    def get(position_key):
        try:
            return Debugcontrol.p[position_key]
        except KeyError as e:
            print("Tried to get unknown debugcontrolsymbol!" + position_key)
            raise e


Debugcontrol() # Always read from file on startup.
