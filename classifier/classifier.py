#!/usr/bin/env python

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

from PySide import QtCore, QtGui
from classify import Ui_classifier
import os
import sys
import file_read
import histograme
import thread
import neural_net
import plot


class MyWidget(QtGui.QMainWindow, Ui_classifier):
    def __init__(self, parent=None):
        super(MyWidget, self).__init__(parent)
        self.setupUi(self)
        self.file_name = ""
        self.hist_u = list()
        self.hist_n = list()
        self.net = neural_net.neural(10, 1, 3, 15, 0.001, 0.0)
        self.net.init()
        self.net.put_weights(self.load())

        self.img = ""

        self.convert.clicked.connect(self.convert_file)
        self.classify.clicked.connect(self.classify_func)
        self.browse.clicked.connect(self.browse_func)
        self.hist_lable.setScaledContents(True)
        self.run = True
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.re_draw)
        self.timer.start()

    def browse_func(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file')

        self.music_file.setText(str(fname))

    def re_draw(self):
        if not self.run:
            QtGui.QMessageBox.about(self, "Done", "Done !!!")
            self.run = True
            return 0

    def convert_file(self):
        r, w = os.pipe()
        self.file_name = self.music_file.text()
        if self.file_name == "":
            QtGui.QMessageBox.about(self, "ERROR", "invaild file")
            return 0
        pid = os.fork()
        if pid:
            os.waitpid(pid, 0)
        else:
            os.execlp("ffmpeg", "ffmpeg", "-i",
                self.file_name, "-y", "out.aif")
            exit(0)

        try:
            thread.start_new_thread(self.thread_func, ())
        except Exception:
            QtGui.QMessageBox.about(self, "ERROR", "thread error")

    def thread_func(self):
        self.run = True
        f = file_read.file_read(("out.aif", "out.aif"))
        f.convert()
        f.save("./")
        self.image = f.image

        h = histograme.histograme(f.image)
        h.create_histograme()
        self.hist_u = h.unnormaliced_histograme()
        self.hist_n = h.normalice_histograme()

        print "done"
        self.run = False

    def classify_func(self):

        p = plot.plot(self.hist_u, 600, 400, (256, 125, 0), (256, 256, 256))
        p.set_scales()
        p.set_plot()
        p.draw("hist.jpg")

        qimage = QtGui.QImage("out.aif.jpg")
        pix = QtGui.QPixmap.fromImage(qimage)
        self.label.setPixmap(pix)

        qimage = QtGui.QImage("hist.jpg")
        pix = QtGui.QPixmap.fromImage(qimage)
        self.hist_lable.setPixmap(pix)

        try:
            thread.start_new_thread(self.thread_func2, ())
        except Exception:
            QtGui.QMessageBox.about(self, "ERROR", "thread error")

    def thread_func2(self):
        print self.hist_n
        out = self.net.update(self.hist_n)
        print out
        self.gener.setText("")

        if out[0] < 0.5:
            self.type = "Rock"
        else:
            self.type = "Classic"

        self.gener.setText(self.type)

    def load(self):
        f = open('weights', 'r')
        cat = f.read()
        f.close()
        weights = list()
        lst = cat.splitlines()
        for i in range(0, len(lst)):
            weights.append(float(lst[i]))

        return weights


if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec_())
