#!/usr/bin/env python3

import puzzler.coordsys
from puzzler.puzzles.polyominoes import Pentominoes


class MyPuzzle(Pentominoes):

    height = 3
    width = 21

    check_for_duplicates = True

    duplicate_conditions = ({'x_reversed': True},
                            {'y_reversed': True},
                            {'x_reversed': True, 'y_reversed': True})

    def coordinates(self):
        holes = {(4,1), (10,1), (16,1)}
        for y in range(self.height):
            for x in range(self.width):
                if (x,y) not in holes:
                    yield puzzler.coordsys.Cartesian2D((x, y))


if __name__ == '__main__':
    puzzler.run(MyPuzzle)
