.. -*- coding: utf-8 -*-

==============================
 An Introduction to Polycubes
==============================

:Author: David Goodger <goodger@python.org>
:Date: $Date$
:Revision: $Revision$
:Web site: http://puzzler.sourceforge.net/
:Copyright: ©1998-2018 by David J. Goodger
:License: `GPL 2 <../COPYING.html>`__

.. image:: images/puzzler.png
   :align: center

.. sidebar:: Also see:

   * `Polycubes: Puzzles & Solutions <polycubes.html>`_
   * `Pentacubes: Puzzles & Solutions <pentacubes.html>`_
   * `Solid Pentominoes: Puzzles & Solutions <solid-pentominoes.html>`_
   * `Notes on Polycubes <polycube-notes.html>`_
   * `Polyform Puzzler: Puzzles & Solutions <puzzles.html>`_
   * `Polyform Puzzler FAQ <FAQ.html>`_
     (`polyform details <FAQ.html#what-polyforms-are-there>`__,
     `numbers of polyforms <FAQ.html#how-many-of-each-type-of-polyform-are-there>`__,
     `interpreting solution files <FAQ.html#how-should-polycube-solution-files-be-interpreted>`__)

.. contents::

**Polycubes** are polyforms constructed from unit cubes joined
face-to-face in regular three-dimensional Cartesian space.  The
polycubes that are flat (only one cube thick) are known as "planar
polycubes" or "solid polyominoes".

Here is a puzzle containing all the polycubes of order 1 through 5:

.. image:: images/cubes/polycubes-12345-overlapping-blocks-1.png

See `Polycubes: Puzzles & Solutions`_, `Pentacubes: Puzzles &
Solutions`_, and `Solid Pentominoes: Puzzles & Solutions`_ for many
more puzzles.


Polyforms
=========

The number and names of the various orders of polycubes are as
follows:

=====  ==========  ===========  ===========
Order  | Polyform  Polycubes    | Planar
       | Name                   | Polycubes
=====  ==========  ===========  ===========
1      monocube    1            1
2      dicube      1            1
3      tricubes    2            2
4      tetracubes  8            5
5      pentacubes  29           12
6      hexacubes   166          35
=====  ==========  ===========  ===========

"*" above means that forms with enclosed holes exist.

The numbers of polycubes can also be found in the following sequences
from `The On-Line Encyclopedia of Integer Sequences
<http://oeis.org>`_: A000162_ (3-D) and A000105_ (planar polycubes /
solid polyominoes).

.. _A000162: http://oeis.org/A000162
.. _A000105: http://oeis.org/A000105

Examples of the polycubes from order 1 (monocube) to order 6
(hexacubes) are given in the tables below.

The polycubes are named with letters (like the monocube "M") or a
letter-number scheme (like the "I3" tricube, and the "F5" and "V15"
pentacubes).  The names used by Polyform Puzzler are based on the
traditional names for pentominoes, `Kadon's names for their
Superquints`__, hexacubes__, and `Poly-4 Supplement`_ sets, as well as
`Thorleif Bundgård's names for Soma cubes`__.

__ http://www.gamepuzzles.com/sqnames.htm
__ http://www.gamepuzzles.com/hxnames.htm
__ http://www.fam-bundgaard.dk/SOMA/FIGURES/NOTATION.HTM

The initial letter of each name is the letter of the alphabet that the
polycube most closely resembles, or an initial.  In some cases, that
resemblance is weak, and the letters are arbitrary.  The final digit
of the number represents the polyform order (how many unit cubes are
in the polycube).  There are more pentacubes than letters in the
alphabet, so the names of many of the non-planar pieces have an
extra middle digit to differentiate the variations.  
All 166 of the hexacubes have 3-character names.

.. _table legend:

In the tables below, "Aspects" refers to the number of unique
orientations that a polyform may take (different rotations, flipped or
not).  This varies with the symmetry of the polyform.

The "Notes" column records which pieces are planar and non-planar, as
well as chiral pairs (matching left-hand and right-hand mirror
images).  The 3-D polycubes cannot be "flipped" into their mirror
images (that would require access to a fourth physical dimension).

Alternate names and name origins are noted in the "Name" column.


Monocube
--------

There is only one monocube (order-1 polycube):

