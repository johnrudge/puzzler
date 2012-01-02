#!/usr/bin/env python
# -*- coding: utf-8 -*-
# $Id$

# Author: David Goodger <goodger@python.org>
# Copyright: (C) 1998-2011 by David J. Goodger
# License: GPL 2 (see __init__.py)

import sys
import copy
import datetime
import re
from pprint import pprint, pformat

from puzzler import coordsys
from puzzler import colors


class DataError(RuntimeError): pass


class Puzzle(object):

    """
    Abstract base class for puzzles.
    """

    height = 0
    width = 0
    depth = 0

    check_for_duplicates = False

    duplicate_conditions = ()
    """A list of dictionaries of default-value keyword arguments to
    `format_solution`, to generate all solution permutations."""

    secondary_columns = 0

    empty_cell = ' '

    margin = 1

    piece_data = {}
    """Mapping of piece names to 2-tuples (a copy.deepcopy is made first):

    * list of unit coordinates (usually one unit, the origin, is implicit)
    * dictionary of aspect restrictions, keyword arguments to `make_aspects`;
      customized in `customize_piece_data`
    """

    piece_colors = None
    """Mapping of piece names to colors.  The '0' name is reserved for
    formatting solution coordinates."""

    svg_header = '''\
<?xml version="1.0" standalone="no"?>
<!-- Created by Polyform Puzzler (http://puzzler.sourceforge.net/) -->
<svg width="%(width)s" height="%(height)s" viewBox="0 0 %(width)s %(height)s"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink">
'''
    svg_footer = '</svg>\n'
    svg_g_start = '<g>\n'
    svg_g_end = '</g>\n'

    svg_polygon = '''\
<polygon fill="%(color)s" stroke="%(stroke)s" stroke-width="%(stroke_width)s"
         points="%(points)s">
<desc>%(name)s</desc>
</polygon>
'''

    svg_stroke = 'white'
    """Polygon outline color."""

    svg_stroke_width = '1'
    """Width of polygon outline."""

    svg_unit_length = 10
    """Unit side length in pixels."""

    svg_unit_width = svg_unit_length
    """Unit width in pixels."""

    svg_unit_height = svg_unit_length
    """Unit height in pixels."""

    x3d_header = '''\
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE X3D PUBLIC "ISO//Web3D//DTD X3D 3.0//EN"
 "http://www.web3d.org/specifications/x3d-3.0.dtd">
<X3D profile="Immersive" version="2.0">
<Scene>
'''

    x3d_footer = '</Scene>\n</X3D>\n'

    @classmethod
    def components(cls):
        """Return a tuple of puzzle component classes (sub-puzzles)."""
        return (cls,)

    def __init__(self, init_puzzle=True):
        """
        Use `init_puzzle` to speed up initialization when not actually solving
        the puzzle.
        """

        self.solutions = set()
        """Set of all permutations of solutions, for duplicate checking."""

        self.solution_coords = set(self.coordinates())
        """A set of all coordinates that make up the solution area/space."""

        self.aspects = {}
        """Mapping of piece name to a set of aspects (pieces in all
        orientations)."""

        self.pieces = {}
        """Mapping of piece name to a sorted list of 2-tuples: sorted
        coordinates & aspect objects.  Ensures reproducible results."""

        self.x_width = len(str(self.width - 1))
        """Maximum width of string representation of X coordinate."""

        self.y_width = len(str(self.height - 1))
        """Maximum width of string representation of Y coordinate."""

        self.z_width = len(str(self.depth - 1))
        """Maximum width of string representation of Z coordinate."""

        self.matrix = []
        """A list of lists; see the ExactCover.load_matrix() method of
        puzzler.exact_cover_dlx or puzzler.exact_cover_x2."""

        self.matrix_columns = {}
        """Mapping of `self.matrix` column names to indices."""

        # Make an object-local deep copy of the dict:
        self.piece_data = copy.deepcopy(self.piece_data)
        # Now we can modify it as we like:
        self.customize_piece_data()

        if init_puzzle:
            self.init_puzzle()

    def init_puzzle(self):
        """Initialize the puzzle pieces and matrix."""
        for name, (data, kwargs) in self.piece_data.items():
            self.aspects[name] = self.make_aspects(data, **kwargs)
        for name, aspects in self.aspects.items():
            self.pieces[name] = tuple(sorted((tuple(sorted(aspect)), aspect)
                                             for aspect in aspects))
        self.build_matrix_header()
        self.build_matrix()

    def coordinates(self):
        """
        A generator that yields all the coordinates of the solution space.

        Implement in subclasses.
        """
        raise NotImplementedError

    def customize_piece_data(self):
        """
        Make instance-specific customizations to copies of `self.piece_data`
        and `self.piece_colors`.

        Override in subclasses.
        """
        pass

    def make_aspects(self, data, **kwargs):
        """
        Return a set of aspects (rotations & flips) of a puzzle piece
        described by `data`.  Puzzle-specific parameters control the range of
        aspect orientations.

        Implement in subclasses.
        """
        raise NotImplementedError

    def build_matrix_header(self):
        """
        Create and populate the first row of `self.matrix`, a list of column
        names.

        Implement in subclasses.
        """
        raise NotImplementedError

    def build_matrix(self):
        """
        Create and populate the data rows of `self.matrix`, lists of 0's and
        1's (or other true values).
        """
        self.build_regular_matrix(sorted(self.pieces.keys()))

    def build_regular_matrix(self, keys):
        """
        Build `self.matrix` rows from puzzle pieces listed in `keys`.

        Implement in subclasses.
        """
        raise NotImplementedError

    def record_solution(self, solution, solver, stream=sys.stdout, dated=False):
        """
        Output a formatted solution to `stream`.
        """
        formatted = self.format_solution(solution, normalized=True)
        if self.check_for_duplicates:
            if self.store_solutions(solution, formatted):
                return
        if dated:
            print >>stream, 'at %s,' % datetime.datetime.now(),
        print >>stream, solver.format_solution()
        print >>stream
        print >>stream, self.format_solution(solution, normalized=False)
        print >>stream
        stream.flush()

    def record_dated_solution(self, solution, solver, stream=sys.stdout):
        """A dated variant of `self.record_solution`."""
        self.record_solution(solution, solver, stream=stream, dated=True)

    def format_solution(self, solution, normalized=True):
        """
        Return a puzzle-specific formatting of a solution.

        Implement in subclasses.

        * `solution` is a list of pieces.  Each piece is a list of column
          names from the exact cover matrix: cooridinates and the piece name.

        * `normalized` is a flag; if set, the solution is formatted in a way
          that allows for easy duplicate detection (such as renaming identical
          pieces).
        """
        raise NotImplementedError

    def format_svg(self, solution=None, s_matrix=None):
        """
        Return a puzzle-specific SVG formatting of a solution.

        Implement in subclasses.
        """
        raise NotImplementedError

    def write_svg(self, output_path, solution=None, s_matrix=None):
        try:
            svg = self.format_svg(solution, s_matrix)
        except NotImplementedError:
            print >>sys.stderr, (
                'Warning: SVG output not supported by this puzzle.\n')
        else:
            try:
                if hasattr(output_path, 'write'):
                    svg_file = output_path
                else:
                    svg_file = open(output_path, 'w')
                svg_file.write(svg)
            finally:
                if not hasattr(output_path, 'write'):
                    svg_file.close()

    def format_x3d(self, solution=None, s_matrix=None):
        """
        Return a puzzle-specific X3D formatting of a solution.

        Implement in subclasses.
        """
        raise NotImplementedError

    def write_x3d(self, output_path, solution=None, s_matrix=None):
        try:
            x3d = self.format_x3d(solution, s_matrix)
        except NotImplementedError:
            print >>sys.stderr, (
                'Warning: X3D output not supported by this puzzle.\n')
        else:
            try:
                x3d_file = open(output_path, 'w')
                x3d_file.write(x3d)
            finally:
                x3d_file.close()

    solution_header = re.compile(r'^solution (\d)+:$', re.IGNORECASE)

    def read_solution(self, input_path):
        if input_path == '-':
            input_file = sys.stdin
        elif hasattr(input_path, 'readline'):
            input_file = input_path
        else:
            input_file = open(input_path, 'r')
        try:
            for line in input_file:
                match = self.solution_header.match(line)
                if match:
                    #number = int(match.group(1))
                    break
            else:
                raise DataError('Input does not contain a solution record.')
            record = []
            for line in input_file:
                line = line.strip()
                if not line:
                    break
                record.append(line)
        finally:
            input_file.close()
        s_matrix = self.convert_record_to_solution_matrix(record)
        return s_matrix

    def convert_record_to_solution_matrix(self, record):
        """
        `record` is a list of strings, the solution record.

        Implement in subclasses
        """
        raise NotImplementedError

    def store_solutions(self, solution, formatted):
        """
        Return True if the solution is a duplicate, false if unique.

        Store the formatted solution along with puzzle-specific variants
        (reflections, rotations) in `self.solutions`, to check for duplicates.
        """
        if formatted in self.solutions:
            return True
        self.solutions.add(formatted)
        # keep track of formatted variants of *this* solution, to
        # differentiate from previous solutions:
        solutions = set([formatted])
        for conditions in self.duplicate_conditions:
            formatted = self.format_solution(solution, **conditions)
            if formatted in self.solutions:
                # applying duplicate conditions may result in variant
                # solutions identical to `formatted`
                if formatted not in solutions:
                    return True
            else:
                self.solutions.add(formatted)
                solutions.add(formatted)
        return False


