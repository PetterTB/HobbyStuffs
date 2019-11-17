POS_MANUAL = {}

with open("pos_manual.txt") as f:
    s = f.read()
    if s:
        POS_MANUAL = eval(s)

if __name__ == "__main__":
    print("Adding element!")
    key = "loot_bp"
    d = {}
    d['x'] = 1495
    d['y'] = 54
    POS_MANUAL[key]  = d
    with open("pos_manual.txt",'w') as f:
        f.write(str(POS_MANUAL))
    print("Added: " , POS_MANUAL[key])