.. list-table::
   :widths: 20 20 20 20
   :header-rows: 1

   * - Name
     - Image
     - Aspects
     - Notes

   * - | M
       | (from "Monocube")
     - .. image:: images/pieces/polycubes/M.png
     - 1
     - planar


Dicube
------

There is only one dicube (order-2 polycube), also planar (a solid
monomino):

.. list-table::
   :header-rows: 1
   :class: compact

   * - Name
     - Image
     - Aspects
     - Notes

   * - | D
       | (from "Dicube")
     - .. image:: images/pieces/polycubes/D.png
     - 3
     - planar


Tricubes
--------

There are 2 tricubes (order-3 polycubes), also planar (a solid
domino):

.. list-table::
   :header-rows: 1
   :class: compact

   * - Name
     - Image
     - Aspects
     - Notes

   * - I3
     - .. image:: images/pieces/polycubes/I3.png
     - 3
     - planar

   * - | V3
       | (Soma "V")
     - .. image:: images/pieces/polycubes/V3.png
     - 12
     - planar


Tetracubes
----------

There are 8 tetracubes (order-4 polycubes), 5 of which are planar (solid
tetrominoes):

.. list-table::
   :header-rows: 1
   :class: compact

   * - Name
     - Image
     - Aspects
     - Notes

   * - | A4
       | (Soma "a"; Kadon "V3")
     - .. image:: images/pieces/polycubes/A4.png
     - 12
     - non-planar; chiral pair with "B4"

   * - | B4
       | (Soma "b"; Kadon "V1")
     - .. image:: images/pieces/polycubes/B4.png
     - 12
     - non-planar; chiral pair with "A4"

   * - I4
     - .. image:: images/pieces/polycubes/I4.png
     - 3
     - planar

   * - | L4
       | (Soma "L")
     - .. image:: images/pieces/polycubes/L4.png
     - 24
     - planar

   * - O4
     - .. image:: images/pieces/polycubes/O4.png
     - 3
     - planar

   * - | P4
       | (Soma "p"; Kadon "V2")
     - .. image:: images/pieces/polycubes/P4.png
     - 8
     - non-planar

   * - | S4
       | (Soma "Z")
     - .. image:: images/pieces/polycubes/S4.png
     - 12
     - planar

   * - | T4
       | (Soma "T")
     - .. image:: images/pieces/polycubes/T4.png
     - 12
     - planar


Soma Cubes
----------

The Soma Cubes, invented by Piet Hein in 1933, consist of 7 pieces:
all the non-convex polycubes of order 3 (1) and 4 (6).

.. list-table::
   :header-rows: 1
   :class: compact

   * - Name
     - Image
     - Aspects
     - Notes

   * - | V
       | (polycube "V3")
     - .. image:: images/pieces/polycubes/V3.png
     - 12
     - planar; order 3

   * - | L
       | (polycube "L4")
     - .. image:: images/pieces/polycubes/L4.png
     - 24
     - planar; order 4

   * - | T
       | (polycube "T4")
     - .. image:: images/pieces/polycubes/T4.png
     - 12
     - planar; order 4

   * - | Z
       | (polycube "S4"; Kadon "S")
     - .. image:: images/pieces/polycubes/S4.png
     - 12
     - planar; order 4

   * - | a
       | (polycube "A4"; Kadon "V3")
     - .. image:: images/pieces/polycubes/A4.png
     - 12
     - non-planar; order 4; chiral pair with "b"

   * - | b
       | (polycube "B4"; Kadon "V1")
     - .. image:: images/pieces/polycubes/B4.png
     - 12
     - non-planar; order 4; chiral pair with "a"

   * - | p
       | (polycube "P4"; Kadon "V2")
     - .. image:: images/pieces/polycubes/P4.png
     - 8
     - non-planar; order 4


Pentacubes
----------

There are 29 pentacubes (order-5 polycubes), 12 of which are planar
(solid pentominoes):