class Puzzle2D(Puzzle):

    duplicate_conditions = ({'x_reversed': True},
                            {'y_reversed': True},
                            {'x_reversed': True, 'y_reversed': True})

    def coordinates(self):
        for y in range(self.height):
            for x in range(self.width):
                yield coordsys.Cartesian2D((x, y))

    def make_aspects(self, units, flips=(False, True), rotations=(0, 1, 2, 3)):
        aspects = set()
        coord_list = ((0, 0),) + units
        for flip in flips or (0,):
            for rotation in rotations or (0,):
                aspect = coordsys.Cartesian2DView(coord_list, rotation, flip)
                aspects.add(aspect)
        return aspects

    def build_matrix_header(self):
        headers = []
        for i, key in enumerate(sorted(self.pieces.keys())):
            self.matrix_columns[key] = i
            headers.append(key)
        for (x, y) in self.coordinates():
            header = '%0*i,%0*i' % (self.x_width, x, self.y_width, y)
            self.matrix_columns[header] = len(headers)
            headers.append(header)
        self.matrix.append(headers)

    def build_regular_matrix(self, keys):
        for key in keys:
            for coords, aspect in self.pieces[key]:
                for y in range(self.height - aspect.bounds[1]):
                    for x in range(self.width - aspect.bounds[0]):
                        translated = aspect.translate((x, y))
                        if translated.issubset(self.solution_coords):
                            self.build_matrix_row(key, translated)

    def build_matrix_row(self, name, coords):
        row = [0] * len(self.matrix[0])
        row[self.matrix_columns[name]] = name
        for coord in coords:
            label = '%0*i,%0*i' % (self.x_width, coord[0],
                                   self.y_width, coord[1])
            row[self.matrix_columns[label]] = label
        self.matrix.append(row)

    def format_solution(self, solution, normalized=True,
                        x_reversed=False, y_reversed=False):
        order_functions = (lambda x: x, reversed)
        x_reversed_fn = order_functions[x_reversed]
        y_reversed_fn = order_functions[1 - y_reversed] # reversed by default
        s_matrix = self.build_solution_matrix(solution)
        formatted= '\n'.join(
            ''.join('%-2s' % name for name in x_reversed_fn(s_matrix[y])
                    ).rstrip()
            for y in y_reversed_fn(range(self.height)))
        omitted = '\n'.join(
            '(%s omitted)' % row[-1] for row in solution if row[0] == '!')
        return '\n'.join([omitted, formatted])

    def empty_solution_matrix(self, margin=0):
        s_matrix = [[self.empty_cell] * (self.width + 2 * margin)
                    for y in range(self.height + 2 * margin)]
        return s_matrix

    def build_solution_matrix(self, solution, margin=0):
        s_matrix = self.empty_solution_matrix(margin)
        for row in solution:
            name = row[-1]
            for cell_name in row[:-1]:
                if cell_name.endswith('i') or cell_name == '!':
                    continue            # skip intersections & omitted pieces
                x, y = [int(d.strip()) for d in cell_name.split(',')]
                s_matrix[y + margin][x + margin] = name
        return s_matrix

    def format_svg(self, solution=None, s_matrix=None):
        if s_matrix:
            assert solution is None, ('Provide only one of solution '
                                      '& s_matrix arguments, not both.')
        else:
            s_matrix = self.build_solution_matrix(solution, margin=1)
        polygons = []
        for y in range(1, self.height + 1):
            for x in range(1, self.width + 1):
                if s_matrix[y][x] == self.empty_cell:
                    continue
                polygons.append(self.build_polygon(s_matrix, x, y))
        header = self.svg_header % {
            'height': (self.height + 2) * self.svg_unit_length,
            'width': (self.width + 2) * self.svg_unit_length}
        return '%s%s%s%s%s' % (header, self.svg_g_start, ''.join(polygons),
                               self.svg_g_end, self.svg_footer)

    def build_polygon(self, s_matrix, x, y):
        points = self.get_polygon_points(s_matrix, x, y)
        name = s_matrix[y][x]
        color = self.piece_colors[name]
        # Erase cells of this piece:
        for x, y in self.get_piece_cells(s_matrix, x, y):
            s_matrix[y][x] = self.empty_cell
        points_str = ' '.join('%.3f,%.3f' % (x, y) for (x, y) in points)
        return self.svg_polygon % {'color': color,
                                   'stroke': self.svg_stroke,
                                   'stroke_width': self.svg_stroke_width,
                                   'points': points_str,
                                   'name': name}

    edge_trace = {(+1,  0): ((( 0, -1), ( 0, -1)), # right
                             (( 0,  0), (+1,  0)),
                             (None,     ( 0, +1))),
                  (-1,  0): (((-1,  0), ( 0, +1)), # left
                             ((-1, -1), (-1,  0)),
                             (None,     ( 0, -1))),
                  ( 0, +1): ((( 0,  0), (+1,  0)), # up
                             ((-1,  0), ( 0, +1)),
                             (None,     (-1,  0))),
                  ( 0, -1): (((-1, -1), (-1,  0)), # down
                             (( 0, -1), ( 0, -1)),
                             (None,     (+1,  0))),}
    """Mapping of counterclockwise (x,y)-direction vector to list (ordered by
    test) of 2-tuples: examination cell coordinate delta & new direction
    vector."""

    def get_polygon_points(self, s_matrix, x, y):
        """
        Return a list of coordinate tuples, the corner points of the polygon
        for the piece at (x,y).
        """
        cell_content = s_matrix[y][x]
        unit = self.svg_unit_length
        height = (self.height + 2) * unit
        points = [(x * unit, height - y * unit)]
        direction = (+1, 0)             # to the right
        start = (x, y)
        x += 1
        while (x, y) != start:
            for delta, new_direction in self.edge_trace[direction]:
                if ( delta is None
                     or cell_content != '0'
                     and s_matrix[y + delta[1]][x + delta[0]] == cell_content):
                    break
            if new_direction != direction:
                direction = new_direction
                points.append((x * unit, height - y * unit))
            x += direction[0]
            y += direction[1]
        return points

    def get_piece_cells(self, s_matrix, x, y):
        cell_content = s_matrix[y][x]
        coord = self.coord_class((x, y))
        cells = set([coord])
        if cell_content != '0':
            self._get_piece_cells(cells, coord, s_matrix, cell_content)
        return cells

    def _get_piece_cells(self, cells, coord, s_matrix, cell_content):
        for neighbor in coord.neighbors():
            x, y = neighbor
            if neighbor not in cells and s_matrix[y][x] == cell_content:
                cells.add(neighbor)
                self._get_piece_cells(cells, neighbor, s_matrix, cell_content)

    def format_coords_svg(self, piece_name='0'):
        s_matrix = self.empty_solution_matrix(margin=self.margin)
        for x, y in self.solution_coords:
            s_matrix[y + self.margin][x + self.margin] = piece_name
        return self.format_svg(s_matrix=s_matrix)

    def convert_record_to_solution_matrix(self, record):
        s_matrix = self.empty_solution_matrix(self.margin)
        for row in record:
            parts = row.split()
            name = parts[-1]
            for coords in parts[:-1]:
                if coords.endswith('i') or coords == '!':
                    continue            # skip intersections & omitted pieces
                x, y = coords.split(',')
                s_matrix[int(y) + self.margin][int(x) + self.margin] = name
        return s_matrix


