import pyxel

from random import randrange

WIDTH = 255
BIRD_GAP = 200


class Pipe:
    def __init__(self):

        # create 4 pipes in random heights inside the screen
        # the heights are tuples.
        self.pipes = [((i * 80)+400, randrange(-100, 0, 10)) for i in range(4)]
        self.active = True

    def update(self):
        if self.active:
            # keep updating pipes based on their x, y
            # for loop gets the tuples from pipes list
            # then puts in pipes the returning value from update_pipes
            # calling self.update_pipes using tuple unpack (*v)
            for i, v in enumerate(self.pipes):
                self.pipes[i] = self.update_pipes(*v)

    def update_pipes(self, x, y):
        # every frame mive pipe by one pixel
        # if out of screen, create new pipe
        # return tuple of (x, y) of the new pipe
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
