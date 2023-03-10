.. -*- coding: utf-8 -*-

==============================
 An Introduction to Polyhexes
==============================

:Author: David Goodger <goodger@python.org>
:Date: $Date$
:Revision: $Revision$
:Web site: http://puzzler.sourceforge.net/
:Copyright: |c| 1998-2015 by David J. Goodger
:License: `GPL 2 <../COPYING.html>`__

.. image:: images/puzzler.png
   :align: center

.. sidebar:: Also see:

   * `Polyhexes: Puzzles & Solutions <polyhexes.html>`_
   * `Pentahexes: Puzzles & Solutions <pentahexes.html>`_
   * `Notes on Polyhexes <polyhex-notes.html>`_
   * `Polyform Puzzler: Puzzles & Solutions <puzzles.html>`_
   * `Polyform Puzzler FAQ <FAQ.html>`_
     (`polyform details <FAQ.html#what-polyforms-are-there>`__,
     `numbers of polyforms <FAQ.html#how-many-of-each-type-of-polyform-are-there>`__,
     `interpreting solution files <FAQ.html#how-should-polyhex-solution-files-be-interpreted>`__)

.. contents::

**Polyhexes** are polyforms constructed from unit hexagons joined
edge-to-edge on a regular hexagonal grid (a honeycomb grid).

Here is a puzzle containing all the polyhexes of order 1 through 5:

.. image:: images/hexes/polyhexes-12345-triangle.png

See `Polyhexes: Puzzles & Solutions`_ and `Pentahexes: Puzzles &
Solutions`_ for many more puzzles.


Polyforms
=========

The number and names of the various orders of polyhexes are as follows:

=====  ==========  ===========  ===========
Order  | Polyform  | Free       | One-Sided
       | Name      | Polyhexes  | Polyhexes
=====  ==========  ===========  ===========
1      monohex     1            1
2      dihex       1            1
3      trihexes    3            3
4      tetrahexes  7            10
5      pentahexes  22           33
6*     hexahexes   82           147
=====  ==========  ===========  ===========

"*" above means that forms with enclosed holes exist.

The numbers of polyhexes can also be found in the following sequences
from `The On-Line Encyclopedia of Integer Sequences
<http://oeis.org>`_: A000228_ (free) and A006535_ (one-sided).

.. _A000228: http://oeis.org/A000228
.. _A006535: http://oeis.org/A006535

Examples of the polyhexes from order 1 (monohex) to order 6
(hexahexes) are given in the tables below.

The polyhexes are named with a letter-number scheme, like "H1", "A3",
and "I06".  The initial letter is the letter of the alphabet that the
polyhex most closely resembles.  In some cases, that resemblance is
weak, and the letters are arbitrary.  The final digit of the number
represents the polyform order (how many unit hexagons are in the
polyhex).  There are more hexahexes than letters in the alphabet, so
their names have an extra middle digit (numbered from 0) to
differentiate the variations.

.. _table legend:

In the tables below, "Aspects" refers to the number of unique
orientations that a polyform may take (different rotations, flipped or
not).  This varies with the symmetry of the polyform.

The "One-Sided" column identifies polyforms that are asymmetrical in
reflection.  Treating the flipped and unflipped versions of
asymmetrical polyhexes as distinct polyforms (and disallowing further
reflection or "flipping"), results in "one-sided" polyhexes and
puzzles.


Monohex
-------

There is only one monohex (order-1 polyhex):

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - H1
     - .. image:: images/pieces/polyhexes/H1.png
     - 3
     -


Dihex
-----

There is only one dihex (order-2 polyhex):

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - I2
     - .. image:: images/pieces/polyhexes/I2.png
     - 3
     -


Trihexes
--------

There are 3 trihexes (order-3 polyhexes):

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - A3
     - .. image:: images/pieces/polyhexes/A3.png
     - 2
     -

   * - I3
     - .. image:: images/pieces/polyhexes/I3.png
     - 3
     -

   * - V3
     - .. image:: images/pieces/polyhexes/V3.png
     - 6
     -


Tetrahexes
----------

