.. -*- coding: utf-8 -*-

=================================
 Polysticks: Puzzles & Solutions
=================================

:Author: David Goodger <goodger@python.org>
:Date: $Date$
:Revision: $Revision$
:Web site: http://puzzler.sourceforge.net/
:Copyright: |c| 1998-2015 by David J. Goodger
:License: `GPL 2 <../COPYING.html>`__

.. image:: images/puzzler.png
   :align: center

.. sidebar:: Also see:

   * `An Introduction to Polysticks <polysticks-intro.html>`_
   * `Notes on Polysticks <polystick-notes.html>`_
   * `Polytrigs (Triangular-Grid Polysticks): Puzzles & Solutions <polytrigs.html>`_
   * `An Introduction to Polytrigs (Triangular-Grid Polysticks) <polytrigs-intro.html>`_
   * `Polytwigs (Hexagonal-Grid Polysticks): Puzzles & Solutions <polytwigs.html>`_
   * `An Introduction to Polytwigs (Hexagonal-Grid Polysticks) <polytwigs-intro.html>`_
   * `Polyform Puzzler: Puzzles & Solutions <puzzles.html>`_
   * `Polyform Puzzler FAQ <FAQ.html>`_
     (`polyform details <FAQ.html#what-polyforms-are-there>`__,
     `numbers of polyforms <FAQ.html#how-many-of-each-type-of-polyform-are-there>`__,
     `interpreting solution files <FAQ.html#how-should-polystick-solution-files-be-interpreted>`__)

.. contents::


Polysticks of Order 1 Through 3
===============================

These puzzles use the 1 monostick, 2 disticks, and 5 tristicks, for
a total of 20 line segments on the square grid.

* 4x4 grid with clipped corners:

  .. list-table::
     :class: borderless

     * - .. figure:: images/sticks/polysticks-123-4x4-clipped-corners-1.png

            `21 solutions
            <../solutions/sticks/polysticks-123-4x4-clipped-corners-1.txt>`__

       - .. figure:: images/sticks/polysticks-123-4x4-clipped-corners-2.png

            `132 solutions
            <../solutions/sticks/polysticks-123-4x4-clipped-corners-2.txt>`__


Tetrasticks
===========

One-Sided Welded Tetrasticks
----------------------------

The "welded" tetrasticks are those that contain junction points, or
welds, and therefore do not form simple connected paths (in other
words, they branch).  There are 6 welded tetrasticks, 4 of which are
asymmetrical, therefore there are 10 one-sided welded tetrasticks.

* 5x5 grid: `3 solutions
  <../solutions/sticks/one-sided-welded-tetrasticks-5x5.txt>`__

  .. image:: images/sticks/one-sided-welded-tetrasticks-5x5.png

* Triangle: `9 solutions
  <../solutions/sticks/one-sided-welded-tetrasticks-triangle.txt>`__

  .. image:: images/sticks/one-sided-welded-tetrasticks-triangle.png

* Trapezoid: `7 solutions
  <../solutions/sticks/one-sided-welded-tetrasticks-trapezoid.txt>`__

  .. image:: images/sticks/one-sided-welded-tetrasticks-trapezoid.png


15 of 16 Tetrasticks
--------------------

Due to an imbalance in horizontal/vertical parity, the 16 tetrasticks
cannot be formed into a symmetrical shape.  But by omitting one of the
five tetrasticks that have an excess of 2 vertical or horizontal line
segments (H, J, L, N, or Y), symmetrical shapes can be formed.

* 6x6 grid: `1795 solutions
  <../solutions/sticks/tetrasticks-6x6.txt>`__

  In this solution, the "Y" piece is omitted:

  .. image:: images/sticks/tetrasticks-6x6.png

* Aztec Diamond of order 3: `3 solutions
  <../solutions/sticks/tetrasticks-aztec-diamond.txt>`__

  In this solution, the "J" piece is omitted:

  .. image:: images/sticks/tetrasticks-aztec-diamond.png


One-Sided Tetrasticks
---------------------

9 of the 16 tetrasticks are asymmetrical, therefore there are 25
one-sided tetrasticks.

* 5x5 diamond lattice: `107 solutions
  <../solutions/sticks/one-sided-tetrasticks-5x5-diamond-lattice.txt>`__

  .. image:: images/sticks/one-sided-tetrasticks-5x5-diamond-lattice.png

  Calculating all 107 non-isomorphic solutions took approximately **11
  weeks** using one core of a 2.66GHz Intel Core 2 Duo E6750 CPU
  (Python 2.6.6, Windows XP) on an otherwise idle and always-on
  machine.  The calculated solutions correspond to those listed in
  `"Covering the Aztec Diamond with One-sided Tetrasticks, Extended
  Version", by Alfred Wassermann, University of Bayreuth`__.
  (Wassermann, and Knuth before him, mistakenly called the shape an
  "aztec diamond", but an `aztec diamond is a subtly different
  shape`__.  This puzzle actually corresponds to a `centered square
  number`__.)

  __ http://did.mat.uni-bayreuth.de/~alfred/home/index.html
  __ http://mathworld.wolfram.com/AztecDiamond.html
  __ http://mathworld.wolfram.com/CenteredSquareNumber.html

  The solution above is number 9 in Wassermann's paper, and number 58
  in the `Polyform Puzzler solutions`__.  Both Wassermann's and the
  Polyform Puzzler solution sets are split into six sub-puzzles by
  position of the "X" piece, and correspond as follows:

  ================  ==========  =========
  X-Position (sub-puzzle)
  ----------------------------  ---------
  Polyform Puzzler  Wassermann  Solutions
  ================  ==========  =========
  A (symmetrical)   6           19
  B                 5           36
  C (symmetrical)   2           11
  D                 4           19
  E                 1           15
  F                 3           7
  ================  ==========  =========

  __ ../solutions/sticks/one-sided-tetrasticks-5x5-diamond-lattice.txt

  Note: The Polyform Puzzler order for the X-positions is in
  increasing distance from the center of the puzzle.  Wassermann's
  order is as follows: with all X-piece possitions in the upper-left
  quadrant in two horizontal rows (rotate the diagrams in the paper
  90?? clockwise), ordered from left to right, top to bottom.
  Symmetrical X-positions (X-piece on the diagonal) have the I-piece
  limited to horizontal for both Polyform Puzzler and Wassermann (when
  rotated as noted above).

