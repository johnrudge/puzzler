.. -*- coding: utf-8 -*-

================================
 An Introduction to Polyiamonds
================================

:Author: David Goodger <goodger@python.org>
:Date: $Date$
:Revision: $Revision$
:Web site: http://puzzler.sourceforge.net/
:Copyright: |c| 1998-2015 by David J. Goodger
:License: `GPL 2 <../COPYING.html>`__

.. image:: images/puzzler.png
   :align: center

.. sidebar:: Also see:

   * `Polyiamonds: Puzzles & Solutions <polyiamonds.html>`_
   * `Hexiamonds: Puzzles & Solutions <hexiamonds.html>`_
   * `Heptiamonds: Puzzles & Solutions <heptiamonds.html>`_
   * `Notes on Polyiamonds <polyiamond-notes.html>`_
   * `Polyform Puzzler: Puzzles & Solutions <puzzles.html>`_
   * `Polyform Puzzler FAQ <FAQ.html>`_
     (`polyform details <FAQ.html#what-polyforms-are-there>`__,
     `numbers of polyforms <FAQ.html#how-many-of-each-type-of-polyform-are-there>`__,
     `interpreting solution files <FAQ.html#how-should-polyiamond-solution-files-be-interpreted>`__)

.. contents::

**Polyiamonds** are polyforms constructed from unit equilateral
triangles joined edge-to-edge on a triangular grid.  The name comes
from diamonds the same way "polyominoes" comes from "dominoes"; one
diamond is composed of two ("di-") unit triangles ("-iamond").

Here is a puzzle containing all the polyiamonds of order 1 through 6:

.. image:: images/iamonds/polyiamonds-123456-elongated-hexagon-3x5.png

See `Polyiamonds: Puzzles & Solutions`_, `Hexiamonds: Puzzles &
Solutions`_, and `Heptiamonds: Puzzles & Solutions`_ for many more
puzzles.


Polyforms
=========

The number and names of the various orders of polyiamonds are as
follows:

=====  ===========  =============  =============
Order  | Polyform   | Free         | One-Sided
       | Name       | Polyiamonds  | Polyiamonds
=====  ===========  =============  =============
1      moniamond    1              1
2      diamond      1              1
3      triamonds    1              1
4      tetriamonds  3              4
5      pentiamonds  4              6
6      hexiamonds   12             19
7      heptiamonds  24             43
8      octiamonds   66             120
=====  ===========  =============  =============

The numbers of polyiamonds can also be found in the following sequences
from `The On-Line Encyclopedia of Integer Sequences
<http://oeis.org>`_: A000577_ (free) and A006534_ (one-sided).

.. _A000577: http://oeis.org/A000577
.. _A006534: http://oeis.org/A006534

Examples of the polyiamonds from order 1 (moniamond) to order 7
(heptiamonds) are given in the tables below.

The polyiamonds are named with a letter-number scheme (like the "P6"
hexiamond).  The initial letter of each name is the letter of the
alphabet that the polyiamond most closely resembles, or an initial.
In some cases, that resemblance is weak (or non-existant!), and the
letters are arbitrary.  The final digit of the number represents the
polyform order (how many unit triangles are in the polyiamond).

.. _table legend:

In the tables below, "Aspects" refers to the number of unique
orientations that a polyform may take (different rotations, flipped or
not).  This varies with the symmetry of the polyform.

The "One-Sided" column identifies polyforms that are asymmetrical in
reflection.  Treating the flipped and unflipped versions of
asymmetrical polyiamonds as distinct polyforms (and disallowing
further reflection or "flipping"), results in "one-sided" polyiamonds
and puzzles.

The "Disparity" column shows the discrepancy in parity of the
polyiamond's unit triangles, i.e. the difference between the number of
z=0 and z=1 units in the polyiamond.  Left blank when there is no
difference.

Alternate names and name origins are noted in the "Name" column.


Moniamond
---------

There is only one moniamond (order-1 polyiamond):

.. list-table::
   :widths: 40 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Disparity

   * - | T1
       | (from "Triangle")
     - .. image:: images/pieces/polyiamonds/T1.png
     - 2
     -
     - 1


Diamond
-------

There is only one diamond (order-2 polyiamond):

.. list-table::
   :widths: 40 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Disparity

   * - | D2
       | (from "Diamond")
     - .. image:: images/pieces/polyiamonds/D2.png
     - 3
     -
     -


