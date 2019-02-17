import pyxel
import os

from collections import namedtuple
from player import Bird
from tilemap import Background
from pipe import Pipe
WIDTH  = 255
HEIGHT = 255
assets = os.path.join(os.getcwd(),os.path.dirname(__file__),'flappy.pyxel')

class App:

    def __init__(self):
        pyxel.init(width= WIDTH,height= HEIGHT, caption= "Flappy Bird", fps= 35)
        pyxel.load(assets)
        self.bird = Bird()
        self.pipe = Pipe()
        self.background = Background()
        pyxel.run(self.update, self.draw)

    def update(self):

        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
        self.pipe.update()

        self.bird.update_bird()
        print (pyxel.frame_count)

    def draw(self):
        pyxel.cls(0)
        pyxel.Image().load(0,0,"background.png")
        # TODO: Implement background!
        self.pipe.draw_pipes()
        self.background.draw_floor()
        #self.background.draw_background()
        self.bird.draw_bird()


App()