.. list-table::
   :header-rows: 1
   :class: compact

   * - Name
     - Image
     - Aspects
     - Notes

   * - A5
     - .. image:: images/pieces/polycubes/A5.png
     - 24
     - non-planar

   * - F5
     - .. image:: images/pieces/polycubes/F5.png
     - 24
     - planar

   * - I5
     - .. image:: images/pieces/polycubes/I5.png
     - 3
     - planar

   * - J15
     - .. image:: images/pieces/polycubes/J15.png
     - 12
     - non-planar; chiral pair with "L15"

   * - J25
     - .. image:: images/pieces/polycubes/J25.png
     - 24
     - non-planar; chiral pair with "L25"

   * - J45
     - .. image:: images/pieces/polycubes/J45.png
     - 24
     - non-planar; chiral pair with "L45"

   * - L5
     - .. image:: images/pieces/polycubes/L5.png
     - 24
     - planar

   * - L15
     - .. image:: images/pieces/polycubes/L15.png
     - 12
     - non-planar; chiral pair with "J15"

   * - L25
     - .. image:: images/pieces/polycubes/L25.png
     - 24
     - non-planar; chiral pair with "J25"

   * - L35
     - .. image:: images/pieces/polycubes/L35.png
     - 24
     - non-planar; Kadon's `Super Deluxe Quintillions`_ set includes a
       second copy called "J35" (also adopted by Polyform Puzzler's
       `Pentacubes Plus`_)

   * - L45
     - .. image:: images/pieces/polycubes/L45.png
     - 24
     - non-planar; chiral pair with "J45"

   * - N5
     - .. image:: images/pieces/polycubes/N5.png
     - 24
     - planar

   * - N15
     - .. image:: images/pieces/polycubes/N15.png
     - 24
     - non-planar; chiral pair with "S15"

   * - N25
     - .. image:: images/pieces/polycubes/N25.png
     - 24
     - non-planar; chiral pair with "S25"

   * - P5
     - .. image:: images/pieces/polycubes/P5.png
     - 24
     - planar

   * - Q5
     - .. image:: images/pieces/polycubes/Q5.png
     - 24
     - non-planar

   * - S15
     - .. image:: images/pieces/polycubes/S15.png
     - 24
     - non-planar; chiral pair with "N15"

   * - S25
     - .. image:: images/pieces/polycubes/S25.png
     - 24
     - non-planar; chiral pair with "N25"

   * - T5
     - .. image:: images/pieces/polycubes/T5.png
     - 12
     - planar

   * - T15
     - .. image:: images/pieces/polycubes/T15.png
     - 12
     - non-planar

   * - T25
     - .. image:: images/pieces/polycubes/T25.png
     - 24
     - non-planar

   * - U5
     - .. image:: images/pieces/polycubes/U5.png
     - 12
     - planar

   * - V5
     - .. image:: images/pieces/polycubes/V5.png
     - 12
     - planar

   * - V15
     - .. image:: images/pieces/polycubes/V15.png
     - 12
     - non-planar; chiral pair with "V25"

   * - V25
     - .. image:: images/pieces/polycubes/V25.png
     - 12
     - non-planar; chiral pair with "V15"

   * - W5
     - .. image:: images/pieces/polycubes/W5.png
     - 12
     - planar

   * - X5
     - .. image:: images/pieces/polycubes/X5.png
     - 3
     - planar

   * - Y5
     - .. image:: images/pieces/polycubes/Y5.png
     - 24
     - planar

   * - Z5
     - .. image:: images/pieces/polycubes/Z5.png
     - 12
     - planar


Hexacubes
----------

There are 166 hexacubes (order-6 polycubes), 35 of which are planar
(solid hexominoes):

