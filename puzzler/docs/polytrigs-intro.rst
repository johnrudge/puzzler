.. -*- coding: utf-8 -*-

===========================================================
 An Introduction to Polytrigs (Triangular-Grid Polysticks)
===========================================================

:Author: David Goodger <goodger@python.org>
:Date: $Date$
:Revision: $Revision$
:Web site: http://puzzler.sourceforge.net/
:Copyright: |c| 1998-2015 by David J. Goodger
:License: `GPL 2 <../COPYING.html>`__

.. image:: images/puzzler.png
   :align: center

.. sidebar:: Also see:

   * `Polytrigs: Puzzles & Solutions <polytrigs.html>`_
   * `Notes on Polytrigs <polytrig-notes.html>`_
   * `Polysticks: Puzzles & Solutions <polysticks.html>`_
   * `An Introduction to Polysticks <polysticks-intro.html>`_
   * `Polytwigs (Hexagonal-Grid Polysticks): Puzzles & Solutions <polytwigs.html>`_
   * `An Introduction to Polytwigs (Hexagonal-Grid Polysticks) <polytwigs-intro.html>`_
   * `Polyform Puzzler: Puzzles & Solutions <puzzles.html>`_
   * `Polyform Puzzler FAQ <FAQ.html>`_
     (`polyform details <FAQ.html#what-polyforms-are-there>`__,
     `numbers of polyforms <FAQ.html#how-many-of-each-type-of-polyform-are-there>`__,
     `interpreting solution files <FAQ.html#how-should-polytrig-solution-files-be-interpreted>`__)

.. contents::

**Polytrigs** are polyforms constructed from unit line segments (edges)
joined end-to-end on a regular triangular grid, also known as
"triangular-grid polysticks" or "triangular polysticks".

Here is a puzzle containing all the polytrigs of order 1 through 3:

.. image:: images/trigs/polytrigs-123-trapezoid-5x4.png

See `Polytrigs: Puzzles & Solutions`_ for many more puzzles.

The name "trig" comes from "TRIangular Grid"; a neologism I invented
because "triangular-grid polysticks" is too unwieldy, especially when
combined with order-prefixes (mono-, di-, tri-, tetra-, etc.;
"triangular-grid tristicks"!?).  I hope the name catches on.

The polytrigs can be thought of as the projective duals of polyhexes.
Most of the polytrigs of order N can be derived from the polyhexes of
order N+1 (i.e., joining the centers of the hexagons of a tetrahex
results in a tritrig).  The exceptions are the polytrigs with loops
(e.g. the "O04" tetratrig), which are duals of the same order or
lower-order polyhexes.

Hopefully these puzzles will begin to fill this particular gap in the
polyform puzzle branch of recreational mathematics.


Prior Research
==============

    If the square polysticks don't get the respect they deserve, this
    is doubly true for the triangular polysticks.

    -- Alexandre Owen Mu??iz, `Puzzle Zapper Blog
       <http://puzzlezapper.com/blog/2010/12/polysticks-on-a-regular-spanning-subgraph/>`__