* 8x8 grid with center hole: `solutions incomplete
  <../solutions/sticks/one-sided-tetrasticks-8x8-center-hole.txt>`__

  .. image:: images/sticks/one-sided-tetrasticks-8x8-center-hole.png

* 8x8 grid with one clipped corner: `solutions incomplete
  <../solutions/sticks/one-sided-tetrasticks-8x8-clipped-corner.txt>`__

  .. image:: images/sticks/one-sided-tetrasticks-8x8-clipped-corner.png

* 8x8 grid with two clipped corners 1: `solutions incomplete
  <../solutions/sticks/one-sided-tetrasticks-8x8-clipped-corners-1.txt>`__

  .. image:: images/sticks/one-sided-tetrasticks-8x8-clipped-corners-1.png

* X (`designed for G4G10 <g4gX.html>`_):

  .. list-table::
     :class: borderless

     * - .. figure:: images/sticks/one-sided-tetrasticks-x-1.png

            `solutions incomplete
            <../solutions/sticks/one-sided-tetrasticks-x-1.txt>`__

       - .. figure:: images/sticks/one-sided-tetrasticks-x-2.png

            `solutions incomplete
            <../solutions/sticks/one-sided-tetrasticks-x-2.txt>`__

* 10x5 trapezoid: `solutions incomplete
  <../solutions/sticks/one-sided-tetrasticks-trapezoid-10x5.txt>`__

  .. image:: images/sticks/one-sided-tetrasticks-trapezoid-10x5.png


Polysticks of Order 1 Through 4
===============================

These puzzles use the 1 monostick, 2 disticks, 5 tristicks, and 16
tetrasticks, for a total of 84 line segments.

* 7x7 grid: `solutions incomplete
  <../solutions/sticks/polysticks-1234-7x7.txt>`__

  .. image:: images/sticks/polysticks-1234-7x7.png

* 10x5 grid (with a hole): `solutions incomplete
  <../solutions/sticks/polysticks-1234-10x5.txt>`__

  .. image:: images/sticks/polysticks-1234-10x5.png

* 3x7 diamond lattice: `solutions incomplete
  <../solutions/sticks/polysticks-1234-3x7-diamond-lattice.txt>`__

  .. image:: images/sticks/polysticks-1234-3x7-diamond-lattice.png

* Truncated diamond lattices:

  - 6x4: `solutions incomplete
    <../solutions/sticks/polysticks-1234-truncated-diamond-lattice-6x4.txt>`__

    .. image:: images/sticks/polysticks-1234-truncated-diamond-lattice-6x4.png

  - 8x3: `solutions incomplete
    <../solutions/sticks/polysticks-1234-truncated-diamond-lattice-8x3.txt>`__

    .. image:: images/sticks/polysticks-1234-truncated-diamond-lattice-8x3.png

  - 12x2: `solutions incomplete
    <../solutions/sticks/polysticks-1234-truncated-diamond-lattice-12x2.txt>`__

    .. image:: images/sticks/polysticks-1234-truncated-diamond-lattice-12x2.png

* Octagons:

  .. list-table::
     :class: borderless

     * - .. figure:: images/sticks/polysticks-1234-octagon-1.png

            `solutions incomplete
            <../solutions/sticks/polysticks-1234-octagon-1.txt>`__

       - .. figure:: images/sticks/polysticks-1234-octagon-2.png

            `solutions incomplete
            <../solutions/sticks/polysticks-1234-octagon-2.txt>`__

* Four overlapping squares: `solutions incomplete
  <../solutions/sticks/polysticks-1234-four-squares-1.txt>`__

  .. image:: images/sticks/polysticks-1234-four-squares-1.png

* Three overlapping squares: `solutions incomplete
  <../solutions/sticks/polysticks-1234-three-squares-1.txt>`__

  .. image:: images/sticks/polysticks-1234-three-squares-1.png


Seven-Segment Digits
====================

The pieces in this puzzle are modeled after the seven-segment display
digits 0 through 9, as seen on digital watches, for a total of 49 line
segments.  Based on the "Digigrams" puzzle (AKA "Count On Me" or
"Count Me In") by Martin H. Watson.

In the following puzzle, the digit pairs (2, 5) and (6, 9) are
considered identical for the sake of counting solutions (preventing
duplicate solutions). Also note that the 0 digit has a gap in one long
side, allowing the 1 or 7 digit to intersect and occupy the 0 digit's
otherwise enclosed central line segment.

* 6x5 grid: `5 solutions
  <../solutions/sticks/seven-segment-digits-6x5.txt>`__

  .. image:: images/sticks/seven-segment-digits-6x5.png

  Unfortunately, there are no solutions where all of the digits are
  unflipped.  For example, in the solution above, the green 2 digit is
  flipped and appears as a second 5.

.. |c| unicode:: U+00A9 .. copyright sign