.. list-table::
   :header-rows: 1
   :class: compact

   * - Name
     - Image
     - Aspects
     - Notes

   * - | A06
       | (Kadon's "A")
     - .. image:: images/pieces/polycubes/A06.png
     - 12
     - planar

   * - | Aa6
       | ("Fat A")
     - .. image:: images/pieces/polycubes/Aa6.png
     - 12
     - non-planar

   * - | Ba6
       | ("B")
     - .. image:: images/pieces/polycubes/Ba6.png
     - 4
     - non-planar

   * - C06
     - .. image:: images/pieces/polycubes/C06.png
     - 12
     - planar

   * - D06
     - .. image:: images/pieces/polycubes/D06.png
     - 12
     - planar

   * - E06
     - .. image:: images/pieces/polycubes/E06.png
     - 12
     - planar

   * - | F06
       | ("hi F")
     - .. image:: images/pieces/polycubes/F06.png
     - 24
     - planar

   * - | F16
       | ("low F")
     - .. image:: images/pieces/polycubes/F16.png
     - 24
     - planar

   * - | F26
       | ("hi 4")
     - .. image:: images/pieces/polycubes/F26.png
     - 24
     - planar

   * - | F36
       | ("low 4")
     - .. image:: images/pieces/polycubes/F36.png
     - 24
     - planar

   * - | Fa6
       | ("F1")
     - .. image:: images/pieces/polycubes/Fa6.png
     - 24
     - non-planar

   * - | Fb6
       | ("F2")
     - .. image:: images/pieces/polycubes/Fb6.png
     - 24
     - non-planar

   * - | Fc6
       | ("F3")
     - .. image:: images/pieces/polycubes/Fc6.png
     - 24
     - non-planar

   * - | Fd6
       | ("F4")
     - .. image:: images/pieces/polycubes/Fd6.png
     - 24
     - non-planar

   * - | Fe6
       | ("F5")
     - .. image:: images/pieces/polycubes/Fe6.png
     - 24
     - non-planar

   * - | Ff6
       | ("Fb1")
     - .. image:: images/pieces/polycubes/Ff6.png
     - 24
     - non-planar

   * - | Fg6
       | ("Fb2")
     - .. image:: images/pieces/polycubes/Fg6.png
     - 24
     - non-planar

   * - | Fh6
       | ("Fb3")
     - .. image:: images/pieces/polycubes/Fh6.png
     - 24
     - non-planar

   * - | Fi6
       | ("Fb4")
     - .. image:: images/pieces/polycubes/Fi6.png
     - 24
     - non-planar

   * - | Fj6
       | ("Fb5")
     - .. image:: images/pieces/polycubes/Fj6.png
     - 24
     - non-planar

   * - G06
     - .. image:: images/pieces/polycubes/G06.png
     - 24
     - planar

   * - H06
     - .. image:: images/pieces/polycubes/H06.png
     - 24
     - planar

   * - I06
     - .. image:: images/pieces/polycubes/I06.png
     - 3
     - planar

   * - J06
     - .. image:: images/pieces/polycubes/J06.png
     - 24
     - planar

   * - | Ja6
       | ("J1l")
     - .. image:: images/pieces/polycubes/Ja6.png
     - 24
     - non-planar

   * - | Jb6
       | ("J1r")
     - .. image:: images/pieces/polycubes/Jb6.png
     - 24
     - non-planar

   * - | Jc6
       | ("J2l")
     - .. image:: images/pieces/polycubes/Jc6.png
     - 24
     - non-planar

   * - | Jd6
       | ("J2r")
     - .. image:: images/pieces/polycubes/Jd6.png
     - 24
     - non-planar

   * - | Je6
       | ("J3r")
     - .. image:: images/pieces/polycubes/Je6.png
     - 24
     - non-planar

   * - | Jf6
       | ("J4l")
     - .. image:: images/pieces/polycubes/Jf6.png
     - 24
     - non-planar

   * - | Jg6
       | ("J4u")
     - .. image:: images/pieces/polycubes/Jg6.png
     - 24
     - non-planar

   * - | Jh6
       | ("J4d")
     - .. image:: images/pieces/polycubes/Jh6.png
     - 24
     - non-planar

   * - | Ji6
       | ("J4v")
     - .. image:: images/pieces/polycubes/Ji6.png
     - 12
     - non-planar

   * - K06
     - .. image:: images/pieces/polycubes/K06.png
     - 12
     - planar

   * - L06
     - .. image:: images/pieces/polycubes/L06.png
     - 24
     - planar

   * - | La6
       | ("L1")
     - .. image:: images/pieces/polycubes/La6.png
     - 12
     - non-planar

   * - | Lb6
       | ("L4")
     - .. image:: images/pieces/polycubes/Lb6.png
     - 24
     - non-planar

   * - | Lc6
       | ("L5")
     - .. image:: images/pieces/polycubes/Lc6.png
     - 24
     - non-planar

   * - | Ld6
       | ("Lb1")
     - .. image:: images/pieces/polycubes/Ld6.png
     - 12
     - non-planar

   * - | Le6
       | ("Lb5")
     - .. image:: images/pieces/polycubes/Le6.png
     - 24
     - non-planar

   * - | Lf6
       | ("L1l")
     - .. image:: images/pieces/polycubes/Lf6.png
     - 24
     - non-planar

   * - | Lg6
       | ("L1r")
     - .. image:: images/pieces/polycubes/Lg6.png
     - 24
     - non-planar

   * - | Lh6
       | ("L2l")
     - .. image:: images/pieces/polycubes/Lh6.png
     - 24
     - non-planar

   * - | Li6
       | ("L2r")
     - .. image:: images/pieces/polycubes/Li6.png
     - 24
     - non-planar

   * - | Lj6
       | ("L3l")
     - .. image:: images/pieces/polycubes/Lj6.png
     - 24
     - non-planar

   * - | Lk6
       | ("L4r")
     - .. image:: images/pieces/polycubes/Lk6.png
     - 24
     - non-planar

   * - | Ll6
       | ("L4u")
     - .. image:: images/pieces/polycubes/Ll6.png
     - 24
     - non-planar

   * - | Lm6
       | ("L4d")
     - .. image:: images/pieces/polycubes/Lm6.png
     - 24
     - non-planar

   * - | Ln6
       | ("L4v")
     - .. image:: images/pieces/polycubes/Ln6.png
     - 12
     - non-planar

   * - M06
     - .. image:: images/pieces/polycubes/M06.png
     - 24
     - planar

   * - | N06
       | ("short N")
     - .. image:: images/pieces/polycubes/N06.png
     - 12
     - planar

   * - | N16
       | ("long N")
     - .. image:: images/pieces/polycubes/N16.png
     - 24
     - planar

   * - | Na6
       | ("N1")
     - .. image:: images/pieces/polycubes/Na6.png
     - 24
     - non-planar

   * - | Nb6
       | ("N2")
     - .. image:: images/pieces/polycubes/Nb6.png
     - 24
     - non-planar

   * - | Nc6
       | ("N3")
     - .. image:: images/pieces/polycubes/Nc6.png
     - 24
     - non-planar

   * - | Nd6
       | ("N4")
     - .. image:: images/pieces/polycubes/Nd6.png
     - 24
     - non-planar

   * - | Ne6
       | ("N5")
     - .. image:: images/pieces/polycubes/Ne6.png
     - 24
     - non-planar

   * - | Nf6
       | ("Nb1")
     - .. image:: images/pieces/polycubes/Nf6.png
     - 24
     - non-planar

   * - | Ng6
       | ("Nb2")
     - .. image:: images/pieces/polycubes/Ng6.png
     - 24
     - non-planar

   * - | Nh6
       | ("Nb3")
     - .. image:: images/pieces/polycubes/Nh6.png
     - 24
     - non-planar

   * - | Ni6
       | ("Nb4")
     - .. image:: images/pieces/polycubes/Ni6.png
     - 24
     - non-planar

   * - | Nj6
       | ("Nb5")
     - .. image:: images/pieces/polycubes/Nj6.png
     - 24
     - non-planar

   * - | Nk6
       | ("N13")
     - .. image:: images/pieces/polycubes/Nk6.png
     - 24
     - non-planar

   * - | Nl6
       | ("N14")
     - .. image:: images/pieces/polycubes/Nl6.png
     - 12
     - non-planar

   * - | Nm6
       | ("N1l")
     - .. image:: images/pieces/polycubes/Nm6.png
     - 24
     - non-planar

   * - | Nn6
       | ("N1r")
     - .. image:: images/pieces/polycubes/Nn6.png
     - 24
     - non-planar

   * - | No6
       | ("N1u")
     - .. image:: images/pieces/polycubes/No6.png
     - 12
     - non-planar

   * - | Np6
       | ("N1b3")
     - .. image:: images/pieces/polycubes/Np6.png
     - 24
     - non-planar

   * - | Nq6
       | ("N1b4")
     - .. image:: images/pieces/polycubes/Nq6.png
     - 24
     - non-planar

   * - | Nr6
       | ("N23")
     - .. image:: images/pieces/polycubes/Nr6.png
     - 12
     - non-planar

   * - | Ns6
       | ("N2r")
     - .. image:: images/pieces/polycubes/Ns6.png
     - 24
     - non-planar

   * - | Nt6
       | ("N2b3")
     - .. image:: images/pieces/polycubes/Nt6.png
     - 12
     - non-planar

   * - | Nu6
       | ("N2b4")
     - .. image:: images/pieces/polycubes/Nu6.png
     - 24
     - non-planar

   * - O06
     - .. image:: images/pieces/polycubes/O06.png
     - 6
     - planar

   * - P06
     - .. image:: images/pieces/polycubes/P06.png
     - 24
     - planar

   * - | Pa6
       | ("P1")
     - .. image:: images/pieces/polycubes/Pa6.png
     - 24
     - non-planar

   * - | Pb6
       | ("P2")
     - .. image:: images/pieces/polycubes/Pb6.png
     - 24
     - non-planar

   * - | Pc6
       | ("P3")
     - .. image:: images/pieces/polycubes/Pc6.png
     - 24
     - non-planar

   * - | Pd6
       | ("P4")
     - .. image:: images/pieces/polycubes/Pd6.png
     - 24
     - non-planar

   * - | Pe6
       | ("P5")
     - .. image:: images/pieces/polycubes/Pe6.png
     - 24
     - non-planar

   * - | Pf6
       | ("Pb1")
     - .. image:: images/pieces/polycubes/Pf6.png
     - 24
     - non-planar

   * - | Pg6
       | ("Pb2")
     - .. image:: images/pieces/polycubes/Pg6.png
     - 24
     - non-planar

   * - | Ph6
       | ("Pb3")
     - .. image:: images/pieces/polycubes/Ph6.png
     - 24
     - non-planar

   * - | Pi6
       | ("Pb4")
     - .. image:: images/pieces/polycubes/Pi6.png
     - 24
     - non-planar

   * - | Pj6
       | ("Pb5")
     - .. image:: images/pieces/polycubes/Pj6.png
     - 24
     - non-planar

   * - Q06
     - .. image:: images/pieces/polycubes/Q06.png
     - 24
     - planar

   * - | Qa6
       | ("Q14")
     - .. image:: images/pieces/polycubes/Qa6.png
     - 12
     - non-planar

   * - | Qb6
       | ("Q4r")
     - .. image:: images/pieces/polycubes/Qb6.png
     - 24
     - non-planar

   * - | Qc6
       | ("Q4d")
     - .. image:: images/pieces/polycubes/Qc6.png
     - 24
     - non-planar

   * - | Qd6
       | ("Q4v")
     - .. image:: images/pieces/polycubes/Qd6.png
     - 24
     - non-planar

   * - | Qe6
       | ("Q4b1")
     - .. image:: images/pieces/polycubes/Qe6.png
     - 12
     - non-planar

   * - R06
     - .. image:: images/pieces/polycubes/R06.png
     - 24
     - planar

   * - | S06
       | ("long S")
     - .. image:: images/pieces/polycubes/S06.png
     - 12
     - planar

   * - | Sa6
       | ("S13")
     - .. image:: images/pieces/polycubes/Sa6.png
     - 24
     - non-planar

   * - | Sb6
       | ("S14")
     - .. image:: images/pieces/polycubes/Sb6.png
     - 12
     - non-planar

   * - | Sc6
       | ("S1l")
     - .. image:: images/pieces/polycubes/Sc6.png
     - 24
     - non-planar

   * - | Sd6
       | ("S1r")
     - .. image:: images/pieces/polycubes/Sd6.png
     - 24
     - non-planar

   * - | Se6
       | ("S1u")
     - .. image:: images/pieces/polycubes/Se6.png
     - 12
     - non-planar

   * - | Sf6
       | ("S23")
     - .. image:: images/pieces/polycubes/Sf6.png
     - 12
     - non-planar

   * - | Sg6
       | ("S2l")
     - .. image:: images/pieces/polycubes/Sg6.png
     - 24
     - non-planar

   * - | Sh6
       | ("S2d")
     - .. image:: images/pieces/polycubes/Sh6.png
     - 24
     - non-planar

   * - | T06
       | ("long T")
     - .. image:: images/pieces/polycubes/T06.png
     - 12
     - planar

   * - | T16
       | ("short T")
     - .. image:: images/pieces/polycubes/T16.png
     - 24
     - planar

   * - | Ta6
       | ("T1")
     - .. image:: images/pieces/polycubes/Ta6.png
     - 24
     - non-planar

   * - | Tb6
       | ("T2")
     - .. image:: images/pieces/polycubes/Tb6.png
     - 24
     - non-planar

   * - | Tc6
       | ("T3")
     - .. image:: images/pieces/polycubes/Tc6.png
     - 24
     - non-planar

   * - | Td6
       | ("T4")
     - .. image:: images/pieces/polycubes/Td6.png
     - 24
     - non-planar

   * - | Te6
       | ("T5")
     - .. image:: images/pieces/polycubes/Te6.png
     - 24
     - non-planar

   * - | Tf6
       | ("T1u")
     - .. image:: images/pieces/polycubes/Tf6.png
     - 24
     - non-planar

   * - | Tg6
       | ("T1d")
     - .. image:: images/pieces/polycubes/Tg6.png
     - 24
     - non-planar

   * - | Th6
       | ("T24")
     - .. image:: images/pieces/polycubes/Th6.png
     - 12
     - non-planar

   * - | Ti6
       | ("T2u")
     - .. image:: images/pieces/polycubes/Ti6.png
     - 24
     - non-planar

   * - | Tj6
       | ("T3u")
     - .. image:: images/pieces/polycubes/Tj6.png
     - 24
     - non-planar

   * - | Tk6
       | ("T3d")
     - .. image:: images/pieces/polycubes/Tk6.png
     - 24
     - non-planar

   * - | Tl6
       | ("T4l")
     - .. image:: images/pieces/polycubes/Tl6.png
     - 24
     - non-planar

   * - | Tm6
       | ("T4r")
     - .. image:: images/pieces/polycubes/Tm6.png
     - 24
     - non-planar

   * - | Tn6
       | ("T4d")
     - .. image:: images/pieces/polycubes/Tn6.png
     - 24
     - non-planar

   * - | To6
       | ("T4v")
     - .. image:: images/pieces/polycubes/To6.png
     - 24
     - non-planar

   * - | Tp6
       | ("T4b4")
     - .. image:: images/pieces/polycubes/Tp6.png
     - 6
     - non-planar

   * - U06
     - .. image:: images/pieces/polycubes/U06.png
     - 24
     - planar

   * - | Ua6
       | ("U1")
     - .. image:: images/pieces/polycubes/Ua6.png
     - 24
     - non-planar

   * - | Ub6
       | ("U2")
     - .. image:: images/pieces/polycubes/Ub6.png
     - 24
     - non-planar

   * - | Uc6
       | ("U3")
     - .. image:: images/pieces/polycubes/Uc6.png
     - 24
     - non-planar

   * - | Ud6
       | ("U4")
     - .. image:: images/pieces/polycubes/Ud6.png
     - 24
     - non-planar

   * - | Ue6
       | ("U5")
     - .. image:: images/pieces/polycubes/Ue6.png
     - 24
     - non-planar

   * - V06
     - .. image:: images/pieces/polycubes/V06.png
     - 24
     - planar

   * - | Va6
       | ("V1")
     - .. image:: images/pieces/polycubes/Va6.png
     - 24
     - non-planar

   * - | Vb6
       | ("V2")
     - .. image:: images/pieces/polycubes/Vb6.png
     - 24
     - non-planar

   * - | Vc6
       | ("V3")
     - .. image:: images/pieces/polycubes/Vc6.png
     - 24
     - non-planar

   * - | Vd6
       | ("V4")
     - .. image:: images/pieces/polycubes/Vd6.png
     - 24
     - non-planar

   * - | Ve6
       | ("V5")
     - .. image:: images/pieces/polycubes/Ve6.png
     - 24
     - non-planar

   * - | Vf6
       | ("V1l")
     - .. image:: images/pieces/polycubes/Vf6.png
     - 12
     - non-planar

   * - | Vg6
       | ("V1d")
     - .. image:: images/pieces/polycubes/Vg6.png
     - 24
     - non-planar

   * - | Vh6
       | ("V3r")
     - .. image:: images/pieces/polycubes/Vh6.png
     - 12
     - non-planar

   * - | Vi6
       | ("V3d")
     - .. image:: images/pieces/polycubes/Vi6.png
     - 24
     - non-planar

   * - | W06
       | ("Wa")
     - .. image:: images/pieces/polycubes/W06.png
     - 24
     - planar

   * - | W16
       | ("Wb")
     - .. image:: images/pieces/polycubes/W16.png
     - 12
     - planar

   * - | W26
       | ("Wc")
     - .. image:: images/pieces/polycubes/W26.png
     - 24
     - planar

   * - | Wa6
       | ("W1")
     - .. image:: images/pieces/polycubes/Wa6.png
     - 24
     - non-planar

   * - | Wb6
       | ("W2")
     - .. image:: images/pieces/polycubes/Wb6.png
     - 24
     - non-planar

   * - | Wc6
       | ("W3")
     - .. image:: images/pieces/polycubes/Wc6.png
     - 24
     - non-planar

   * - | Wd6
       | ("W4")
     - .. image:: images/pieces/polycubes/Wd6.png
     - 24
     - non-planar

   * - | We6
       | ("W5")
     - .. image:: images/pieces/polycubes/We6.png
     - 24
     - non-planar

   * - X06
     - .. image:: images/pieces/polycubes/X06.png
     - 12
     - planar

   * - | X16
       | ("italic X")
     - .. image:: images/pieces/polycubes/X16.png
     - 12
     - planar

   * - | Xa6
       | ("X1")
     - .. image:: images/pieces/polycubes/Xa6.png
     - 24
     - non-planar

   * - | Xb6
       | ("X3")
     - .. image:: images/pieces/polycubes/Xb6.png
     - 6
     - non-planar

   * - | Y06
       | ("hi Y")
     - .. image:: images/pieces/polycubes/Y06.png
     - 24
     - planar

   * - | Y16
       | ("low Y")
     - .. image:: images/pieces/polycubes/Y16.png
     - 12
     - planar

   * - | Ya6
       | ("Y1")
     - .. image:: images/pieces/polycubes/Ya6.png
     - 24
     - non-planar

   * - | Yb6
       | ("Y2")
     - .. image:: images/pieces/polycubes/Yb6.png
     - 24
     - non-planar

   * - | Yc6
       | ("Y3")
     - .. image:: images/pieces/polycubes/Yc6.png
     - 24
     - non-planar

   * - | Yd6
       | ("Y4")
     - .. image:: images/pieces/polycubes/Yd6.png
     - 12
     - non-planar

   * - | Ye6
       | ("Y5")
     - .. image:: images/pieces/polycubes/Ye6.png
     - 24
     - non-planar

   * - | Yf6
       | ("Yb1")
     - .. image:: images/pieces/polycubes/Yf6.png
     - 24
     - non-planar

   * - | Yg6
       | ("Yb2")
     - .. image:: images/pieces/polycubes/Yg6.png
     - 24
     - non-planar

   * - | Yh6
       | ("Yb4")
     - .. image:: images/pieces/polycubes/Yh6.png
     - 12
     - non-planar

   * - | Yi6
       | ("Yb5")
     - .. image:: images/pieces/polycubes/Yi6.png
     - 24
     - non-planar

   * - | Z06
       | ("long Z")
     - .. image:: images/pieces/polycubes/Z06.png
     - 12
     - planar

   * - | Z16
       | ("short Z")
     - .. image:: images/pieces/polycubes/Z16.png
     - 24
     - planar

   * - | Za6
       | ("Z1")
     - .. image:: images/pieces/polycubes/Za6.png
     - 24
     - non-planar

   * - | Zb6
       | ("Z2")
     - .. image:: images/pieces/polycubes/Zb6.png
     - 24
     - non-planar

   * - | Zc6
       | ("Z3")
     - .. image:: images/pieces/polycubes/Zc6.png
     - 12
     - non-planar

   * - | Zd6
       | ("Zb1")
     - .. image:: images/pieces/polycubes/Zd6.png
     - 24
     - non-planar

   * - | Ze6
       | ("Zb2")
     - .. image:: images/pieces/polycubes/Ze6.png
     - 24
     - non-planar

   * - | Zf6
       | ("Zb3")
     - .. image:: images/pieces/polycubes/Zf6.png
     - 12
     - non-planar


Coordinate System
=================

Polycubes (including solid pentominoes and Soma cubes) use a
3-dimensional *(x,y,z)* Cartesian coordinate system.

Each unit cube has 6 immediate neighbors.  The neighbors of the
cube at coordinates *(x, y, z)* are:

    *{(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1),
    (x, y, z-1)}*

`See the FAQ for more details.
<FAQ.html#how-should-polycube-solution-files-be-interpreted>`__


.. _Super Deluxe Quintillions:
   http://gamepuzzles.com/polycube.htm#SQd

.. _Poly-4 Supplement: http://www.gamepuzzles.com/poly4.htm

.. _Pentacubes Plus: pentacubes.html#pentacubes-plus

.. |c| unicode:: U+00A9 .. copyright sign