Brief mention of triangular-grid polysticks is made on the `Wolfram
Mathworld page on Polysticks`__, in Alexandre Owen Mu??iz's blog above,
as well as in Livio Zucca's work (the original site is gone, `but a
mirror exists`__).

__ http://mathworld.wolfram.com/Polystick.html
__ http://www.iread.it/lz/index.html

In January 2012 I received email from Leslie E. Shader (Ph.D.,
Professor Emeritus, Mathematics, University of Wyoming), who shared
the results of his unpublished work on triangular-grid polysticks from
around 1993.

Colin F. Brown, in addition to his work on `polytwigs (hexagonal-grid
polysticks)`__, has also done some work on the quasi-polytrigs; see
"`Quasi-Polyforms`_" below.

__ polytwigs-intro.html

At the Gathering for Gardner 10 (G4G10, 2012), Les Shader gave me a
copy of his gift exchange paper from the Gathering for Gardner 2 or 3
(1996 or 1998), reproduced below, with permission.

If you know of any other work on this type of puzzle, please let me
know!


3-Trees and a Triangle
----------------------

by Leslie E. Shader, Ph.D.

*[A paper from the Gathering for Gardner 2 or 3 (1996 or 1998).]*

In a paper, ???Polysticks???, J. Recreatinal Mathematics, vol. 22(3) 1990,
Brian Barwell introduced a new type of puzzle.  Instead of tiling a
region in the plane or packing a region in 3-space, Barwell considered
a rectangular lattice (graph paper) and used ???Polysticks??? to cover
certain subsets of the lattice.  There has also been a puzzle called
???845???, I believe produced by International Puzzles and Games in
Taiwan.  This used 10 polysticks each with 4 unit lengths.  (A
polystick of length n, is a set of n unit segments joined at the ends
at an angle of 90, 180, or 270 degrees.)  The ???845??? puzzle did not
allow the pieces to cross.

For ???3-Trees and a Triangle??? we will use 3 unit lengths joined at the
ends at angles of 60, 120, 180, 240, or 300 degrees.  There are
exactly 12 such pieces.  In the language of mathematics (graph
theory), each of the pieces is either a ???tree??? or a ???triangle???.
Actually we should say Euclidean Tree since angles as well as length
are important.  Since we wish a physical model of this puzzle we will
not allow crossings.  The pieces may be rotated or turned over.

The pieces are: [sketch of the 12 tritrigs_, which see]

I am including with my submission, a list of more than 300 different
lattices that can be covered by subsets of the set of all pieces
above.  I also have included a set of solutions for each of these.
But the solutions are sealed!  Please try some of the puzzles before
looking at the solutions.  I have included a smaller set of my
favorite puzzles.  Those puzzles with 6 or fewer pieces are relatively
easy.  I classify the puzzles using 7-9 pieces as [moderately]
difficult, and if the puzzle requires 10-12 pieces the puzzle is
difficult.  Some of the 10-12 pieces have taken me up to 20 hours to
solve by hand.  Of course, I didn???t now if a solution existed or not,
which means an exhaustive search had to be done.  Within the sealed
envelope marked ???solutions???, there is also a set of six puzzles that
cannot be solved.  I am sure there are other interesting puzzles that
I have not included inthe set that I am submitting to you.

Some thoughts on the technical aspects of the puzzles.  I think that
the unit length should be either 7/8 in. or 1 in., the individual
pieces should be injection molded with width 1/8 in and 1/2 in. deep.
Care must be given to fit at the vertices where more than 1 piece come
together.  Several rough sketches are included.  I prefer rounded
corners to sharp corners.  A universal base can also be injection
molded and should be large enough to make most of the puzzles I have
included.  There should be raised traingles (corners rounded) to hold
the pieces in position.  The ???845??? puzzle used circles but I think the
triangles would be better.

Finally, although the use of the trees and triangle looks entirely
new, the pieces can be ???fleshed out??? allowing an isoceles triangle,
base angle 30 degrees, to ???grow??? on each edge.  I have included a page
with two examples.  Actually, we are now very close to Damert???s ???Bees???
puzzle except that crossings are still not allowed.  Perhaps the idea
of joining pieces at the vertex and not the edge (two dimensional) or
at an edge and not a face (three dimensional) is an idea whose time
has come.  Have you seen the Rubik???s Blocks puzzle?


Polyforms
=========

The number and names of the various orders of polytrigs are as follows:

=====  ==========  ===========  ===========
Order  | Polyform  | Free       | One-Sided
       | Name      | Polytrigs  | Polytrigs
=====  ==========  ===========  ===========
1      monotrig    1            1
2      ditrigs     3            3
3      tritrigs    12           19
4*     tetratrigs  60           104
5*     pentatrigs  375          719
6*     hexatrigs   2613         5123
=====  ==========  ===========  ===========

"*" above means that forms with enclosed holes exist.

The numbers of polytrigs can also be found in the following sequences
from `The On-Line Encyclopedia of Integer Sequences
<http://oeis.org>`_: A159867_ (free) and A151539_ (one-sided).

.. _A159867: http://oeis.org/A159867
.. _A151539: http://oeis.org/A151539

Examples of the polytrigs from order 1 (monotrig) to order 4
(tetratrigs) are given in the tables below.

The polytrigs are named with a letter-number scheme, like "I1", "C3",
and "R14".  The initial letter is the letter of the alphabet that the
polytrig most closely resembles.  In some cases, that resemblance is
weak, and the letters are arbitrary.  The final digit of the number
represents the polyform order (how many line segments are in the
polytrig).  There are more tetratrigs than letters in the alphabet, so
their names have an extra middle digit (numbered from 0) to
differentiate the variations.

.. _table legend:

In the tables below, "Aspects" refers to the number of unique
orientations that a polyform may take (different rotations, flipped or
not).  This varies with the symmetry of the polyform.

The "One-Sided" column identifies polyforms that are asymmetrical in
reflection.  Treating the flipped and unflipped versions of
asymmetrical polytrigs as distinct polyforms (and disallowing further
reflection or "flipping"), results in "one-sided" polytrigs and
puzzles.


