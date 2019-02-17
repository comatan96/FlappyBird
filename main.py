import pyxel
import os

from collections import namedtuple
from player import Bird
from tilemap import Background
from pipe import Pipe
WIDTH    = 255
HEIGHT   = 255
BIRD_GAP = 200
RESTART  = "PRESS R TO RESTART GAME "
SCORE    = "YOUR SCORE IS: "
INS      = "PRESS SPACE OR ARROW UP TO FLAP THE BIRD"
assets   = os.path.join(os.getcwd(),os.path.dirname(__file__),'flappy.pyxel')

class App:

    def __init__(self):
        pyxel.init(width= WIDTH,height= HEIGHT, caption= "Flappy Bird", fps= 35)
        pyxel.load(assets)
        self.reset()
        pyxel.run(self.update, self.draw)

    def reset(self):
        self.activate_game = False
        self.bird = Bird()
        self.pipe = Pipe()
        self.score_count = 0
        self.background = Background()

    def update(self):
        if self.activate_game:
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

            if pyxel.btnp(pyxel.KEY_R):
                self.reset()

            self.hit()
            self.pipe.update()
            self.bird.update_bird()
            print (f"bird hit: {self.bird.hit}")
            print (f"bird y: {self.bird.location.y}")
            #print (self.pipe.pipes[])
        if not self.activate_game:
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_UP):
                self.bird.update_bird()
                self.activate_game = True


    def display_score(self):
        for i in range(4):
            if self.bird.location.x == self.pipe.pipes[i][0]:
                self.score_count += 1
        pyxel.text(WIDTH//2, HEIGHT//3, str(self.score_count),7)

    def hit(self):
        for i in range(4):
            print (f"down pip y: {self.pipe.pipes[i][1]+ BIRD_GAP}")
            print (f"up pipe y:  {self.pipe.pipes[i][1]+ 80}")
            if  self.pipe.pipes[i][0]+12.5 > self.bird.location.x > self.pipe.pipes[i][0]-12.5:
                if (
                    self.bird.location.y > self.pipe.pipes[i][1] + BIRD_GAP
                    or self.bird.location.y < self.pipe.pipes[i][1] + 140
                    ):
                    self.bird.hit          = True
                    self.pipe.active       = False
                    self.background.active = False
        if self.bird.location.y > HEIGHT - 36:
            self.bird.hit          = True
            self.pipe.active       = False
            self.background.active = False

    def draw(self):
        pyxel.cls(0)

        if not self.activate_game:
            pyxel.text(WIDTH/2 - len((INS)*2), HEIGHT//3, INS, 7)

        self.pipe.draw_pipes()
        self.background.draw_floor()
        # TODO: Implement background!
        #self.background.draw_background()
        self.bird.draw_bird()
        self.display_score()

        if self.bird.hit == True:
            pyxel.text(WIDTH/2 - (len(SCORE)*2), HEIGHT//3, SCORE + str(self.score_count), 7)
            pyxel.text(WIDTH/2 - (len(RESTART)*2), HEIGHT//2, RESTART, 7)

App()