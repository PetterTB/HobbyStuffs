POS_MANUAL = {}

with open("pos_manual.txt") as f:
    s = f.read()
    if s:
        POS_MANUAL = eval(s)