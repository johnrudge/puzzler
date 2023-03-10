.. -*- coding: utf-8 -*-

===============================
 An Introduction to Polysticks
===============================

:Author: David Goodger <goodger@python.org>
:Date: $Date$
:Revision: $Revision$
:Web site: http://puzzler.sourceforge.net/
:Copyright: |c| 1998-2015 by David J. Goodger
:License: `GPL 2 <../COPYING.html>`__

.. image:: images/puzzler.png
   :align: center

.. sidebar:: Also see:

   * `Polysticks: Puzzles & Solutions <polysticks.html>`_
   * `Notes on Polysticks <polystick-notes.html>`_
   * `Polytrigs (Triangular-Grid Polysticks): Puzzles & Solutions <polytrigs.html>`_
   * `An Introduction to Polytrigs (Triangular-Grid Polysticks) <polytwigs-intro.html>`_
   * `Polytwigs (Hexagonal-Grid Polysticks): Puzzles & Solutions <polytwigs.html>`_
   * `An Introduction to Polytwigs (Hexagonal-Grid Polysticks) <polytwigs-intro.html>`_
   * `Polyform Puzzler: Puzzles & Solutions <puzzles.html>`_
   * `Polyform Puzzler FAQ <FAQ.html>`_
     (`polyform details <FAQ.html#what-polyforms-are-there>`__,
     `numbers of polyforms <FAQ.html#how-many-of-each-type-of-polyform-are-there>`__,
     `interpreting solution files <FAQ.html#how-should-polystick-solution-files-be-interpreted>`__)

.. contents::

