import pyxel
HEIGHT = 255
WIDTH  = 255
GROUND_SCROLL_SPEED = 10
class Background:
    def __init__(self):
        self.background_scroll = 0
        self.ground_scroll     = 0
        self.active            = True

    def draw_background(self):
        #pyxel.bltm(x=i*WIDTH-offset,y=20,tm= 1,u=0,v=0,w=32,h=16)
        pass
    
    def draw_floor(self):
        if self.active:
            offset = pyxel.frame_count % WIDTH
            for i in range(2):
                pyxel.bltm(i*WIDTH - offset,HEIGHT - 16,0,0,0,32,3)
        else:
            pyxel.bltm(0,HEIGHT - 16,0,0,0,32,3)
