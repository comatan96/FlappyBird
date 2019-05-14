import pyxel
HEIGHT = 255
WIDTH = 255
GROUND_SCROLL_SPEED = 10


class Background:
    def __init__(self):
        self.background_scroll = 0
        self.ground_scroll = 0
        self.active = True

    def draw_background(self):
        # if background is active run background, else not
        if self.active:
            offset = pyxel.frame_count % WIDTH
            for i in range(2):
                pyxel.bltm(x=i*WIDTH - offset, y=0, tm=1, u=0, v=0, w=32, h=30)
        else:
            pyxel.bltm(x=0, y=0, tm=1, u=0, v=0, w=32, h=30)

    def draw_floor(self):
        if self.active:
            offset = pyxel.frame_count % WIDTH
            for i in range(2):
                pyxel.bltm(x=i*WIDTH - offset, y=HEIGHT - 16, tm=0, u=0, v=0, w=32, h=3)
        else:
            pyxel.bltm(x=0, y=HEIGHT - 16, tm=0, u=0, v=0, w=32, h=3)
