#! /usr/bin/env python

# Author: David Goodger <goodger@python.org>
# Copyright: (C) 1998-2006 by David J. Goodger
# License: GPL 2 (see maze.py)

import visual
import ratbot
import maze


class RatMaze:

    maze_size = 19

    def __init__(self):
        self.maze = maze.Maze(VisualGrid(self.maze_size, self.maze_size))
        self.maze.generate_dfs()
        self.maze.grid.render()
        self.rat = ratbot.RatBot()


class VisualGrid(maze.RectangleGrid):

    wall_rate = 30

    def render(self):
        self.frame = frame = visual.frame()
        color = (1., 1., .6)
        visual.box(length=self.width+.099, height=self.height+.099, width=.1,
                   pos=(0, 0, -.55), color=(.8, .8, 1.), frame=frame)
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[x][y]
                if cell.wall[2]:
                    visual.rate(self.wall_rate)
                    visual.box(length=.1, height=1.1, width=1.1,
                               pos=(x - self.width / 2.,
                                    y - (self.width - 1) / 2.,
                                    0), color=color, frame=frame)
                if cell.wall[3]:
                    visual.rate(self.wall_rate)
                    visual.box(height=.1, length=1.1, width=1.1,
                               pos=(x - (self.width - 1) / 2.,
                                    y - self.width / 2.,
                                    0), color=color, frame=frame)
        visual.box(length=self.width + .1, height=.1, width=1.1,
                   pos=(0, self.height / 2., 0), color=color, frame=frame)
        visual.box(length=.1, height=self.height + .1, width=1.1,
                   pos=(self.width / 2., 0, 0), color=color, frame=frame)


if __name__ == '__main__':
    ratmaze = RatMaze()
