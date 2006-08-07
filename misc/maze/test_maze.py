#! /usr/bin/env python

import unittest
import maze


class SquareCellTests(unittest.TestCase):

    def test_neighbors(self):
        self.assertEquals(maze.SquareCell(2, 5).neighbors(),
                          ((3, 5), (2, 6), (1, 5), (2, 4)))


class RectangleGridTests(unittest.TestCase):

    def test_neighbors(self):
        grid = maze.RectangleGrid(2, 5)
        self.assertEquals(grid.neighbors(grid.cells[0][0]),
                          [grid.cells[1][0], grid.cells[0][1]])
        self.assertEquals(grid.neighbors(grid.cells[0][3]),
                          [grid.cells[1][3], grid.cells[0][4],
                           grid.cells[0][2]])

    def test_cell(self):
        grid = maze.RectangleGrid(2, 5)
        self.assertEquals(grid.cell(0), grid.cells[0][0])
        self.assertEquals(grid.cell(3), grid.cells[1][1])
        self.assertEquals(grid.cell(6), grid.cells[0][3])


class TriangleCellTests(unittest.TestCase):

    def test_neighbors(self):
        self.assertEquals(maze.TriangleCell(2, 5).neighbors(),
                          ((3, 5), (1, 5), (3, 4)))
        self.assertEquals(maze.TriangleCell(3, 5).neighbors(),
                          ((4, 5), (2, 6), (2, 5)))


class LozengeGridTests(unittest.TestCase):

    def test_neighbors(self):
        grid = maze.LozengeGrid(2, 5)
        self.assertEquals(grid.neighbors(grid.cells[0][0]),
                          [grid.cell(1)])
        self.assertEquals(grid.neighbors(grid.cells[0][3]),
                          [grid.cell(7), grid.cell(5)])
        self.assertEquals(grid.neighbors(grid.cells[1][4]),
                          [grid.cell(8)])

    def test_cell(self):
        grid = maze.LozengeGrid(2, 5)
        self.assertEquals(grid.cell(0), grid.cells[0][0])
        self.assertEquals(grid.cell(3), grid.cells[1][1])
        self.assertEquals(grid.cell(6), grid.cells[0][3])


if __name__ == '__main__':
    unittest.main()
