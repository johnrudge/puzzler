.. -*- coding: utf-8 -*-

==================================
 Pentominoes: Puzzles & Solutions
==================================

:Author: David Goodger <goodger@python.org>
:Date: $Date$
:Revision: $Revision$
:Web site: http://puzzler.sourceforge.net/
:Copyright: |c| 1998-2016 by David J. Goodger
:License: `GPL 2 <../COPYING.html>`__

.. image:: images/puzzler.png
   :align: center

.. sidebar:: Also see:

   * `Polyominoes: Puzzles & Solutions <polyominoes.html>`_
   * `Hexominoes: Puzzles & Solutions <hexominoes.html>`_
   * `Solid Pentominoes: Puzzles & Solutions <solid-pentominoes.html>`_
   * `Pentacubes: Puzzles & Solutions <pentacubes.html>`_
   * `Polycubes: Puzzles & Solutions <polycubes.html>`_
   * `An Introduction to Polyominoes <polyominoes-intro.html>`_
   * `Notes on Polyominoes <polyomino-notes.html>`_
   * `Polyform Puzzler: Puzzles & Solutions <puzzles.html>`_
   * `Polyform Puzzler FAQ <FAQ.html>`_
     (`polyform details <FAQ.html#what-polyforms-are-there>`__,
     `numbers of polyforms <FAQ.html#how-many-of-each-type-of-polyform-are-there>`__,
     `interpreting solution files <FAQ.html#how-should-polyomino-solution-files-be-interpreted>`__)

.. contents::


Pentominoes
===========

Rectangles
----------

- 3x20: `2 solutions
  <../solutions/ominoes/pentominoes-3x20.txt>`__

  .. image:: images/ominoes/pentominoes-3x20.png

- 4x15: `368 solutions
  <../solutions/ominoes/pentominoes-4x15.txt>`__

  .. image:: images/ominoes/pentominoes-4x15.png

- 5x12: `1010 solutions
  <../solutions/ominoes/pentominoes-5x12.txt>`__

  .. image:: images/ominoes/pentominoes-5x12.png

- 6x10: `2339 solutions
  <../solutions/ominoes/pentominoes-6x10.txt>`__

  .. image:: images/ominoes/pentominoes-6x10.png


Skewed Rectangles
-----------------

- 20x3: `2 solutions
  <../solutions/ominoes/pentominoes-skewed-20x3.txt>`__

  .. image:: images/ominoes/pentominoes-skewed-20x3.png

  These are the same two solutions as the 3x20 rectangle above, just
  cut at the W pentomino and rearranged.

- 15x4: `138 solutions
  <../solutions/ominoes/pentominoes-skewed-15x4.txt>`__

  .. image:: images/ominoes/pentominoes-skewed-15x4.png

- 12x5: `233 solutions
  <../solutions/ominoes/pentominoes-skewed-12x5.txt>`__

  .. image:: images/ominoes/pentominoes-skewed-12x5.png

  This solution can be easily rearranged into a solution to the 5x12
  rectangle above, but not all solutions share this property.

- 10x6: `156 solutions
  <../solutions/ominoes/pentominoes-skewed-10x6.txt>`__

  .. image:: images/ominoes/pentominoes-skewed-10x6.png


Misc
----

* 3x20 ring (3x20 rectangle joined at the ends): 2 solutions
  (same as the 3x20 rectangle; the V piece forces a partition)

* 3x20 tube (3x20 rectangle joined at the long edges): `48,928
  solutions <../solutions/ominoes/pentominoes-3x20-tube.txt>`__ (at
  least, depending on how pieces that wrap around on themselves are
  defined)

* _`8x8 square with a central 2x2 hole`: `65 solutions
  <../solutions/ominoes/pentominoes-8x8.txt>`__

  .. image:: images/ominoes/pentominoes-8x8.png

* 8x8 square with missing corners: `2170 solutions
  <../solutions/ominoes/pentominoes-8x8-corners.txt>`__

  .. image:: images/ominoes/pentominoes-8x8-corners.png

* 8x8 squares with four holes:

  .. list-table::
     :class: borderless

     * - .. figure:: images/ominoes/pentominoes-8x8-four-holes-1.png

         `188 solutions <../solutions/ominoes/pentominoes-8x8-four-holes-1.txt>`__

       - .. figure:: images/ominoes/pentominoes-8x8-four-holes-2.png

         `21 solutions <../solutions/ominoes/pentominoes-8x8-four-holes-2.txt>`__

     * - .. figure:: images/ominoes/pentominoes-8x8-four-holes-3.png

         `126 solutions <../solutions/ominoes/pentominoes-8x8-four-holes-3.txt>`__

       - .. figure:: images/ominoes/pentominoes-8x8-four-holes-4.png

         `74 solutions <../solutions/ominoes/pentominoes-8x8-four-holes-4.txt>`__

