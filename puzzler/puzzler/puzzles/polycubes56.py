#!/usr/bin/env python
# $Id$

# Author: David Goodger <goodger@python.org>
# Copyright: (C) 1998-2018 by David J. Goodger
# License: GPL 2 (see __init__.py)

"""
Concrete polycube puzzles, orders 5 & 6: pentacubes & hexacubes.
"""

from puzzler.puzzles import Puzzle3D, Puzzle2D
from puzzler.puzzles.polycubes import Polycubes56


class Polycubes56Crystal1(Polycubes56):

    """
    ? solutions

    An order-18 tetrahedral pyramid (plus one unit cube), consisting of 1141
    unit cubes.

    Based on the "`Mega-Pyramid`__" puzzle designed by Andy Niedermaier.

    __ http://gamepuzzles.com/megapyramid.htm
    """

    size = 18
    width = height = depth = size
    extra = (6,6,6)

    def coordinates(self):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    total = x + y + z
                    if total < self.size or (x,y,z) == self.extra:
                        yield (x, y, z)

"""
C:\Users\goodgd1\projects\puzzler\puzzler>c:\Python27\python.exe bin\cubes\polycubes-56-crystal-1.py -n10 -N -s docs\images\cubes\polycubes-56-crystal-1.svg -x docs\images\cubes\polycubes-56-crystal-1.x3d > ..\solutions\cubes\polycubes-56-crystal-1.txt
Traceback (most recent call last):
  File "bin\cubes\polycubes-56-crystal-1.py", line 9, in <module>
    puzzler.run(puzzle)
  File "C:\Users\goodgd1\projects\puzzler\puzzler\puzzler\__init__.py", line 91, in run
    return solve(puzzle_class, output_stream, settings)
  File "C:\Users\goodgd1\projects\puzzler\puzzler\puzzler\__init__.py", line 246, in solve
    puzzle.write_x3d(settings.x3d, solution)
  File "C:\Users\goodgd1\projects\puzzler\puzzler\puzzler\puzzles\__init__.py", line 363, in write_x3d
    x3d = self.format_x3d(solution, s_matrix)
  File "C:\Users\goodgd1\projects\puzzler\puzzler\puzzler\puzzles\__init__.py", line 1004, in format_x3d
    'color': colors.x3d[self.piece_colors[name]]})
KeyError: 'Lj6'
"""
