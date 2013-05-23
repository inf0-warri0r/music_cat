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

from PIL import Image


class file_read:

    def __init__(self, file_info):
        self.file_name = file_info[0]
        self.file_path = file_info[1]
        self.height = 400
        self.width = 400
        self.image = Image.new("RGB", (self.width, self.height))

    def convert(self):

        f = open(self.file_path, 'r')
        cat = f.read()
        f.close()
        start = len(cat) / 2 - 400 * 200
        pix = self.image.load()

        for y in range(0, self.height):
            for x in range(0, self.width):

                g = ord(cat[y * self.height + x + start])
                pix[x, y] = g, g, g

    def save(self, dr):
        self.image.save(dr + '/' + self.file_name + ".jpg")