class Puzzle3D(Puzzle):

    margin = 0
    piece_width = 2                     # for format_solution
    svg_x_width = 9
    svg_x_height = -2
    svg_y_height = 10
    svg_z_height = -3
    svg_z_width = -6
    svg_stroke_width = '0.5'
    svg_defs_start = '<defs>\n'
    svg_cube_def = '''\
<symbol id="cube%(name)s">
<polygon fill="%(color)s" stroke="%(stroke)s"
         stroke-width="%(stroke_width)s" stroke-linejoin="round"
         points="0,13 9,15 15,12 15,2 6,0 0,3" />
<polygon fill="black" fill-opacity="0.25" stroke="%(stroke)s"
         stroke-width="%(stroke_width)s" stroke-linejoin="round"
         points="9,15 15,12 15,2 9,5" />
<polygon fill="white" fill-opacity="0.30" stroke="%(stroke)s"
         stroke-width="%(stroke_width)s" stroke-linejoin="round"
         points="0,3 9,5 15,2 6,0" />
</symbol>
'''
    svg_defs_end = '</defs>\n'
    svg_cube = '<use xlink:href="#cube%(name)s" x="%(x).3f" y="%(y).3f" />\n'

    x3d_box = '''\
<Transform translation="%(x)s %(y)s %(z)s">
  <Shape>
    <Appearance>
      <Material diffuseColor="%(color)s"/>
    </Appearance>
    <Box size="1 1 1"/>
  </Shape>
</Transform>
'''

    def coordinates(self):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    yield coordsys.Cartesian3D((x, y, z))

    def make_aspects(self, units,
                     flips=(0, 1), axes=(0, 1, 2), rotations=(0, 1, 2, 3)):
        aspects = set()
        coord_list = ((0, 0, 0),) + units
        for axis in axes or (2,):
            coord_set = coordsys.Cartesian3DView(coord_list)
            if axis != 2:
                coord_set = coord_set.rotate0(1, (1 - axis) % 3)
            coords = tuple(coord_set)
            for flip in flips or (0,):
                for rotation in rotations or (0,):
                    aspect = coordsys.Cartesian3DView(
                        coords, rotation, axis, flip)
                    aspects.add(aspect)
        return aspects

    def build_matrix_header(self):
        headers = []
        for i, key in enumerate(sorted(self.pieces.keys())):
            self.matrix_columns[key] = i
            headers.append(key)
        for (x, y, z) in self.coordinates():
            header = '%0*i,%0*i,%0*i' % (
                self.x_width, x, self.y_width, y, self.z_width, z)
            self.matrix_columns[header] = len(headers)
            headers.append(header)
        self.matrix.append(headers)

    def build_regular_matrix(self, keys):
        for key in keys:
            for coords, aspect in self.pieces[key]:
                for z in range(self.depth - aspect.bounds[2]):
                    for y in range(self.height - aspect.bounds[1]):
                        for x in range(self.width - aspect.bounds[0]):
                            translated = aspect.translate((x, y, z))
                            if translated.issubset(self.solution_coords):
                                self.build_matrix_row(key, translated)

    def build_matrix_row(self, name, coords):
        row = [0] * len(self.matrix[0])
        row[self.matrix_columns[name]] = name
        for coord in coords:
            label = '%0*i,%0*i,%0*i' % (self.x_width, coord[0],
                                        self.y_width, coord[1],
                                        self.z_width, coord[2])
            row[self.matrix_columns[label]] = label
        self.matrix.append(row)

    def format_solution(self, solution, normalized=True,
                        x_reversed=False, y_reversed=False, z_reversed=False,
                        xy_swapped=False, xz_swapped=False, yz_swapped=False):
        order_functions = (lambda x: x, reversed)
        x_reversed_fn = order_functions[x_reversed]
        y_reversed_fn = order_functions[1 - y_reversed] # reversed by default
        z_reversed_fn = order_functions[z_reversed]
        #s_matrix = self.build_solution_matrix(solution)
        s_matrix = self.empty_solution_matrix()
        for row in solution:
            name = row[-1]
            for cell_name in row[:-1]:
                x, y, z = (int(d.strip()) for d in cell_name.split(','))
                if xy_swapped:
                    x, y = y, x
                if xz_swapped:
                    x, z = z, x
                if yz_swapped:
                    y, z = z, y
                s_matrix[z][y][x] = name
        return '\n'.join(
            '    '.join(''.join('%-*s' % (self.piece_width, name)
                                for name in x_reversed_fn(s_matrix[z][y]))
                        for z in z_reversed_fn(range(self.depth))).rstrip()
            for y in y_reversed_fn(range(self.height)))

    def empty_solution_matrix(self, margin=0):
        s_matrix = [[[self.empty_cell] * (self.width + 2 * margin)
                     for y in range(self.height + 2 * margin)]
                    for z in range(self.depth + 2 * margin)]
        return s_matrix

    def build_solution_matrix(self, solution, margin=0):
        s_matrix = self.empty_solution_matrix(margin)
        for row in solution:
            name = row[-1]
            for cell_name in row[:-1]:
                x, y, z = [int(d.strip()) for d in cell_name.split(',')]
                s_matrix[z + margin][y + margin][x + margin] = name
        return s_matrix

    def format_svg(self, solution=None, s_matrix=None):
        if s_matrix:
            assert solution is None, ('Provide only one of solution '
                                      '& s_matrix arguments, not both.')
        else:
            s_matrix = self.build_solution_matrix(solution)
        s_matrix = self.transform_solution_matrix(s_matrix)
        s_depth = len(s_matrix)
        s_height = len(s_matrix[0])
        s_width = len(s_matrix[0][0])
        height = (s_height * abs(self.svg_y_height)
                  + s_depth * abs(self.svg_z_height)
                  + s_width * abs(self.svg_x_height)
                  + 2 * self.svg_unit_length)
        width = (s_width * abs(self.svg_x_width)
                  + s_depth * abs(self.svg_z_width)
                  + 2 * self.svg_unit_length)
        cube_defs = []
        for name in sorted(self.piece_colors.keys()):
            color = self.piece_colors[name]
            cube_defs.append(
                self.svg_cube_def % {'color': color,
                                     'stroke': self.svg_stroke,
                                     'stroke_width': self.svg_stroke_width,
                                     'name': name})
        cubes = []
        for z in range(s_depth):
            for y in range(s_height):
                for x in range(s_width):
                    name = s_matrix[z][y][x]
                    if name == self.empty_cell:
                        continue
                    cubes.append(
                        self.svg_cube
                        % {'name': name,
                           'x': (x * self.svg_x_width
                                 + (z + 1 - s_depth) * self.svg_z_width
                                 + self.svg_unit_length),
                           'y': (height
                                 - (y * self.svg_y_height
                                    + (z - s_depth) * self.svg_z_height
                                    + (x - s_width) * self.svg_x_height
                                    + 2 * self.svg_unit_length))})
        header = self.svg_header % {'height': height, 'width': width}
        defs = '%s%s%s' % (self.svg_defs_start, ''.join(cube_defs),
                           self.svg_defs_end)
        return '%s%s%s%s%s%s' % (header, defs, self.svg_g_start,
                                 ''.join(cubes), self.svg_g_end,
                                 self.svg_footer)

    def format_coords_svg(self, piece_name='0'):
        s_matrix = self.empty_solution_matrix(margin=self.margin)
        for x, y, z in self.solution_coords:
            s_matrix[z + self.margin][y + self.margin][
                x + self.margin] = piece_name
        return self.format_svg(s_matrix=s_matrix)

    def format_x3d(self, solution=None, s_matrix=None):
        if s_matrix:
            assert solution is None, ('Provide only one of solution '
                                      '& s_matrix arguments, not both.')
        else:
            s_matrix = self.build_solution_matrix(solution)
        s_matrix = self.transform_solution_matrix(s_matrix)
        s_depth = len(s_matrix)
        s_height = len(s_matrix[0])
        s_width = len(s_matrix[0][0])
        cubes = []
        for z in range(s_depth):
            for y in range(s_height):
                for x in range(s_width):
                    name = s_matrix[z][y][x]
                    if name == self.empty_cell:
                        continue
                    cubes.append(
                        self.x3d_box
                        % {'name': name, 'x': x, 'y': y, 'z': z,
                           'color': colors.x3d[self.piece_colors[name]]})
        return '%s%s%s' % (self.x3d_header, ''.join(cubes), self.x3d_footer)

    def transform_solution_matrix(self, s_matrix):
        """Transform for rendering `s_matrix`.  Override in subclasses."""
        return s_matrix

    def swap_yz_transform(self, s_matrix):
        """Common solution matrix transform: Z, Y = reversed(Y), Z."""
        return [[[s_matrix[z][y][x] for x in range(self.width)]
                 for z in range(self.depth)]
                for y in reversed(range(self.height))]

    def cycle_xyz_transform(self, s_matrix):
        """Common solution matrix transform: cycle X Y & Z dimensions."""
        return [[[s_matrix[z][y][x] for y in range(self.height)]
                 for z in range(self.depth)]
                for x in range(self.width)]

    def convert_record_to_solution_matrix(self, record):
        s_matrix = self.empty_solution_matrix(self.margin)
        for row in record:
            parts = row.split()
            name = parts[-1]
            for coords in parts[:-1]:
                if coords.endswith('i') or coords == '!':
                    continue            # skip intersections & omitted pieces
                x, y, z = (int(coord) + self.margin
                           for coord in coords.split(','))
                s_matrix[z][y][x] = name
        return s_matrix


