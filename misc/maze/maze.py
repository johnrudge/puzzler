#! /usr/bin/env python
# $Id$

# Author: David Goodger <goodger@python.org>
# Copyright: (C) 2005-2006 by David J. Goodger
# License:
#     This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License version 2
#     as published by the Free Software Foundation.
#
#     This program is distributed in the hope that it will be useful, but
#     WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#     General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program; if not, refer to
#     http://puzzler.sourceforge.net/GPL2.txt or write to the Free Software
#     Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

import random
import sys


class Maze:

    """
    Implementation of several different perfect maze generation algorithms.

        A perfect maze is defined as a maze which has one and only one path
        from any point in the maze to any other point.  This means that the
        maze has no inaccessible sections, no circular paths, no open areas.

        -- http://www.mazeworks.com/mazegen/mazetut/index.htm

    For algorithm details and discussions, see
    <http://www.mazeworks.com/mazegen/maze_faq>.
    """

    def __init__(self, grid, debug=False):
        self.grid = grid
        self.debug = debug

    def generate_dfs(self):
        """Depth-first search"""
        cell_stack = []
        total_cells = len(self.grid)
        current_cell = self.grid.cell(random.randrange(total_cells))
        visited_cells = 1
        while visited_cells < total_cells:
            neighbors = [cell for cell in self.grid.neighbors(current_cell)
                         if cell.walls() == cell.num_neighbors]
            if neighbors:
                new_cell = random.choice(neighbors)
                self.grid.remove_common_wall(current_cell, new_cell)
                cell_stack.append(current_cell)
                current_cell = new_cell
                visited_cells += 1
                if self.debug:
                    print(self.grid.dfs_representation(current_cell))
            else:
                current_cell = cell_stack.pop()

    def generate_prim(self):
        """Prim's Algorithm"""
        total_cells = len(self.grid)
        cell = self.grid.cell(random.randrange(total_cells))
        inner = set([cell])
        frontier = set(self.grid.neighbors(cell))
        outer = set()
        for i in range(total_cells):
            outer.add(self.grid.cell(i))
        outer.difference_update(inner)
        outer.difference_update(frontier)
        while frontier:
            cell = random.choice(list(frontier))
            frontier.remove(cell)
            inner.add(cell)
            neighbors = set(self.grid.neighbors(cell))
            outer_neighbors = outer.intersection(neighbors)
            outer.difference_update(outer_neighbors)
            frontier.update(outer_neighbors)
            inner_neighbors = inner.intersection(neighbors)
            neighbor = random.choice(list(inner_neighbors))
            self.grid.remove_common_wall(cell, neighbor)
            if self.debug:
                print(self.grid.set_representation(inner, frontier, outer))

    def generate_kruskal(self):
        """Kruskal's Algorithm"""
        union_find = UnionFind()
        for i in range(len(self.grid)):
            cell = self.grid.cell(i)
        walls = self.grid.walls()
        count = len(self.grid)
        while count > 1:
            index = random.randrange(len(walls))
            wall = walls.pop(index)
            if (union_find[wall[0]] != union_find[wall[1]]):
                union_find.union(wall[0], wall[1])
                count -= 1
                self.grid.remove_common_wall(wall[0], wall[1])
                if self.debug:
                    print(self.grid.equivalence_representation(union_find))


class Cell:

    def __init__(self):
        self.wall = [1] * self.num_neighbors
        self.border = [1] * self.num_neighbors
        self.solution = [0] * self.num_neighbors
        self.backtrack = [0] * self.num_neighbors

    def walls(self):
        return sum(self.wall)


class XYCoordCell(Cell):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Cell.__init__(self)

    def __repr__(self):
        return '<%s (%s, %s)>' % (self.__class__.__name__, self.x, self.y)

    def coord_string(self):
        """2-character coordinate string, for grids up to 26x10."""
        return chr(ord('a') + self.x) + str(self.y)


class SquareCell(XYCoordCell):

    """
    5 x 5 grid (2 lines per row; room for 2 characters per cell)::

        +--+--+--+--+--+
        |a4|b4|c4|e4 e4|
        +--+--+--+--+--+
        |a3|b3|c3|d3|e3|
        +--+--+--+--+--+
        |a2|b2|c2|d2|e2|
        +--+--+--+--+--+
        |a1|b1|c1|d1|e1|
        +--+--+--+--+--+
        |a0|b0|c0|d0|e0|
        +--+--+--+--+--+
    """

    num_neighbors = 4

    def neighbors(self):
        # counterclockwise from right
        return ((self.x + 1, self.y),       # right
                (self.x,     self.y + 1),   # above
                (self.x - 1, self.y),       # left
                (self.x,     self.y - 1))   # below


