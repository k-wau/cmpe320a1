
# test file to make sure i'm not going crazy lol
# - jake

def turn( a, b, c ):

    det = (a.x-c.x) * (b.y-c.y) - (b.x-c.x) * (a.y-c.y)

    if det > 0:
        return "left"
    elif det < 0:
        return "right"
    else:
        return "neither"
    

class point:

    def __init__(self, xc, yc):
        self.x = xc
        self.y = yc

p1 = point(1, 1)
p2 = point(3, 4)
p3 = point(5, 2)

print(turn(p1, p2, p3))