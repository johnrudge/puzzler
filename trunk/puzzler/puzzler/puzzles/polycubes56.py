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