class PuzzlePseudo3D(Puzzle3D):

    """The Z dimension is used for direction/orientation."""

    def empty_solution_matrix(self, margin=0):
        s_matrix = [[[self.empty_cell] * (self.width + 2 * margin)
                     for y in range(self.height + 2 * margin)]
                    for z in range(self.depth)]
        return s_matrix

    def build_solution_matrix(self, solution, margin=0):
        s_matrix = self.empty_solution_matrix(margin)
        for row in solution:
            name = row[-1]
            for cell_name in row[:-1]:
                x, y, z = [int(d.strip()) for d in cell_name.split(',')]
                s_matrix[z][y + margin][x + margin] = name
        return s_matrix

    def format_coords_svg(self, piece_name='0'):
        s_matrix = self.empty_solution_matrix(margin=self.margin)
        for x, y, z in self.solution_coords:
            s_matrix[z][y + self.margin][x + self.margin] = piece_name
        return self.format_svg(s_matrix=s_matrix)

    def format_x3d(self, solution=None, s_matrix=None):
        raise NotImplementedError


class OneSidedLowercaseMixin(object):

    """
    Must be the first base class listed in client subclass definitions for
    MRO (method resolution order) to work.
    """

    def customize_piece_data(self):
        """
        Disable flips on all pieces, and add flipped versions of asymmetric
        pieces with lowercase names.
        """
        self.piece_colors = copy.deepcopy(self.piece_colors)
        for key in self.piece_data.keys():
            self.piece_data[key][-1]['flips'] = None
        for key in self.asymmetric_pieces:
            new_key = key.lower()
            self.piece_data[new_key] = copy.deepcopy(self.piece_data[key])
            self.piece_data[new_key][-1]['flips'] = (1,)
            self.piece_colors[new_key] = self.piece_colors[key]


if __name__ == '__main__':
    from puzzler.puzzles.pentominoes import Pentominoes6x10
    p = Pentominoes6x10()
    print 'matrix length =', len(p.matrix)
    print 'first 20 rows:'
    pprint(p.matrix[:20], width=720)