Triamond
--------

There is only one triamond (order-3 polyiamond):

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Disparity

   * - I3
     - .. image:: images/pieces/polyiamonds/I3.png
     - 6
     -
     - 1


Tetriamonds
-----------

There are 3 free tetriamonds (order-4 polyiamonds) and 4 one-sided
tetriamonds:

.. list-table::
   :widths: 40 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Disparity

   * - C4
     - .. image:: images/pieces/polyiamonds/C4.png
     - 6
     -
     -

   * - I4
     - .. image:: images/pieces/polyiamonds/I4.png
     - 6
     - yes
     -

   * - | T4
       | (from "Triangle")
     - .. image:: images/pieces/polyiamonds/T4.png
     - 2
     -
     - 2


Pentiamonds
-----------

There are 4 free pentiamonds (order-5 polyiamonds) and 6 one-sided
pentiamonds:

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Disparity

   * - C5
     - .. image:: images/pieces/polyiamonds/C5.png
     - 6
     -
     - 1

   * - I5
     - .. image:: images/pieces/polyiamonds/I5.png
     - 6
     -
     - 1

   * - L5
     - .. image:: images/pieces/polyiamonds/L5.png
     - 12
     - yes
     - 1

   * - P5
     - .. image:: images/pieces/polyiamonds/P5.png
     - 12
     - yes
     - 1


Hexiamonds
----------

There are 12 free hexiamonds (order-6 polyiamonds) and 19 one-sided
hexiamonds:

.. list-table::
   :widths: 20 10 10 10 10
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Disparity

   * - | C6
       | (a.k.a. "Chevron" or "Bat")
     - .. image:: images/pieces/polyiamonds/C6.png
     - 6
     -
     -

   * - | E6
       | (a.k.a. "Crown")
     - .. image:: images/pieces/polyiamonds/E6.png
     - 6
     -
     -

   * - | F6
       | (a.k.a. "Yacht")
     - .. image:: images/pieces/polyiamonds/F6.png
     - 12
     - yes
     - 2

   * - | G6
       | (a.k.a. "Shoe" or "Hook")
     - .. image:: images/pieces/polyiamonds/G6.png
     - 12
     - yes
     -

   * - | H6
       | (a.k.a. "Pistol" or "Signpost")
     - .. image:: images/pieces/polyiamonds/H6.png
     - 12
     - yes
     -

   * - | I6
       | (a.k.a. "Bar" or "Rhomboid")
     - .. image:: images/pieces/polyiamonds/I6.png
     - 6
     - yes
     -

   * - | J6
       | (a.k.a. "Club" or "Crook")
     - .. image:: images/pieces/polyiamonds/J6.png
     - 12
     - yes
     -

   * - | O6
       | (a.k.a. "Hexagon")
     - .. image:: images/pieces/polyiamonds/O6.png
     - 1
     -
     -

   * - | P6
       | (a.k.a. "Sphinx")
     - .. image:: images/pieces/polyiamonds/P6.png
     - 12
     - yes
     - 2

   * - | S6
       | (a.k.a. "Snake")
     - .. image:: images/pieces/polyiamonds/S6.png
     - 6
     - yes
     -

   * - | V6
       | (a.k.a. "Lobster")
     - .. image:: images/pieces/polyiamonds/V6.png
     - 6
     -
     -

   * - | X6
       | (a.k.a. "Butterfly")
     - .. image:: images/pieces/polyiamonds/X6.png
     - 3
     -
     -


Heptiamonds
-----------