Monotrig
--------

There is only one monotrig (order-1 polytrig):

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - I1
     - .. image:: images/pieces/polytrigs/I1.png
     - 3
     -


Ditrigs
-------

There are 3 ditrigs (order-2 polytrigs):

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - I2
     - .. image:: images/pieces/polytrigs/I2.png
     - 3
     -

   * - L2
     - .. image:: images/pieces/polytrigs/L2.png
     - 6
     -

   * - V2
     - .. image:: images/pieces/polytrigs/V2.png
     - 6
     -


Tritrigs
--------

There are 12 free tritrigs (order-3 polytrigs) and 19 one-sided tritrigs:

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - C3
     - .. image:: images/pieces/polytrigs/C3.png
     - 6
     -

   * - E3
     - .. image:: images/pieces/polytrigs/E3.png
     - 6
     -

   * - I3
     - .. image:: images/pieces/polytrigs/I3.png
     - 3
     -

   * - J3
     - .. image:: images/pieces/polytrigs/J3.png
     - 12
     - yes

   * - L3
     - .. image:: images/pieces/polytrigs/L3.png
     - 12
     - yes

   * - O3
     - .. image:: images/pieces/polytrigs/O3.png
     - 2
     -

   * - P3
     - .. image:: images/pieces/polytrigs/P3.png
     - 12
     - yes

   * - S3
     - .. image:: images/pieces/polytrigs/S3.png
     - 6
     - yes

   * - T3
     - .. image:: images/pieces/polytrigs/T3.png
     - 12
     - yes

   * - U3
     - .. image:: images/pieces/polytrigs/U3.png
     - 12
     - yes

   * - Y3
     - .. image:: images/pieces/polytrigs/Y3.png
     - 2
     -

   * - Z3
     - .. image:: images/pieces/polytrigs/Z3.png
     - 6
     - yes


Tetratrigs
----------

