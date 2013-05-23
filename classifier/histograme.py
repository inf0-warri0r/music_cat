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


class histograme:

    def __init__(self, img):

        self.image = img
        self.height = 400
        self.width = 400
        self.ind = {}
        for i in range(0, 256):
            self.ind[i] = 0

    def create_histograme(self):

        pix = self.image.load()
        for y in range(0, self.height):
            for x in range(0, self.width):
                self.ind[pix[x, y][0]] = self.ind[pix[x, y][0]] + 1

    def unnormaliced_histograme(self):
        ls = list()
        for j in range(0, 256):
            n = self.ind[j]
            ls.append(n)
        return ls

    def normalice_histograme(self):

        i = 0
        sm = 0
        ls = list()
        for j in range(0, 256):
            sm = sm + self.ind[j]
            i = i + 1
            if i == 25:
                ls.append(float(sm))
                i = 0
                sm = 0

        c = len(ls) - 1
        ls[c] = ls[c] + sm
        mx = 0.0
        mn = 200000
        for i in range(0, len(ls)):
            if ls[i] > mx:
                mx = ls[i]
            if ls[i] < mn:
                mn = ls[i]

        for i in range(0, len(ls)):
            ls[i] = float(ls[i]) - mn

        mx = mx - mn

        for i in range(0, len(ls)):
            ls[i] = float(ls[i]) / mx + 0.1

        return ls