class TriangleCell(XYCoordCell):

    """
    16 x 4 grid (3 lines per row; room for 2 characters per cell)::

                     ________________________________________________
                    /\    /\    /\    /\    /\    /\    /\    /\    /
                   /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /
                  /____\/____\/____\/____\/____\/____\/____\/____\/
                 /\    /\    /\    /\    /\    /\    /\    /\    /
                /  \  /  \  /  \  /  \  /  \  /  \  /  \  /  \  /
               /____\/____\/____\/____\/____\/____\/____\/____\/
              /\    /\    /\    /\    /\    /\    /\    /\    /
             /a1\b1/c1\d1/  \  /  \  /  \  /  \  /  \  /  \  /
            /____\/____\/____\/____\/____\/____\/____\/____\/
           /\    /\    /\    /\    /\    /\    /\    /\    /
          /a0\b0/c0\d0/  \  /  \  /  \  /  \  /  \  /  \  /
         /____\/____\/____\/____\/____\/____\/____\/____\/
    """

    num_neighbors = 3

    def neighbors(self):
        # counterclockwise from right
        if self.x % 2:                        # odd ==> down-pointing triangle
            return ((self.x + 1, self.y),     # right
                    (self.x - 1, self.y + 1), # above
                    (self.x - 1, self.y))     # left

        else:                                 # even ==> up-pointing triangle
            return ((self.x + 1, self.y),     # right
                    (self.x - 1, self.y),     # left
                    (self.x + 1, self.y - 1)) # below


class HexagonCell(XYCoordCell):

    """
    5 x 5 grid (2 lines per row, skewed; room for 2 characters per cell)::
                       __
                    __/e4\
                 __/  \__/
              __/  \__/  \
           __/  \__/  \__/
          /a4\__/  \__/  \
          \__/  \__/  \__/
          /a3\__/  \__/  \
          \__/b2\__/  \__/
          /a2\__/c1\__/e0\
          \__/b1\__/d0\__/
          /a1\__/c0\__/
          \__/b0\__/
          /a0\__/
          \__/
    """

    num_neighbors = 6

    def neighbors(self):
        # counterclockwise from above-right
        return ((self.x + 1, self.y),     # above-right
                (self.x,     self.y + 1), # above
                (self.x - 1, self.y + 1), # above-left
                (self.x - 1, self.y),     # below-left
                (self.x,     self.y - 1), # below
                (self.x + 1, self.y - 1)) # below-right


class Grid:

    def __init__(self, cells):
        self.cells = cells


class XYCoordinateGrid(Grid):

    def __init__(self, width, height):
        self.width = width
        self.height = height
        Grid.__init__(self, [[self.cell_class(x, y) for y in range(height)]
                             for x in range(width)])

    def __len__(self):
        return self.width * self.height

    def in_grid(self, x, y):
        return (0 <= x < self.width) and (0 <= y < self.height)

    def neighbors(self, cell):
        coords = self.cells[cell.x][cell.y].neighbors()
        return [self.cells[i][j] for (i, j) in coords if self.in_grid(i, j)]

    def cell(self, index):
        if index < 0 or index >= len(self):
            raise IndexError('grid index out of range')
        x = index % self.width
        y = index // self.width
        return self.cells[x][y]

    def __str__(self):
        return self.string_representation()

    def equivalence_representation(self, union_find):
        def coord_string(cell):
            return union_find[cell].coord_string()
        return self.string_representation(coord_string)

    def set_representation(self, inner, frontier, outer):
        def set_indicator(cell):
            if cell in inner:
                return '. '
            elif cell in frontier:
                return '**'
            elif cell in outer:
                return '  '
            else:
                raise Exception('cell %s not in any set!' % cell)
        return self.string_representation(set_indicator)

    def dfs_representation(self, current_cell):
        def current(cell):
            if cell == current_cell:
                return '**'
            else:
                return '  '
        return self.string_representation(current)


def empty_content(cell):
    return '  '