There are 24 free heptiamonds (order-7 polyiamonds) and 43 one-sided
heptiamonds:

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Disparity

   * - A7
     - .. image:: images/pieces/polyiamonds/A7.png
     - 12
     - yes
     - 1

   * - B7
     - .. image:: images/pieces/polyiamonds/B7.png
     - 12
     - yes
     - 1

   * - C7
     - .. image:: images/pieces/polyiamonds/C7.png
     - 6
     -
     - 1

   * - D7
     - .. image:: images/pieces/polyiamonds/D7.png
     - 6
     -
     - 1

   * - E7
     - .. image:: images/pieces/polyiamonds/E7.png
     - 12
     - yes
     - 1

   * - F7
     - .. image:: images/pieces/polyiamonds/F7.png
     - 12
     - yes
     - 1

   * - G7
     - .. image:: images/pieces/polyiamonds/G7.png
     - 12
     - yes
     - 1

   * - H7
     - .. image:: images/pieces/polyiamonds/H7.png
     - 12
     - yes
     - 1

   * - I7
     - .. image:: images/pieces/polyiamonds/I7.png
     - 6
     -
     - 1

   * - J7
     - .. image:: images/pieces/polyiamonds/J7.png
     - 12
     - yes
     - 1

   * - L7
     - .. image:: images/pieces/polyiamonds/L7.png
     - 12
     - yes
     - 1

   * - M7
     - .. image:: images/pieces/polyiamonds/M7.png
     - 6
     -
     - 3

   * - N7
     - .. image:: images/pieces/polyiamonds/N7.png
     - 12
     - yes
     - 1

   * - P7
     - .. image:: images/pieces/polyiamonds/P7.png
     - 12
     - yes
     - 1

   * - Q7
     - .. image:: images/pieces/polyiamonds/Q7.png
     - 12
     - yes
     - 1

   * - R7
     - .. image:: images/pieces/polyiamonds/R7.png
     - 12
     - yes
     - 1

   * - S7
     - .. image:: images/pieces/polyiamonds/S7.png
     - 12
     - yes
     - 1

   * - T7
     - .. image:: images/pieces/polyiamonds/T7.png
     - 12
     - yes
     - 1

   * - U7
     - .. image:: images/pieces/polyiamonds/U7.png
     - 12
     - yes
     - 1

   * - V7
     - .. image:: images/pieces/polyiamonds/V7.png
     - 6
     -
     - 1

   * - W7
     - .. image:: images/pieces/polyiamonds/W7.png
     - 4
     - yes
     - 1

   * - X7
     - .. image:: images/pieces/polyiamonds/X7.png
     - 12
     - yes
     - 1

   * - Y7
     - .. image:: images/pieces/polyiamonds/Y7.png
     - 12
     - yes
     - 1

   * - Z7
     - .. image:: images/pieces/polyiamonds/Z7.png
     - 12
     - yes
     - 1


Coordinate System
=================

Polyiamonds use a pseudo-3-dimensional skewed *(x,y,z)* Cartesian
coordinate system. The X and Y axes are 60?? apart instead of 90??, and
the Z dimension is used to represent the orientation of triangles::

                  ____
         /\       \  /
    z=0 /__\,  z=1 \/

Example (with coordinates)::

                  x=0  1   2   3   4   5   6   7   8
                 ____________________________________
                /   /           /    \      /       /
            3  /   /___________/   ___\    /       /
              /       /    \      /   /    \  /\  /
          2  /_______/      \____/   /______\/  \/
            /       /\      /   /\       \      /
        1  /   ____/  \____/   /  \_______\    /
          /   /        \       \          /   /
    y=0  /___/__________\_______\________/___/

         x=0  1   2   3   4   5   6   7   8

Each coordinate triple locates a triangle. The *(x,y)* pair locates an
equilateral parallelogram (*not* a point), and the *z* coordinate
identifies the triangle (half of the parallelogram).

Another example::

             .    /\    ..    .
              .G /F \H .  .I .
          ______/____\_ _ _..
         /\    /\    /\    .
    y=0 /A \B /C \D /E \  .
       /____\/____\/____\
        x=0

The coordinates in the figure above are as follows:

| A: (0,0,0)
| B: (0,0,1) -- same X=column as A, same Y=row as A,
  different orientation so Z=1
| C: (1,0,0) -- different X=column from A, same Y=row as A, 
  same Z=orientation as A
| D: (1,0,1)
| E: (2,0,0)
| F: (1,1,0) -- same X=column as C & D, different Y=row from all the
  others, same Z=orientation as C but different from D.

The coordinate (0,1,1) would be at G, (1,1,1) would be at H, and
(2,1,1) would be at I.  The *(x,y)* coordinates (0,0) identify the
parallelogram formed from triangles A & B, (1,0) is C & D together,
etc.

Each unit triangle has 3 immediate neighbors.  The neighbors of the
triangle at coordinates *(x, y, 0)* are:

    *{(x, y, 1), (x-1, y, 1), (x, y-1, 1)}*

The neighbors of the triangle at coordinates *(x, y, 1)* are:

    *{(x, y, 0), (x+1, y, 0), (x, y+1, 0)}*


.. _Poly-4 Supplement: http://www.gamepuzzles.com/poly4.htm

.. |c| unicode:: U+00A9 .. copyright sign
