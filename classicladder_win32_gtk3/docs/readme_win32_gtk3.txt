CLASSIC LADDER PROJECT
Copyright (C) 2001-2020 Marc Le Douarain
marc . le - douarain /AT\ laposte \DOT/ net
http://www.sourceforge.net/projects/classicladder
http://sites.google.com/site/classicladder
February 2001

Version 0.9.113 "Windows port" for GTK+ 3.22.26 (4 January 2020)
----------------------------------------------------------------

This file archive is a "complete" version, directly including all the GTK+3 DLLs files required !!!

This version of GTK+ requires Windows Vista or later.

NOW IN THE WINDOWS VERSION, THE DIRECT PORT ACCESS FOR LOCAL INPUTS/OUTPUTS (parallel port, ...)
IS ALSO WORKING (as in the Linux version since a very long time).
The external "inpout32.dll" library is necessary (included in this archive).


This version has been ported on Windows using MinGW compiling from the MSYS2 console.
In the Makefile, the WINDOWS variable must be set, and the GTK3 version selected (GTK2 for Linux per-default).
The GTK dev files were taken here:
https://www.gtk.org/download/windows.php


The ClassicLadder sources are included in the Linux archive file.
