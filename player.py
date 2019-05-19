import pyxel
from collections import namedtuple

# location of the bird
Point = namedtuple("location", ['x', 'y'])
WIDTH = 255
HEIGHT = 255
GRAVITY = 1


class Bird:
    def __init__(self):
        self.location = Point(WIDTH//3, HEIGHT//2)
        self._gravity = GRAVITY
        self._velocity = 0
        self.hit = False

    def update_bird(self):
        location = self.location

        # change velocity according to gravity in order to make the fast fall
        self._velocity = self._velocity + (self._gravity)

        # change y location of the bird based on velocity
        self.location = self.location._replace(y=location.y + self._velocity)

        # if jumped - update velocity
        if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP))and not self.hit:
            self._velocity = -8

    def draw_bird(self):
        if self.location.y < HEIGHT - 20:

            # save locations
            bird_x = self.location.x
            bird_y = self.location.y

            # in order to animate, change v according to frames
            bird_v = ((pyxel.frame_count) // 4) % 3 * 16
            pyxel.blt(x=bird_x, y=bird_y, img=0, u=0,
                      v=bird_v, w=17, h=13, colkey=0)
        else:
            pyxel.blt(x=self.location.x, y=HEIGHT-27,
                      img=0, u=0, v=0, w=17, h=13, colkey=0)
