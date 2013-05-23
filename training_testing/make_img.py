"""
Author : tharindra galahena (inf0_warri0r)
Project: classifing music using neural network
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 23/05/2013
License:

     Copyright 2013 Tharindra Galahena

This is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
this. If not, see http://www.gnu.org/licenses/.

"""

import file_read
import os


def get_file_list(name):
    ls = list()
    for dirname, dirnames, filenames in os.walk(name):
        for filename in filenames:
            ls.append(((filename, os.path.join(dirname, filename)), filename))

    return ls

ls_rock = get_file_list('./rock')
ls_pop = get_file_list('./pop')
ls_jazz = get_file_list('./jazz')
ls_classic = get_file_list('./classic')

print "\nMaking Images for music files ... \n"

for i in range(0, len(ls_rock)):
    song = file_read.file_read(ls_rock[i][0])
    song.convert()
    song.save('./rock_img')
    print ls_rock[i][1]

for i in range(0, len(ls_pop)):
    song = file_read.file_read(ls_pop[i][0])
    song.convert()
    song.save('./pop_img')
    print ls_pop[i][1]

for i in range(0, len(ls_jazz)):
    song = file_read.file_read(ls_jazz[i][0])
    song.convert()
    song.save('./jazz_img')
    print ls_jazz[i][1]

for i in range(0, len(ls_classic)):
    song = file_read.file_read(ls_classic[i][0])
    song.convert()
    song.save('./classic_img')
    print ls_classic[i][1]

print "\n-DONE-\n"