* 3x21 rectangle with holes: `6 solutions
  <../solutions/ominoes/pentominoes-3x21.txt>`__ (an
  example puzzle from `How to Extend Polyform Puzzler <extend.html>`_)

  .. image:: images/ominoes/pentominoes-3x21.png

* 10x10 triangle with one omitted piece: `580 solutions
  <../solutions/ominoes/pentominoes-triangle.txt>`__

  Solutions are possible omitting all but the "P" & "W" pieces.  This
  solution omits the "V" piece (shown to the side):

  .. image:: images/ominoes/pentominoes-triangle.png

* 15x8 triangle: `8 solutions
  <../solutions/ominoes/pentominoes-triangle-2.txt>`__

  .. image:: images/ominoes/pentominoes-triangle-2.png

* Truncated triangle: `3626 solutions
  <../solutions/ominoes/pentominoes-truncated-triangle.txt>`__

  .. image:: images/ominoes/pentominoes-truncated-triangle.png

* 11x10 diamond: `8 solutions
  <../solutions/ominoes/pentominoes-diamond.txt>`__

  .. image:: images/ominoes/pentominoes-diamond.png

  (The configuration with a central hole has no solutions,
  unfortunately.  But see the diamond puzzle in `Pentominoes Plus the
  Monomino`_.)

* Trapezoid: `140 solutions
  <../solutions/ominoes/pentominoes-trapezoid.txt>`__

  .. image:: images/ominoes/pentominoes-trapezoid.png

* Chevrons:

  .. list-table::
     :class: borderless

     * - .. figure:: images/ominoes/pentominoes-chevron-1.png

         `101 solutions <../solutions/ominoes/pentominoes-chevron-1.txt>`__

       - .. figure:: images/ominoes/pentominoes-chevron-2.png

         `82 solutions <../solutions/ominoes/pentominoes-chevron-2.txt>`__


* Crosses:

  .. list-table::
     :class: borderless

     * - .. figure:: images/ominoes/pentominoes-cross-1.png

         `14 solutions <../solutions/ominoes/pentominoes-cross-1.txt>`__.
         Also see `Pentominoes Plus the Monomino`_, cross 1.

       - .. figure:: images/ominoes/pentominoes-cross-2.png

         `84 solutions <../solutions/ominoes/pentominoes-cross-2.txt>`__
         (design by Dan Klarskov)

     * - .. figure:: images/ominoes/pentominoes-cross-3.png

         `28 solutions <../solutions/ominoes/pentominoes-cross-3.txt>`__
         (design by Dan Klarskov)

       - .. figure:: images/ominoes/pentominoes-cross-4.png

         `21 solutions <../solutions/ominoes/pentominoes-cross-4.txt>`__

     * - .. figure:: images/ominoes/pentominoes-cross-5.png

         `4 solutions <../solutions/ominoes/pentominoes-cross-3.txt>`__

       - .. figure:: images/ominoes/pentominoes-cross-6.png

         `164 solutions <../solutions/ominoes/pentominoes-cross-6.txt>`__

* Flowers:

  .. list-table::
     :class: borderless

     * - .. figure:: images/ominoes/pentominoes-flower-1.png

         `47 solutions <../solutions/ominoes/pentominoes-flower-1.txt>`__
         (design by Dan Klarskov)

       - .. figure:: images/ominoes/pentominoes-flower-2.png

         `414 solutions <../solutions/ominoes/pentominoes-flower-2.txt>`__
         (design by Dan Klarskov)

     * - .. figure:: images/ominoes/pentominoes-flower-3.png

         `15 solutions <../solutions/ominoes/pentominoes-flower-3.txt>`__
         (design by Dan Klarskov)

       - .. figure:: images/ominoes/pentominoes-flower-4.png

         `57 solutions <../solutions/ominoes/pentominoes-flower-4.txt>`__
         (design by Dan Klarskov)

     * - .. figure:: images/ominoes/pentominoes-flower-5.png

         `1595 solutions <../solutions/ominoes/pentominoes-flower-5.txt>`__

       -

* ???The Eye???: `1 solution
  <../solutions/ominoes/pentominoes-eye.txt>`__ (design by Joel Enwald)

  .. image:: images/ominoes/pentominoes-eye.png

* Arches:

  .. list-table::
     :class: borderless

     * - .. figure:: images/ominoes/pentominoes-arch-1.png

         `602 solutions <../solutions/ominoes/pentominoes-arch-1.txt>`__

       - .. figure:: images/ominoes/pentominoes-arch-2.png

         `125 solutions <../solutions/ominoes/pentominoes-arch-2.txt>`__

     * - .. figure:: images/ominoes/pentominoes-arch-3.png

         `85 solutions <../solutions/ominoes/pentominoes-arch-3.txt>`__

       -

* Yin-Yang: `3 solutions
  <../solutions/ominoes/pentominoes-yin-yang.txt>`__

  .. image:: images/ominoes/pentominoes-yin-yang.png

