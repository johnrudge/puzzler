#!/usr/bin/env python
# $Id$

# Author: David Goodger <goodger@python.org>
# Copyright: (C) 1998-2012 by David J. Goodger
# License: GPL 2 (see __init__.py)

"""
Concrete polystick (orders 1 through 4) puzzles.
"""

from puzzler import coordsys
from puzzler.puzzles.polysticks import Polysticks1234, OneSidedPolysticks1234


class Polysticks1234_7x7(Polysticks1234):

    """
    many solutions (very large number; over 35000 unique solutions in first
    position of X, I, & I1)
    (perfect solutions, i.e. no pieces cross).
    """

    width = 7
    height = 7

    def customize_piece_data(self):
        self.piece_data['P'][-1]['flips'] = None
        self.piece_data['P'][-1]['rotations'] = None


class Polysticks1234_3x7DiamondLattice(Polysticks1234):

    """
    many solutions
    """

    width = 10
    height = 10

    svg_rotation = -45

    def customize_piece_data(self):
        self.piece_data['P'][-1]['flips'] = None
        self.piece_data['P'][-1]['rotations'] = (0,1)

    def coordinates(self):
        return self.coordinates_diamond_lattice(7, 3)


class Polysticks1234_8x8Unbordered(Polysticks1234):

    """
    0? solutions
    """

    width = 8
    height = 8

    def coordinates(self):
        return self.coordinates_unbordered(self.width, self.height)

    def customize_piece_data(self):
        self.piece_data['P'][-1]['flips'] = None
        self.piece_data['P'][-1]['rotations'] = None


class Polysticks1234_5x5DiamondLatticeRing(Polysticks1234):

    """
    0? solutions
    """

    width = 10
    height = 10

    svg_rotation = -45

    def coordinates(self):
        hole = set(
            (coord + (3,3,0))
            for coord in self.coordinates_diamond_lattice(2, 2))
        return sorted(set(self.coordinates_diamond_lattice(5, 5)) - hole)

    def customize_piece_data(self):
        self.piece_data['P'][-1]['flips'] = None
        self.piece_data['P'][-1]['rotations'] = None