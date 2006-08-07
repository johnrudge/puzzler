import visual


class RatBot:

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    zaxis = visual.vector(0, 0, 1)
    framerate = 32
    moverate = 4
    frames_per_move = framerate / moverate

    def __init__(self):
        self.x = 0
        self.y = 0
        self.d_index = 0
        self.direction = self.directions[self.d_index]
        self.setup_body()

    def setup_body(self):
        frame = visual.frame()
        self.parts = Bunch()
        self.parts.body = visual.cone(
            color=visual.color.white, length=.8, radius=.2,
            pos=(-.4, 0, 0), frame=frame)
        self.parts.l_ear = visual.cone(
            color=visual.color.white, length=.1, radius=.02,
            pos=(.05, .04, .06), axis=self.zaxis, frame=frame)
        self.parts.r_ear = visual.cone(
            color=visual.color.white, length=.1, radius=.02,
            pos=(.05, -.04, .06), axis=self.zaxis, frame=frame)
        self.parts.l_eye = visual.sphere(
            color=visual.color.red, radius=.03,
            pos=(.1, .04, .06), frame=frame)
        self.parts.r_eye = visual.sphere(
            color=visual.color.red, radius=.03,
            pos=(.1, -.04, .06), frame=frame)
        self.rat = frame

    def advance(self):
        self.x = self.x + self.direction[0]
        self.y = self.y + self.direction[1]
        dx = 1.0 * self.direction[0] / self.frames_per_move
        dy = 1.0 * self.direction[1] / self.frames_per_move
        for i in range(self.frames_per_move):
            visual.rate(self.framerate)
            self.rat.x = self.rat.x + dx
            self.rat.y = self.rat.y + dy

    def turn(self, lr):
        if lr == 'left':
            sign = +1
        else:
            sign = -1
        self.d_index = (self.d_index + sign) % len(self.directions)
        self.direction = self.directions[self.d_index]
        da = sign * visual.pi / 2 / self.frames_per_move
        for i in range(self.frames_per_move):
            visual.rate(self.framerate)
            self.rat.rotate(angle=da, axis=self.zaxis, origin=self.rat.pos)

    def turn_left(self):
        self.turn('left')

    def turn_right(self):
        self.turn('right')

    def visible(self, visible):
        for obj in self.rat.objects:
            obj.visible = visible


class Bunch(dict):

    """A dictionary with dotted-attribute access (i.e. ``b['a'] is b.a``)."""

    def __init__(self, **keyword_args):
        dict.__init__(self, keyword_args)
        self.__dict__ = self
