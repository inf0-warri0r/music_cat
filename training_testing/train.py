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
            ls.append(os.path.join(dirname, filename))
    return ls


def save(lst):
    f = open('weights', 'w')
    for l in lst:
        f.write(str(l) + "\n")
    f.close()


def load():
    f = open('weights', 'r')
    cat = f.read()
    f.close()
    weights = list()
    lst = cat.splitlines()
    for i in range(0, len(lst)):
        weights.append(float(lst[i]))

    return weights

net = neural_net.neural(10, 1, 3, 15, 0.001, 0.0)
net.init()

dout = [
    [0.0],  # rock
    [1.0]   # classic
    ]

ls_rock = get_file_list('./rock_img')
ls_classic = get_file_list('./classic_img')

inp_rock = list()
inp_classic = list()

for i in range(0, len(ls_rock)):

    song = Image.open(ls_rock[i])
    hist = histograme.histograme(song)
    hist.create_histograme()
    ls = hist.normalice_histograme()
    inp_rock.append(ls)

for i in range(0, len(ls_classic)):

    song = Image.open(ls_classic[i])
    hist = histograme.histograme(song)
    hist.create_histograme()
    ls = hist.normalice_histograme()
    inp_classic.append(ls)

print "\n-HISTOGRAM TRAINING-\n"

f = str(raw_input("load weights [y / n] : "))
if f == 'y':
    net.put_weights(load())

iterations = int(raw_input("iterations : "))

error = 10

for j in range(0, iterations):
    error = 0.0

    for i in range(0, len(inp_rock)):
        out = net.update(inp_rock[i])
        error = error + 0.5 * (dout[0][0] - out[0]) ** 2.0
        net.learn(dout[0])

    for i in range(0, len(inp_classic)):
        out = net.update(inp_classic[i])
        error = error + 0.5 * (dout[1][0] - out[0]) ** 2.0
        net.learn(dout[1])

    print "iteration = ", j + 1, " error = ", error

print "\n", iterations, " iterations trained !!\n"

weights = net.get_weights()
f = str(raw_input("save weights [y / n] : "))
if f == 'y':
    save(weights)
    print "weights are saved in weights file\n"

print "-DONE-\n"