There are 7 free tetrahexes (order-4 polyhexes) and 10 one-sided
tetrahexes:

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - I4
     - .. image:: images/pieces/polyhexes/I4.png
     - 3
     -

   * - J4
     - .. image:: images/pieces/polyhexes/J4.png
     - 12
     - yes

   * - O4
     - .. image:: images/pieces/polyhexes/O4.png
     - 3
     -

   * - P4
     - .. image:: images/pieces/polyhexes/P4.png
     - 12
     - yes

   * - S4
     - .. image:: images/pieces/polyhexes/S4.png
     - 6
     - yes

   * - U4
     - .. image:: images/pieces/polyhexes/U4.png
     - 6
     -

   * - Y4
     - .. image:: images/pieces/polyhexes/Y4.png
     - 2
     -


Pentahexes
----------

There are 22 free pentahexes (order-5 polyhexes) and 33 one-sided
pentahexes:

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - A5
     - .. image:: images/pieces/polyhexes/A5.png
     - 6
     -

   * - B5
     - .. image:: images/pieces/polyhexes/B5.png
     - 12
     - yes

   * - C5
     - .. image:: images/pieces/polyhexes/C5.png
     - 6
     -

   * - D5
     - .. image:: images/pieces/polyhexes/D5.png
     - 6
     -

   * - E5
     - .. image:: images/pieces/polyhexes/E5.png
     - 6
     -

   * - F5
     - .. image:: images/pieces/polyhexes/F5.png
     - 12
     - yes

   * - G5
     - .. image:: images/pieces/polyhexes/G5.png
     - 12
     - yes

   * - H5
     - .. image:: images/pieces/polyhexes/H5.png
     - 12
     - yes

   * - I5
     - .. image:: images/pieces/polyhexes/I5.png
     - 3
     -

   * - J5
     - .. image:: images/pieces/polyhexes/J5.png
     - 12
     - yes

   * - L5
     - .. image:: images/pieces/polyhexes/L5.png
     - 6
     -

   * - N5
     - .. image:: images/pieces/polyhexes/N5.png
     - 12
     - yes

   * - P5
     - .. image:: images/pieces/polyhexes/P5.png
     - 12
     - yes

   * - Q5
     - .. image:: images/pieces/polyhexes/Q5.png
     - 12
     - yes

   * - R5
     - .. image:: images/pieces/polyhexes/R5.png
     - 12
     - yes

   * - S5
     - .. image:: images/pieces/polyhexes/S5.png
     - 6
     - yes

   * - T5
     - .. image:: images/pieces/polyhexes/T5.png
     - 12
     - yes

   * - U5
     - .. image:: images/pieces/polyhexes/U5.png
     - 6
     -

   * - V5
     - .. image:: images/pieces/polyhexes/V5.png
     - 6
     -

   * - W5
     - .. image:: images/pieces/polyhexes/W5.png
     - 6
     -

   * - X5
     - .. image:: images/pieces/polyhexes/X5.png
     - 3
     -

   * - Y5
     - .. image:: images/pieces/polyhexes/Y5.png
     - 6
     -


Hexahexes
----------

