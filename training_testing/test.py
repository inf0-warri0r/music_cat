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

import histograme
import neural_net
import os
import Image


def get_file_list(name):
    ls = list()
    for dirname, dirnames, filenames in os.walk(name):
        for filename in filenames:
            ls.append((os.path.join(dirname, filename), filename))
    return ls


def load():
    f = open('weights', 'r')
    cat = f.read()
    f.close()
    weights = list()
    lst = cat.splitlines()
    for i in range(0, len(lst)):
        weights.append(float(lst[i]))

    return weights


def load_f():
    f = open('weights_f', 'r')
    cat = f.read()
    f.close()
    weights = list()
    lst = cat.splitlines()
    for i in range(0, len(lst)):
        weights.append(float(lst[i]))

    return weights

net = neural_net.neural(10, 1, 3, 15, 0.001, 0.0)
net.init()
net.put_weights(load())

dout = [
    [0.0],  # rock
    [1.0]   # classic
    ]

ls_rock = get_file_list('./rock_img')
ls_classic = get_file_list('./classic_img')

inp_rock = list()
inp_classic = list()

for i in range(0, len(ls_rock)):

    song = Image.open(ls_rock[i][0])
    hist = histograme.histograme(song)
    hist.create_histograme()
    ls = hist.normalice_histograme()
    inp_rock.append(ls)


for i in range(0, len(ls_classic)):

    song = Image.open(ls_classic[i][0])
    hist = histograme.histograme(song)
    hist.create_histograme()
    ls = hist.normalice_histograme()
    inp_classic.append(ls)


print "\n-TESTING-\n"
miss = 0
r_miss = 0

print "\nRock : \n"
for i in range(0, len(ls_rock)):
    out = net.update(inp_rock[i])
    if out[0] > 0.5:
        print ls_rock[i][1], " - miss"
        r_miss = r_miss + 1
    else:
        print ls_rock[i][1], " - hit"

print "\nnumber of misclassifications = ", r_miss
miss = miss + r_miss

print "\nClassic :\n"
c_miss = 0

for i in range(0, len(ls_classic)):
    out = net.update(inp_classic[i])
    if out[0] <= 0.5:
        print ls_classic[i][1], " - miss"
        c_miss = c_miss + 1
    else:
        print ls_classic[i][1], " - hit"

print "\nnumber of misclassifications = ", c_miss
miss = miss + c_miss

print "\nnumber of total miss classifications = ", miss

total = len(ls_rock) + len(ls_classic)

print "total test data = ", total

print "error = ", float(miss) / float(total)