There are 60 free tetratrigs (order-4 polytrigs) and 104 one-sided
tetratrigs:

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - B04
     - .. image:: images/pieces/polytrigs/B04.png
     - 12
     - yes

   * - B14
     - .. image:: images/pieces/polytrigs/B14.png
     - 12
     - yes

   * - C04
     - .. image:: images/pieces/polytrigs/C04.png
     - 6
     -

   * - D04
     - .. image:: images/pieces/polytrigs/D04.png
     - 12
     - yes

   * - E04
     - .. image:: images/pieces/polytrigs/E04.png
     - 12
     - yes

   * - E14
     - .. image:: images/pieces/polytrigs/E14.png
     - 6
     -

   * - E24
     - .. image:: images/pieces/polytrigs/E24.png
     - 12
     - yes

   * - E34
     - .. image:: images/pieces/polytrigs/E34.png
     - 12
     - yes

   * - F04
     - .. image:: images/pieces/polytrigs/F04.png
     - 12
     - yes

   * - F14
     - .. image:: images/pieces/polytrigs/F14.png
     - 12
     - yes

   * - F24
     - .. image:: images/pieces/polytrigs/F24.png
     - 12
     - yes

   * - F34
     - .. image:: images/pieces/polytrigs/F34.png
     - 12
     - yes

   * - H04
     - .. image:: images/pieces/polytrigs/H04.png
     - 12
     - yes

   * - H14
     - .. image:: images/pieces/polytrigs/H14.png
     - 12
     - yes

   * - H24
     - .. image:: images/pieces/polytrigs/H24.png
     - 12
     - yes

   * - H34
     - .. image:: images/pieces/polytrigs/H34.png
     - 12
     - yes

   * - I04
     - .. image:: images/pieces/polytrigs/I04.png
     - 3
     -

   * - J04
     - .. image:: images/pieces/polytrigs/J04.png
     - 12
     - yes

   * - J14
     - .. image:: images/pieces/polytrigs/J14.png
     - 12
     - yes

   * - J24
     - .. image:: images/pieces/polytrigs/J24.png
     - 12
     - yes

   * - J34
     - .. image:: images/pieces/polytrigs/J34.png
     - 12
     - yes

   * - K04
     - .. image:: images/pieces/polytrigs/K04.png
     - 6
     -

   * - L04
     - .. image:: images/pieces/polytrigs/L04.png
     - 12
     - yes

   * - M04
     - .. image:: images/pieces/polytrigs/M04.png
     - 6
     -

   * - N04
     - .. image:: images/pieces/polytrigs/N04.png
     - 12
     - yes

   * - N14
     - .. image:: images/pieces/polytrigs/N14.png
     - 12
     - yes

   * - O04
     - .. image:: images/pieces/polytrigs/O04.png
     - 3
     -

   * - P04
     - .. image:: images/pieces/polytrigs/P04.png
     - 12
     - yes

   * - P14
     - .. image:: images/pieces/polytrigs/P14.png
     - 12
     - yes

   * - P24
     - .. image:: images/pieces/polytrigs/P24.png
     - 12
     - yes

   * - P34
     - .. image:: images/pieces/polytrigs/P34.png
     - 12
     - yes

   * - Q04
     - .. image:: images/pieces/polytrigs/Q04.png
     - 12
     - yes

   * - Q14
     - .. image:: images/pieces/polytrigs/Q14.png
     - 12
     - yes

   * - R04
     - .. image:: images/pieces/polytrigs/R04.png
     - 12
     - yes

   * - R14
     - .. image:: images/pieces/polytrigs/R14.png
     - 12
     - yes

   * - R24
     - .. image:: images/pieces/polytrigs/R24.png
     - 12
     - yes

   * - R34
     - .. image:: images/pieces/polytrigs/R34.png
     - 12
     - yes

   * - S04
     - .. image:: images/pieces/polytrigs/S04.png
     - 6
     - yes

   * - S14
     - .. image:: images/pieces/polytrigs/S14.png
     - 12
     - yes

   * - S24
     - .. image:: images/pieces/polytrigs/S24.png
     - 12
     - yes

   * - S34
     - .. image:: images/pieces/polytrigs/S34.png
     - 12
     - yes

   * - S44
     - .. image:: images/pieces/polytrigs/S44.png
     - 12
     - yes

   * - T04
     - .. image:: images/pieces/polytrigs/T04.png
     - 12
     - yes

   * - T14
     - .. image:: images/pieces/polytrigs/T14.png
     - 6
     -

   * - T24
     - .. image:: images/pieces/polytrigs/T24.png
     - 12
     - yes

   * - U04
     - .. image:: images/pieces/polytrigs/U04.png
     - 12
     - yes

   * - U14
     - .. image:: images/pieces/polytrigs/U14.png
     - 6
     -

   * - U24
     - .. image:: images/pieces/polytrigs/U24.png
     - 6
     -

   * - V04
     - .. image:: images/pieces/polytrigs/V04.png
     - 6
     -

   * - V14
     - .. image:: images/pieces/polytrigs/V14.png
     - 6
     -

   * - V24
     - .. image:: images/pieces/polytrigs/V24.png
     - 6
     -

   * - W04
     - .. image:: images/pieces/polytrigs/W04.png
     - 6
     -

   * - W14
     - .. image:: images/pieces/polytrigs/W14.png
     - 6
     -

   * - W24
     - .. image:: images/pieces/polytrigs/W24.png
     - 12
     - yes

   * - X04
     - .. image:: images/pieces/polytrigs/X04.png
     - 3
     -

   * - Y04
     - .. image:: images/pieces/polytrigs/Y04.png
     - 6
     -

   * - Y14
     - .. image:: images/pieces/polytrigs/Y14.png
     - 12
     - yes

   * - Y24
     - .. image:: images/pieces/polytrigs/Y24.png
     - 12
     - yes

   * - Y34
     - .. image:: images/pieces/polytrigs/Y34.png
     - 12
     - yes

   * - Z04
     - .. image:: images/pieces/polytrigs/Z04.png
     - 6
     - yes


Quasi-Polyforms
===============

Quasi-polyforms are polyforms where the requirement that all unit
shapes be connected has been removed.  In other words, quasi-polyforms
are polyforms where some or all unit shapes may be separate from the
others.

Without limits on the distance between unit shapes there would be an
infinite number of quasi-polyforms (for orders 2 and above).  We will
limit the quasi-polyforms we consider to those with length-1 gaps
between segments.

The number and names of the various orders of quasi-polytrigs are as
follows:

=====  ================  ===========  ===========
Order  | Polyform        | Free       | One-Sided
       | Name            | Polytrigs  | Polytrigs
=====  ================  ===========  ===========
1      monotrig [*]_     1            1
2      quasi-ditrig      9            13
3      quasi-tritrigs    140          259
4      quasi-tetratrigs  3377         6639          
=====  ================  ===========  ===========

