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

import Image


class plot:

    def __init__(self, lst, w, h, color, b):
        self.ls = lst
        self.pls = list()
        self.length = float(len(lst))
        self.width = float(w)
        self.height = float(h)
        self.image = Image.new("RGBA", (w, h))
        self.scale_x = 0.0
        self.scale_y = 0.0
        self.mx = 0.0
        self.mn = 0.0
        self.color = color
        self.back = b
        p = self.image.load()
        for i in range(0, w):
            for j in range(0, h):
                p[i, j] = self.back

    def set_scales(self):
        self.scale_x = self.length / self.width
        ls = sorted(self.ls)
        self.mx = float(ls[int(self.length) - 1])
        self.mn = float(ls[0])
        self.scale_y = (self.mx - self.mn) / self.height

    def set_plot(self):
        self.pls = list()
        for i in range(0, int(self.width)):
            v = self.ls[int(i * self.scale_x)] - self.mn
            self.pls.append(v / self.scale_y)

    def draw(self, name):
        p = self.image.load()
        for x in range(0, int(self.width)):
            y = self.height - self.pls[x]
            if y == self.height:
                y = self.height - 1
            for i in range(int(self.height) - 1, int(y), -1):

                p[x, i] = self.color
        self.image.save(name)