class RectangleGrid(XYCoordinateGrid):

    cell_class = SquareCell

    def walls(self):
        walls = []
        for y in range(self.height):
            for x in range(self.width):
                if x < self.width - 1:
                    walls.append((self.cells[x][y], self.cells[x+1][y]))
                if y < self.height - 1:
                    walls.append((self.cells[x][y], self.cells[x][y+1]))
        return walls

    wall_lookup = {
        # diff  : (wall of cell1, wall of cell2)
        ( 1,  0): (0, 2),    
        ( 0,  1): (1, 3),    
        (-1,  0): (2, 0),    
        ( 0, -1): (3, 1)}

    def remove_common_wall(self, cell1, cell2):
        diff = (cell2.x - cell1.x, cell2.y - cell1.y)
        wall1, wall2 = self.wall_lookup[diff]
        cell2.wall[wall2] = cell1.wall[wall1] = 0

    def string_representation(self, content=empty_content):
        output = []
        for y in range(self.height - 1, -1, -1):
            line1 = []
            line2 = []
            for x in range(self.width):
                cell = self.cells[x][y]
                line1.append(' -'[cell.wall[1]] * 2)
                line2.append(' |'[cell.wall[2]] + content(cell))
            output.append('+' + '+'.join(line1) + '+\n')
            output.append(''.join(line2) + '|\n')
        output.append('+--' * self.width + '+\n')
        return ''.join(output)


class LozengeGrid(XYCoordinateGrid):

    cell_class = TriangleCell

    def __init__(self, width, height):
        if width % 2:
            raise ValueError('LozengeGrid objects must have even width')
        XYCoordinateGrid.__init__(self, width, height)

    def walls(self):
        walls = []
        for y in range(self.height):
            for x in range(self.width):
                if x < self.width - 1:
                    walls.append((self.cells[x][y], self.cells[x+1][y]))
                if y < self.height - 1 and (x % 2):
                    walls.append((self.cells[x][y], self.cells[x-1][y+1]))
        return walls

    wall_lookup = {
        # diff  : (wall of cell1, wall of cell2)
        (-1,  0): (2, 0),    
        ( 1,  0): (0, 1),    
        (-1,  1): (1, 2)}

    def remove_common_wall(self, cell1, cell2):
        """
        Coordinates & walls::

                        ____________          ____________
            line1 ...../\    /\    /         /\    1     /
            line2 ..../a1\b1/c1\d1/         /  \  odd   /
            line3 .../____\/____\/         /    \2    0/
            line1 ../\    /\    /         /1    0\    /
            line2 ./a0\b0/c0\d0/         /  even  \  /
            line3 /____\/____\/         /____2_____\/

        ==================  =====  =====
        difference          wall
        ------------------  ------------
        cell2 - cell1       cell2  cell1
        ==================  =====  =====
        odd
        b0 - c0 = (-1,  0)  0      1
        b0 - a1 = ( 1, -1)  1      2
        b0 - a0 = ( 1,  0)  2      0

        even
        c1 - d1 = (-1,  0)  0      2
        c1 - b1 = ( 1,  0)  1      0
        c1 - d0 = (-1,  1)  2      1
        ==================  =====  =====
        """
        if cell2.x % 2:
            # only deal with one case: cell2 with even x
            cell1, cell2 = cell2, cell1
        diff = (cell2.x - cell1.x, cell2.y - cell1.y)
        wall1, wall2 = self.wall_lookup[diff]
        cell2.wall[wall2] = cell1.wall[wall1] = 0

    def string_representation(self, content=empty_content):
        output = ['   ' * self.height + '___' * self.width + '\n']
        for y in range(self.height - 1, -1, -1):
            padding = ' ' * 3 * y
            line1 = ['  ' + padding]
            line2 = [' ' + padding]
            line3 = [padding]
            for x in range(0, self.width, 2):
                cell = self.cells[x][y]
                border = ' /'[cell.wall[1]]
                bottom = ' _'[cell.wall[2]]
                line1.append(border)
                line2.append(border + content(cell))
                line3.append((bottom, border)[border != ' '] + bottom * 4)
                cell = self.cells[x+1][y]
                border = ' \\'[cell.wall[2]]
                line1.append(border + '    ')
                line2.append(border + content(cell))
                line3.append((bottom, border)[border != ' '])
            output.append(''.join(line1) + '/\n')
            output.append(''.join(line2) + '/\n')
            output.append(''.join(line3) + '/\n')
        return ''.join(output)


