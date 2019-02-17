import pyxel
from collections import namedtuple

#location of the bird
Point = namedtuple("location",['x','y'])
WIDTH    = 255
HEIGHT   = 255
GRAVITY = 1

class Bird:
    def __init__(self):
        self.location = Point(WIDTH//3, HEIGHT//2)
        self.gravity = GRAVITY
        self.velocity = 0
        self.jump     = False

    def update_bird(self):
        self.velocity = self.velocity + (GRAVITY)
        location = self.location

        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
            self.velocity = -8

        self.location = self.location._replace(y= location.y + self.velocity)

    def draw_bird(self):
        bird_x = self.location.x
        bird_y = self.location.y
        bird_v = ((pyxel.frame_count) //4) % 3 * 16
        pyxel.blt(x= bird_x, y= bird_y, img= 0, u= 0, v= bird_v, w= 17, h= 13, colkey= 0)