* Holey oval: `2 solutions
  <../solutions/ominoes/pentominoes-holey-oval.txt>`__

  .. image:: images/ominoes/pentominoes-holey-oval.png

* Spinner (design from `Thimo Rosenkranz's pentoma.de
  <http://www.pentoma.de>`_): `13 solutions
  <../solutions/ominoes/ominoes/pentominoes-spinner-1.txt>`__

  .. image:: images/ominoes/pentominoes-spinner-1.png

* Holey spinner (design from John Greening): `3 solutions
  <../solutions/ominoes/ominoes/pentominoes-holey-spinner.txt>`__

  .. image:: images/ominoes/pentominoes-holey-spinner.png


Pentominoes Plus the Square Tetromino
=====================================

* 8x8 square: `16146 solutions
  <../solutions/ominoes/pentominoes-plus-square-tetromino-8x8.txt>`__

  .. image:: images/ominoes/pentominoes-plus-square-tetromino-8x8.png

  The `8x8 square with a central 2x2 hole`_ puzzle above can be
  considered a subset of this puzzle.

* 15x8 triangle: `473 solutions
  <../solutions/ominoes/pentominoes-plus-square-tetromino-triangle.txt>`__

  .. image:: images/ominoes/pentominoes-plus-square-tetromino-triangle.png

* Crosses

  .. list-table::
     :class: borderless

     * - .. figure:: images/ominoes/pentominoes-plus-square-tetromino-cross-1.png

         `5380 solutions
         <../solutions/ominoes/pentominoes-plus-square-tetromino-cross-1.txt>`__
         (design by Dan Klarskov)

       - .. figure:: images/ominoes/pentominoes-plus-square-tetromino-cross-2.png

         `2071 solutions
         <../solutions/ominoes/pentominoes-plus-square-tetromino-cross-2.txt>`__
         (design by Dan Klarskov)

     * - .. figure:: images/ominoes/pentominoes-plus-square-tetromino-cross-3.png

         `177 solutions
         <../solutions/ominoes/pentominoes-plus-square-tetromino-cross-3.txt>`__
         (design by Dan Klarskov)

       - .. figure:: images/ominoes/pentominoes-plus-square-tetromino-cross-4.png

         `2 solutions
         <../solutions/ominoes/pentominoes-plus-square-tetromino-cross-4.txt>`__
         (design by Dan Klarskov)

* Diamond: `22 solutions
  <../solutions/ominoes/pentominoes-plus-square-tetromino-diamond-1.txt>`__

  .. image:: images/ominoes/pentominoes-plus-square-tetromino-diamond-1.png

  (The symmetrical configuration with a central hole has no solutions,
  unfortunately.)


Pentominoes Plus the Monomino
=============================

* Cross 1 (suggested by Dan Klarskov): `366 solutions
  <../solutions/ominoes/pentominoes-plus-monomino-cross-1.txt>`__

  .. image:: images/ominoes/pentominoes-plus-monomino-cross-1.png

* Diamond: `10 solutions
  <../solutions/ominoes/pentominoes-plus-monomino-diamond.txt>`__

  .. image:: images/ominoes/pentominoes-plus-monomino-diamond.png

  In all solutions the monomino is at the edge of the diamond.


One-Sided Pentominoes
=====================

These are just like regular pentominoes, except that non-isomorphic
reflections (different shape when flipped over) are treated as
separate pieces, and pieces are not allowed to be flipped.


Rectangles
----------

- 3x30: `46 solutions
  <../solutions/ominoes/one-sided-pentominoes-3x30.txt>`__

  .. image:: images/ominoes/one-sided-pentominoes-3x30.png

- 5x18: 686,628 solutions (`incomplete list
  <../solutions/ominoes/one-sided-pentominoes-5x18.txt>`__)

  .. image:: images/ominoes/one-sided-pentominoes-5x18.png

- 6x15: 2,567,183 solutions (`incomplete list
  <../solutions/ominoes/one-sided-pentominoes-6x15.txt>`__)

  .. image:: images/ominoes/one-sided-pentominoes-6x15.png

- 9x10: 10,440,433 solutions (`incomplete list
  <../solutions/ominoes/one-sided-pentominoes-9x10.txt>`__)

  .. image:: images/ominoes/one-sided-pentominoes-9x10.png

  10,440,433 solutions (non-isomorphic in reflection, reflections
  allowed when counting solutions) are reported in "One-sided
  Pentominoes in a 9 x 10 Rectangle" by `Alfred Wassermann`_,
  University of Bayreuth, 2000.

  .. _Alfred Wassermann:
     http://did.mat.uni-bayreuth.de/~alfred/home/index.html

The numbers of solutions for the last three puzzles above were taken
from `Gerard Putter's Polyomino Solution Page`__, as reported by
Stephen Montgomery-Smith.

__ http://www.xs4all.nl/~gp/PolyominoSolver/Polyomino.html


.. |c| unicode:: U+00A9 .. copyright sign