class HoneycombGrid(XYCoordinateGrid):

    cell_class = HexagonCell

    def walls(self):
        walls = []
        for y in range(self.height - 1):
            for x in range(self.width):
                if x > 0:
                    walls.append((self.cells[x][y], self.cells[x-1][y+1]))
                walls.append((self.cells[x][y], self.cells[x][y+1]))
                if x < self.width - 1:
                    walls.append((self.cells[x][y], self.cells[x+1][y]))
        return walls

    wall_lookup = {
        # diff  : (wall of cell1, wall of cell2)
        (-1,  0): (3, 0),    
        ( 0, -1): (4, 1),    
        ( 1, -1): (5, 2),    
        ( 1,  0): (0, 3),    
        ( 0,  1): (1, 4),    
        (-1,  1): (2, 5)}

    def remove_common_wall(self, cell1, cell2):
        """
        Coordinates & walls::

          .............__
          ..........__/e4\
          .......__/  \__/         _______
          ....__/  \__/  \        /   1   \
          .__/  \__/  \__/       /2       0\
          /a4\__/  \__/  \      /   wall    \
          \__/  \__/  \__/      \   index   /
          /a3\__/  \__/  \       \3       5/
          \__/b2\__/  \__/        \___4___/
          /a2\__/c1\__/e0\
          \__/b1\__/d0\__/
          /a1\__/c0\__/
          \__/b0\__/
          /a0\__/
          \__/

        ==================  =====  =====
        difference          wall
        ------------------  ------------
        cell2 - cell1       cell2  cell1
        ==================  =====  =====
        b1 - c1 = (-1,  0)  0      3
        b1 - b2 = ( 0, -1)  1      4
        b1 - a2 = ( 1, -1)  2      5
        b1 - a1 = ( 1,  0)  3      0
        b1 - b0 = ( 0,  1)  4      1
        b1 - c0 = (-1,  1)  5      2
        ==================  =====  =====
        """
        diff = (cell2.x - cell1.x, cell2.y - cell1.y)
        wall1, wall2 = self.wall_lookup[diff]
        cell2.wall[wall2] = cell1.wall[wall1] = 0

    def string_representation(self, content=empty_content):
        output = []
        for x in range(self.width - 1, -1, -1):
            output.append([' ' * (x * 3 + 1)]) # padding for slanted top row
        for y in range(self.height - 1, -1, -1):
            output.append([])
            output.append(['\\'])       # left edge; always there
            for x in range(self.width):
                cell = self.cells[x][y]
                output[-2 - x].append(' /'[cell.wall[2]] + content(cell) +
                                  ' \\'[cell.wall[0]])
                output[-3 - x].append(' _'[cell.wall[1]] * 2)
            if y < self.height - 1:
                output[-self.width - 2].append('/')
        for x in range(self.width, 0, -1):
            output[-x].append('__/')
        for i in range(len(output)):
            output[i] = ''.join(output[i]) + '\n'
        return ''.join(output)


class UnionFind:

    """
    Implementation of the Union-Find algorithm -- a fast implementation of
    equivalence classes.  Union-Find provides the ability to determine which
    equivalence class a given object belongs to (via subscripting), and the
    ability to join two or more equivalance classes into a single class (via
    the 'union' method).

    Code by `Josiah Carlson`__, as modified by `David Eppstein`__ (allowed
    arbitrarily many arguments in unions, allowed subscript syntax for finds,
    and eliminated unnecessary code).

    __ http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/215912
    __ http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/221251
    """

    def __init__(self):
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """
        Find the root of the set that an object is in.  Object must be
        hashable; previously unknown objects become new singleton sets.
        """
        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object
        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]
        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, *objects):
        """Find the sets containing the given objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


if __name__ == '__main__':
    debug = False
#     debug = True
#     width = 6 ; height = 6
    width = 25 ; height = 10
    maze1 = Maze(RectangleGrid(width, height), debug=debug)
    maze1.generate_dfs()
    print(str(maze1.grid))
#     maze2 = Maze(RectangleGrid(width, height), debug=debug)
#     maze2.generate_prim()
#     print str(maze2.grid)
#     maze3 = Maze(RectangleGrid(width, height), debug=debug)
#     maze3.generate_kruskal()
#     print str(maze3.grid)

    debug = False
#     debug = True
#     width = 6 ; height = 6
    width = 18 ; height = 6
    maze4 = Maze(LozengeGrid(width, height), debug=debug)
    maze4.generate_dfs()
    print(str(maze4.grid))
#     maze5 = Maze(LozengeGrid(width, height), debug=debug)
#     maze5.generate_prim()
#     print str(maze5.grid)
#     maze6 = Maze(LozengeGrid(width, height), debug=debug)
#     maze6.generate_kruskal()
#     print str(maze6.grid)

    debug = False
#     debug = True
#     width = 6 ; height = 6
    width = 18 ; height = 10
    maze7 = Maze(HoneycombGrid(width, height), debug=debug)
    maze7.generate_dfs()
    print(str(maze7.grid))
#     maze8 = Maze(HoneycombGrid(width, height), debug=debug)
#     maze8.generate_prim()
#     print str(maze8.grid)
#     maze9 = Maze(HoneycombGrid(width, height), debug=debug)
#     maze9.generate_kruskal()
#     print str(maze9.grid)