.. [*] With only 1 line segment, there can be no disconnected
       quasi-monotrig.  The set of the regular (fully-connected)
       monotrigs is identical to the set of quasi-monotrigs, and
       consists of one piece: the "I1" monotrig.

Examples of the quasi-polytrigs of order 2 (quasi-ditrigs) are given
in the table below.  See the `table legend`_ above for column
descriptions.


Quasi-Ditrigs
-------------

There are 9 free quasi-ditrigs (order-2 quasi-polytrigs) and 13
one-sided quasi-ditrigs:

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - C12
     - .. image:: images/pieces/quasi-polytrigs/C12.png
     - 6
     -

   * - I02
     - .. image:: images/pieces/quasi-polytrigs/I02.png
     - 3
     -

   * - I12
     - .. image:: images/pieces/quasi-polytrigs/I12.png
     - 3
     -

   * - L02
     - .. image:: images/pieces/quasi-polytrigs/L02.png
     - 6
     -

   * - L12
     - .. image:: images/pieces/quasi-polytrigs/L12.png
     - 12
     - yes

   * - P12
     - .. image:: images/pieces/quasi-polytrigs/P12.png
     - 12
     - yes

   * - S12
     - .. image:: images/pieces/quasi-polytrigs/S12.png
     - 6
     - yes

   * - V02
     - .. image:: images/pieces/quasi-polytrigs/V02.png
     - 6
     -

   * - Z12
     - .. image:: images/pieces/quasi-polytrigs/Z12.png
     - 6
     - yes


Coordinate System
=================

Polytrig puzzles use a pseudo-3D skewed coordinate system, where the X
and Y axes are 60?? apart instead of the usual 90??.  The typical
representation (as seen in the Polyform Puzzler solution data files)
positions the X axis horizontally with the Y axis 30?? clockwise from
vertical.

The (X,Y) 2-dimensional coordinate identifies the lower-left corner of
the (X,Y,0) triangle in a polyiamond grid.  The first three line
segments emanating from this point share the (X,Y) coordinate, and the
Z dimension is used for the direction of the line segment:

| z = 0: 0?? horizontal, to the right;
| z = 1: 60?? counter-clockwise, up and to the right;
| z = 2: 120?? counter-clockwise, up and to the left.


Intersections
-------------

As there is the possibility for polytrigs to cross each other at any
(X,Y) intersection, the solution algorithm needs to prevent such
crossings.  Unlike with polysticks, the intersections are not simple
(either used or available); multiple polyforms can use an intersection
simultaneously.

In the puzzle matrix, we represent contstraints on intersections via
up to 6 additional columns per intersection [*]_, in the form i(X,Y,Z)
(or "X,Y,Zi").  This means that the segment in direction Z cannot go
through the intersection, (X,Y).  These are the Z directions::

      2    1
       \  /
    3___\/___0
        /\
       /  \
      4    5

.. [*] Possibly fewer columns for intersections at the edge of a
   puzzle shape.  This represents a possible future optimization.

   Note that since there are already 3 line segments originating at
   each intersection, the cost of intersection constraints is 2 per
   segment, which effectively multiplies the number of coordinate
   columns by 3.  Polytrig puzzle matrixes 

These intersection constraints are secondary columns, meaning that at
most one polyform may use or fill a column.  Unlike primary columns,
secondary columns may remain unused/unfilled.

For each polyform, we check the angle between each pair of line
segments.  Both ends of each segment must be checked, but only in one
direction (counter-clockwise) to avoid duplication.  For any two line
segments, there are six possibilities::

      B  / A
    ____/___     D ____    E ____    F ____
                  /          \
        C        /  D'        \

* A: 60?? (adjacent) -- no constraints are added.

* B: 120?? (one-gapper) -- 3 constraints are added: the 2 line segments
  themselves (e.g. Z={1,3}), plus the gap in-between (e.g. Z=2).

* C: 180?? (two-gapper) -- 4 constraints are added: the 2 line segments
  (e.g. Z={3,0}), plus the two gaps (e.g. Z={4,5}).  Note that the
  gaps on the opposite side will be added when the other line segment
  is checked.

* D: 240?? (three-gapper) -- no constraints are added.  However, D' is
  a case of a 120?? one-gapper (case B).

* E: 300?? (four-gapper) -- no constraints are added.

* F: 360?? (five-gapper or stub; only one segment involved) -- no
  constraints are added.

Only cases B & C require constraints.

If an intersection constraint is already used (or otherwise
unavailable), no other polyform with the same contstraint may be
placed in the puzzle solution.

.. !!! Add example?


.. |c| unicode:: U+00A9 .. copyright sign
