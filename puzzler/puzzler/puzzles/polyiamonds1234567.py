#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $Id$

# Author: David Goodger <goodger@python.org>
# Copyright: (C) 1998-2015 by David J. Goodger
# License: GPL 2 (see __init__.py)

"""
Concrete polyiamonds (orders 1 through 7) puzzles.
"""

from puzzler.puzzles.polyiamonds import (
    Polyiamonds1234567, OneSidedPolyiamonds1234567,
    Polyiamonds12345, Hexiamonds, Heptiamonds)


class Polyiamonds1234567Hexagon1(Polyiamonds1234567):

    """many solutions"""

    height = 14
    width = 14

    holes = (set(Polyiamonds1234567.coordinates_diamond(2, (5,5,0)))
             .union(set(Polyiamonds1234567.coordinates_diamond(2, (7,5,0)))))

    def coordinates(self):
        coords = set(self.coordinates_hexagon(7)) - self.holes
        return sorted(coords)

    def customize_piece_data(self):
        self.piece_data['P5'][-1]['flips'] = None
        self.piece_data['P5'][-1]['rotations'] = (0,1,2)


class Polyiamonds1234567Hexagon2(Polyiamonds1234567Hexagon1):

    holes = (set(Polyiamonds1234567.coordinates_diamond(2, (5,7,0)))
             .union(set(Polyiamonds1234567.coordinates_diamond(2, (7,3,0)))))


class Polyiamonds1234567Hexagon3(Polyiamonds1234567Hexagon1):

    holes = (set(Polyiamonds1234567.coordinates_hexagon(2, (5,5,0)))
             - set(Polyiamonds1234567.coordinates_diamond(2, (6,5,0))))


class Polyiamonds1234567Hexagon4(Polyiamonds1234567Hexagon1):

    holes = (
        (set(Polyiamonds1234567.coordinates_elongated_hexagon(1, 2, (4,5,0)))
         - set(set(Polyiamonds1234567.coordinates_diamond(2, (4,5,0)))))
        .union(
        (set(Polyiamonds1234567.coordinates_elongated_hexagon(1, 2, (7,5,0)))
         - set(set(Polyiamonds1234567.coordinates_diamond(2, (8,5,0)))))))


class Polyiamonds1234567Hexagon5(Polyiamonds1234567Hexagon1):

    holes = (
        set(Polyiamonds1234567.coordinates_elongated_hexagon(3, 1, (5,6,0)))
        .union(set(Polyiamonds1234567.coordinates_diamond(2, (6,5,0)))))


class Polyiamonds1234567Hexagon6(Polyiamonds1234567Hexagon1):

    """
    An order-7 regular hexagon with the same 2×1 semi-regular hexagon hole as
    `Kadon's Iamond Ring`_ puzzle.

    ? solutions
    """

    holes = (
        set(Polyiamonds1234567.coordinates_elongated_hexagon(1, 2, (6,5,0))))

    svg_rotation = -90

    def coordinates(self):
        coords = set(self.coordinates_hexagon(7)) - self.holes
        self.coords12345 = (
            set(self.coordinates_hexagon(3, (3,4,0))) - self.holes)
        self.coords6 = (
            set(self.coordinates_diamond(7))
            .union(set(self.coordinates_hexagon(4, (0,3,0))))
            - self.coords12345 - self.holes)
        self.coords7 = coords - self.coords12345 - self.coords6 - self.holes
        return sorted(coords)
        # No solutions:
        #self.coords12345 = (
        #    set(self.coordinates_hexagon(3, (0,4,0))) - self.holes)
        #self.coords6 = (
        #    set(list(set(self.coordinates_elongated_hexagon(3, 5, (0,2,0))))
        #        + list(set(self.coordinates_hexagon(4, (1,3,0)))))
        #    - self.coords12345 - self.holes)
    
    def build_matrix(self):
        self.build_regular_matrix(
            sorted(Polyiamonds12345.piece_data.keys()),
            sorted(self.coords12345))
        self.build_regular_matrix(
            sorted(Hexiamonds.piece_data.keys()),
            sorted(self.coords6))
        self.build_regular_matrix(
            sorted(Heptiamonds.piece_data.keys()),
            sorted(self.coords7))


class Polyiamonds1234567IamondRing(Polyiamonds1234567Hexagon1):

    """
    `Kadon's Iamond Ring`_ puzzle: an order-7 regular hexagon with a
    2×1 semi-regular hexagon hole.

    .. _Kadon's Iamond Ring: http://gamepuzzles.com/esspoly.htm#IR

    many solutions
    """

    holes = (
        set(Polyiamonds1234567.coordinates_elongated_hexagon(1, 2, (5,5,0))))

    svg_rotation = -90

    def coordinates(self):
        self.coords12345 = (
            set(self.coordinates_diamond(4, (6,3,0)))
            .union(set(self.coordinates_hexagon(2, (5,4,0))))
            .union(set(self.coordinates_hexagon(2, (4,6,0))))
            - self.holes)
        self.coords6 = (
            set(self.coordinates_hexagon(4, (4,2,0)))
            .union(set(self.coordinates_hexagon(4, (3,4,0))))
            - self.coords12345 - self.holes)
        coords = set(self.coordinates_hexagon(7)) - self.holes
        self.coords7 = coords - self.coords12345 - self.coords6 - self.holes
        return sorted(coords)

    def build_matrix(self):
        self.build_regular_matrix(
            sorted(Polyiamonds12345.piece_data.keys()),
            sorted(self.coords12345))
        self.build_regular_matrix(
            sorted(Hexiamonds.piece_data.keys()),
            sorted(self.coords6))
        self.build_regular_matrix(
            sorted(Heptiamonds.piece_data.keys()),
            sorted(self.coords7))


class IamondRingColoringMixin(object):

    iamond_ring_colors = {
        '1': 'black',
        '2': 'gray',
        '3': 'indigo',
        '4': 'navy',
        '5': 'green',
        '6': 'maroon',
        '7': 'orangered',
        }
    
    def colorize_pieces(self):
        self.piece_colors = copy.deepcopy(self.piece_colors)
        for piece in self.piece_colors:
            self.piece_colors[piece] = self.iamond_ring_colors[piece[-1]]


class Polyiamonds1234567IamondRingColored(
        IamondRingColoringMixin, Polyiamonds1234567IamondRing):

    def customize_piece_data(self):
        self.colorize_pieces()


class Polyiamonds1234567ElongatedHexagon2x10_1(Polyiamonds1234567):

    """many solutions"""

    height = 20
    width = 12

    svg_rotation = 90

    holes = set(((5,10,1), (6,9,0)))

    def coordinates(self):
        coords = set(self.coordinates_elongated_hexagon(2, 10)) - self.holes
        return sorted(coords)

    def customize_piece_data(self):
        self.piece_data['P5'][-1]['flips'] = None
        self.piece_data['P5'][-1]['rotations'] = (0,1,2)


class Polyiamonds1234567Butterfly12x10_1(Polyiamonds1234567):

    """many solutions"""

    height = 20
    width = 22

    svg_rotation = 90

    holes = set(((10,10,1), (11,9,0)))

    def coordinates(self):
        coords = set(self.coordinates_butterfly(12, 10)) - self.holes
        return sorted(coords)

    def customize_piece_data(self):
        self.piece_data['P5'][-1]['flips'] = None
        self.piece_data['P5'][-1]['rotations'] = (0,1,2)
