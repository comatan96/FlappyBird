import pyxel

from random import randrange

# upper pipe 24/0 -> 24/112 u,v
# upper pipe w =9 , h = rand
WIDTH = 255
BIRD_GAP = 200


class Pipe:
    def __init__(self):
        self.pipes = [((i * 80)+400, randrange(-100, 0, 10)) for i in range(4)]
        self.active = True

    def update(self):
        if self.active:
            for i, v in enumerate(self.pipes):
                self.pipes[i] = self.update_pipes(*v)

    def update_pipes(self, x, y):
        x -= 1
        if x < -80:
            x += WIDTH+80
            y_old = y
            while abs(y-y_old) < 10:
                y = randrange(-100, 0, 10)
        return (x, y)

    def draw_pipes(self):
        for x, y in self.pipes:
            pyxel.blt(x, y, 1, 0, 0, 25, 150, colkey=0)
            pyxel.blt(x, y+BIRD_GAP, 1, 0, 0, -25, -150, colkey=0)