**Polysticks** are polyforms constructed from unit line segments
(edges) joined end-to-end on a regular square grid.  Polysticks were
named by and seem to have been first formally expolored by Brian
R. Barwell [#barwell]_.

Here is a puzzle containing all the polysticks of order 1 through 4:

.. image:: images/sticks/polysticks-1234-3x7-diamond-lattice.png

See `Polysticks: Puzzles & Solutions`_ for many more puzzles.

The polysticks can be thought of as the projective duals of
polyominoes.  Most of the polysticks of order N can be derived from
the polyominoes of order N+1 (i.e., joining the centers of the squares
of a pentomino results in a tetrastick).  The exceptions are the
polysticks with loops (e.g. the "O" tetrastick), which are duals of
the same order or lower-order polyominoes.  Also, it is not a
one-to-one mapping.  For example, the P pentomino can be mapped to
four different tetrasticks, the F, H, J, and P (depending on which
loop segment of the full "P" pentastick is left out).

During a visit to India in 2010, it was pointed out to me that
polystick puzzles look a lot like some of `the "kolam" sand/chalk
drawings`__ that can be seen on sidewalks and patios outside of homes.
These drawings are thought to bestow prosperity to homes.

__ http://en.wikipedia.org/wiki/Kolam

.. [#barwell] Brian R. Barwell, "Polysticks," `Journal of Recreational
   Mathematics` volume 22 issue 3 (1990), p.165-175


Polyforms
=========

The number and names of the various orders of polysticks are as
follows:

=====  ===========  ============  ============
Order  | Polyform   | Free        | One-Sided
       | Name       | Polysticks  | Polysticks
=====  ===========  ============  ============
1      monostick    1             1
2      distick      2             2
3      tristick     5             7
4      tetrastick   16            25
5      pentastick   55            99
6*     hexastick    222           416
7*     heptastick   950           1854
=====  ===========  ============  ============

"*" above means that forms with enclosed holes exist.

The numbers of polysticks can also be found in the following sequences
from `The On-Line Encyclopedia of Integer Sequences
<http://oeis.org>`_: A019988_ (free) and A151537_ (one-sided).

.. _A019988: http://oeis.org/A019988
.. _A151537: http://oeis.org/A151537

Examples of the polysticks from order 1 (monostick) to order 4
(tetrasticks) are given in the tables below.

The polysticks (other than the tetrasticks) are named with a
letter-number scheme, like "I1" and "L3".  The initial letter is the
letter of the alphabet that the polystick most closely resembles.  In
some cases, that resemblance is weak, and the letters are arbitrary.
The number represents the polyform order (how many line segments are
in the polystick).  The tetrasticks have established letter-only
names.

In the tables below, "Aspects" refers to the number of unique
orientations that a polyform may take (different rotations, flipped or
not).  This varies with the symmetry of the polyform.

The "One-Sided" column identifies polyforms that are asymmetrical in
reflection.  Treating the flipped and unflipped versions of
asymmetrical polysticks as distinct polyforms (and disallowing further
reflection or "flipping"), results in "one-sided" polysticks and
puzzles.

The "Welded" column identifies polyforms that contain junction points
or branches (they cannot be formed by simple bending).


Monostick
---------

There is only one monostick (order-1 polystick):

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Welded

   * - I1
     - .. image:: images/pieces/polysticks/I1.png
     - 2
     -
     -


Disticks
--------

There are 2 disticks (order-2 polysticks):

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Welded

   * - I2
     - .. image:: images/pieces/polysticks/I2.png
     - 2
     -
     -

   * - V2
     - .. image:: images/pieces/polysticks/V2.png
     - 4
     -
     -


Tristicks
---------

There are 5 free tristicks (order-3 polysticks) and 7 one-sided tristicks:

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Welded

   * - I3
     - .. image:: images/pieces/polysticks/I3.png
     - 2
     -
     -

   * - L3
     - .. image:: images/pieces/polysticks/L3.png
     - 8
     - yes
     -

   * - T3
     - .. image:: images/pieces/polysticks/T3.png
     - 8
     - 
     - yes

   * - U3
     - .. image:: images/pieces/polysticks/U3.png
     - 4
     -
     -

   * - Z3
     - .. image:: images/pieces/polysticks/Z3.png
     - 4
     - yes
     -


Tetrasticks
-----------

There are 16 free tetrasticks (order-4 polysticks) and 25 one-sided
tetrasticks:

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Welded

   * - F
     - .. image:: images/pieces/polysticks/F.png
     - 8
     - yes
     - yes

   * - H
     - .. image:: images/pieces/polysticks/H.png
     - 8
     - yes
     - yes

   * - I
     - .. image:: images/pieces/polysticks/I.png
     - 2
     -
     -

   * - J
     - .. image:: images/pieces/polysticks/J.png
     - 8
     - yes
     -

   * - L
     - .. image:: images/pieces/polysticks/L.png
     - 8
     - yes
     -

   * - N
     - .. image:: images/pieces/polysticks/N.png
     - 8
     - yes
     -

   * - O
     - .. image:: images/pieces/polysticks/O.png
     - 1
     -
     - ?

   * - P
     - .. image:: images/pieces/polysticks/P.png
     - 8
     - yes
     -

   * - R
     - .. image:: images/pieces/polysticks/R.png
     - 8
     - yes
     - yes

   * - T
     - .. image:: images/pieces/polysticks/T.png
     - 4
     -
     - yes

   * - U
     - .. image:: images/pieces/polysticks/U.png
     - 4
     -
     -

   * - V
     - .. image:: images/pieces/polysticks/V.png
     - 4
     -
     -

   * - W
     - .. image:: images/pieces/polysticks/W.png
     - 4
     -
     -

   * - X
     - .. image:: images/pieces/polysticks/X.png
     - 1
     -
     - yes

   * - Y
     - .. image:: images/pieces/polysticks/Y.png
     - 8
     - yes
     - yes

   * - Z
     - .. image:: images/pieces/polysticks/Z.png
     - 4
     - yes
     -


Seven-Segment Digits
--------------------

These pieces correspond to the seven-segment display decimal digits 0
through 9, as seen on digital watches, for a total of 49 line
segments.  Based on the "Digigrams" puzzle (AKA "Count On Me" or
"Count Me In") by Martin H. Watson. The 0/zero digit must have a gap
in one side to allow the central segment to be occupied (by a 1 or a 7
only). The 2 and 5 digits are identical (through reflection), and the
6 and 9 are identical (through rotation). The pieces comprise one
distick (digit 1), one tristick (digit 7), one tetrastick (digit 4),
three pentasticks (digits 2, 3, & 5), three hexasticks (digits 0, 6, &
9), and one heptastick (digit 8).

.. list-table::
   :widths: 20 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided
     - Welded

   * - d0
     - .. image:: images/pieces/polysticks/d0.png
     - 2
     -
     -

   * - d1
     - .. image:: images/pieces/polysticks/d1.png
     - 2
     -
     -

   * - d2
     - .. image:: images/pieces/polysticks/d2.png
     - 4
     - yes
     -

   * - d3
     - .. image:: images/pieces/polysticks/d3.png
     - 4
     -
     - yes

   * - d4
     - .. image:: images/pieces/polysticks/d4.png
     - 8
     - yes
     - yes

   * - d5
     - .. image:: images/pieces/polysticks/d5.png
     - 4
     - yes
     -

   * - d6
     - .. image:: images/pieces/polysticks/d6.png
     - 8
     - yes
     - yes

   * - d7
     - .. image:: images/pieces/polysticks/d7.png
     - 8
     - yes
     -

   * - d8
     - .. image:: images/pieces/polysticks/d8.png
     - 2
     -
     - yes

   * - d9
     - .. image:: images/pieces/polysticks/d9.png
     - 8
     - yes
     - yes


Coordinate System
=================

Polystick puzzles use a pseudo-3D coordinate system.  The (X,Y)
2-dimensional coordinate identifies the lower-left corner of the
(X,Y,0) square in a polyomino grid.  The Z dimension is used for the
direction of the line segment:

| z = 0: 0?? horizontal, to the right;
| z = 1: 90?? counter-clockwise, up.


Intersections
-------------

As there is the possibility for polysticks to cross each other at any
(X,Y) intersection, the solution algorithm needs to prevent such
crossings.  The intersections are simple, either used (by a
straight-through piece) or available.

In the puzzle matrix, we represent contstraints on intersections via
an additional column per intersection [*]_, in the form i(X,Y,Z) (or
"X,Yi").

.. [*] Intersections at the edge of a puzzle shape may be ignored.
   This represents a possible future optimization.

These intersection constraints are secondary columns, meaning that at
most one polyform may use or fill a column.  Unlike primary columns,
secondary columns may remain unused/unfilled.

If an intersection constraint is already used (or otherwise
unavailable), no other polyform with the same contstraint may be
placed in the puzzle solution.  This prevents two polysticks from
crossing each other.

.. !!! Add example?


.. |c| unicode:: U+00A9 .. copyright sign