There are 82 free hexahexes (order-6 polyhexes) and 147 one-sided
hexahexes:

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - One-Sided

   * - A06
     - .. image:: images/pieces/polyhexes/A06.png
     - 2
     -

   * - A16
     - .. image:: images/pieces/polyhexes/A16.png
     - 12
     - yes

   * - A26
     - .. image:: images/pieces/polyhexes/A26.png
     - 12
     - yes

   * - C06
     - .. image:: images/pieces/polyhexes/C06.png
     - 6
     -

   * - C16
     - .. image:: images/pieces/polyhexes/C16.png
     - 6
     -

   * - C26
     - .. image:: images/pieces/polyhexes/C26.png
     - 12
     - yes

   * - C36
     - .. image:: images/pieces/polyhexes/C36.png
     - 12
     - yes

   * - C46
     - .. image:: images/pieces/polyhexes/C46.png
     - 12
     - yes

   * - C56
     - .. image:: images/pieces/polyhexes/C56.png
     - 12
     - yes

   * - C66
     - .. image:: images/pieces/polyhexes/C66.png
     - 12
     - yes

   * - C76
     - .. image:: images/pieces/polyhexes/C76.png
     - 12
     - yes

   * - E06
     - .. image:: images/pieces/polyhexes/E06.png
     - 6
     -

   * - F06
     - .. image:: images/pieces/polyhexes/F06.png
     - 12
     - yes

   * - F16
     - .. image:: images/pieces/polyhexes/F16.png
     - 12
     - yes

   * - H06
     - .. image:: images/pieces/polyhexes/H06.png
     - 12
     - yes

   * - H16
     - .. image:: images/pieces/polyhexes/H16.png
     - 12
     - yes

   * - H26
     - .. image:: images/pieces/polyhexes/H26.png
     - 12
     - yes

   * - I06
     - .. image:: images/pieces/polyhexes/I06.png
     - 3
     -

   * - J06
     - .. image:: images/pieces/polyhexes/J06.png
     - 12
     - yes

   * - J16
     - .. image:: images/pieces/polyhexes/J16.png
     - 12
     - yes

   * - J26
     - .. image:: images/pieces/polyhexes/J26.png
     - 12
     - yes

   * - J36
     - .. image:: images/pieces/polyhexes/J36.png
     - 12
     - yes

   * - J46
     - .. image:: images/pieces/polyhexes/J46.png
     - 12
     - yes

   * - K06
     - .. image:: images/pieces/polyhexes/K06.png
     - 12
     - yes

   * - L06
     - .. image:: images/pieces/polyhexes/L06.png
     - 12
     - yes

   * - L16
     - .. image:: images/pieces/polyhexes/L16.png
     - 12
     - yes

   * - L26
     - .. image:: images/pieces/polyhexes/L26.png
     - 12
     - yes

   * - L36
     - .. image:: images/pieces/polyhexes/L36.png
     - 12
     - yes

   * - M06
     - .. image:: images/pieces/polyhexes/M06.png
     - 12
     - yes

   * - M16
     - .. image:: images/pieces/polyhexes/M16.png
     - 12
     - yes

   * - M26
     - .. image:: images/pieces/polyhexes/M26.png
     - 12
     - yes

   * - M36
     - .. image:: images/pieces/polyhexes/M36.png
     - 6
     - yes

   * - M46
     - .. image:: images/pieces/polyhexes/M46.png
     - 6
     - yes

   * - N06
     - .. image:: images/pieces/polyhexes/N06.png
     - 6
     - yes

   * - N16
     - .. image:: images/pieces/polyhexes/N16.png
     - 12
     - yes

   * - O06
     - .. image:: images/pieces/polyhexes/O06.png
     - 1
     -

   * - P06
     - .. image:: images/pieces/polyhexes/P06.png
     - 12
     - yes

   * - P16
     - .. image:: images/pieces/polyhexes/P16.png
     - 12
     - yes

   * - P26
     - .. image:: images/pieces/polyhexes/P26.png
     - 12
     - yes

   * - P36
     - .. image:: images/pieces/polyhexes/P36.png
     - 12
     - yes

   * - P46
     - .. image:: images/pieces/polyhexes/P46.png
     - 12
     - yes

   * - P56
     - .. image:: images/pieces/polyhexes/P56.png
     - 12
     - yes

   * - P66
     - .. image:: images/pieces/polyhexes/P66.png
     - 12
     - yes

   * - P76
     - .. image:: images/pieces/polyhexes/P76.png
     - 12
     - yes

   * - Q06
     - .. image:: images/pieces/polyhexes/Q06.png
     - 12
     - yes

   * - Q16
     - .. image:: images/pieces/polyhexes/Q16.png
     - 12
     - yes

   * - Q26
     - .. image:: images/pieces/polyhexes/Q26.png
     - 12
     - yes

   * - Q36
     - .. image:: images/pieces/polyhexes/Q36.png
     - 12
     - yes

   * - R06
     - .. image:: images/pieces/polyhexes/R06.png
     - 12
     - yes

   * - R16
     - .. image:: images/pieces/polyhexes/R16.png
     - 12
     - yes

   * - S06
     - .. image:: images/pieces/polyhexes/S06.png
     - 6
     - yes

   * - S16
     - .. image:: images/pieces/polyhexes/S16.png
     - 6
     - yes

   * - S26
     - .. image:: images/pieces/polyhexes/S26.png
     - 6
     - yes

   * - S36
     - .. image:: images/pieces/polyhexes/S36.png
     - 12
     - yes

   * - T06
     - .. image:: images/pieces/polyhexes/T06.png
     - 6
     -

   * - T16
     - .. image:: images/pieces/polyhexes/T16.png
     - 6
     -

   * - T26
     - .. image:: images/pieces/polyhexes/T26.png
     - 12
     - yes

   * - T36
     - .. image:: images/pieces/polyhexes/T36.png
     - 12
     - yes

   * - T46
     - .. image:: images/pieces/polyhexes/T46.png
     - 12
     - yes

   * - T56
     - .. image:: images/pieces/polyhexes/T56.png
     - 6
     -

   * - T66
     - .. image:: images/pieces/polyhexes/T66.png
     - 12
     - yes

   * - T76
     - .. image:: images/pieces/polyhexes/T76.png
     - 12
     - yes

   * - U06
     - .. image:: images/pieces/polyhexes/U06.png
     - 6
     -

   * - U16
     - .. image:: images/pieces/polyhexes/U16.png
     - 6
     -

   * - U26
     - .. image:: images/pieces/polyhexes/U26.png
     - 12
     - yes

   * - V06
     - .. image:: images/pieces/polyhexes/V06.png
     - 6
     -

   * - V16
     - .. image:: images/pieces/polyhexes/V16.png
     - 12
     - yes

   * - W06
     - .. image:: images/pieces/polyhexes/W06.png
     - 12
     - yes

   * - W16
     - .. image:: images/pieces/polyhexes/W16.png
     - 12
     - yes

   * - W26
     - .. image:: images/pieces/polyhexes/W26.png
     - 12
     - yes

   * - W36
     - .. image:: images/pieces/polyhexes/W36.png
     - 12
     - yes

   * - X06
     - .. image:: images/pieces/polyhexes/X06.png
     - 3
     -

   * - X16
     - .. image:: images/pieces/polyhexes/X16.png
     - 3
     -

   * - X26
     - .. image:: images/pieces/polyhexes/X26.png
     - 12
     - yes

   * - Y06
     - .. image:: images/pieces/polyhexes/Y06.png
     - 6
     -

   * - Y16
     - .. image:: images/pieces/polyhexes/Y16.png
     - 6
     -

   * - Y26
     - .. image:: images/pieces/polyhexes/Y26.png
     - 6
     -

   * - Y36
     - .. image:: images/pieces/polyhexes/Y36.png
     - 12
     - yes

   * - Y46
     - .. image:: images/pieces/polyhexes/Y46.png
     - 12
     - yes

   * - Y56
     - .. image:: images/pieces/polyhexes/Y56.png
     - 12
     - yes

   * - Y66
     - .. image:: images/pieces/polyhexes/Y66.png
     - 4
     - yes

   * - Z06
     - .. image:: images/pieces/polyhexes/Z06.png
     - 6
     - yes


Coordinate System
=================

Polyhex puzzles use a skewed 2-D coordinate system, where the X and Y
axes are 60?? apart instead of the usual 90??.  The typical
representation (as seen in the Polyform Puzzler solution data files)
positions the Y axis vertically with the X axis 30?? counter-clockwise
from horizontal::

                            __   3
                         __/  \
                      __/  \  /  2
                   __/   __/  \
                __/     /   __/  1
             __/  \__   \  /  \
          __/   __   \__/  \  /  y=0
         /  \  /  \__/  \__/  \
      3  \  /  \__    __/   __/
         /  \__/  \  /   __/
      2  \  /     /  \__/    6
         /  \     \__/    5
      1  \  /   __/    4
         /  \__/    3
    y=0  \__/    2
              1
         x=0

Each unit hexagon has 6 immediate neighbors.  The neighbors of the
hexagon at coordinates *(x, y)* are:

    *{(x+1, y), (x, y+1), (x-1, y-1), (x-1, y), (x, y-1), (x+1, y-1)}*


.. |c| unicode:: U+00A9 .. copyright sign
