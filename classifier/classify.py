# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classify.ui'
#
# Created: Thu May 23 18:46:28 2013
#      by: pyside-uic 0.2.8 running on PySide 1.0.1
#
# WARNING! All changes made in this file will be lost!

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


class Ui_classifier(object):
    def setupUi(self, classifier):
        classifier.setObjectName("classifier")
        classifier.resize(769, 602)
        self.centralwidget = QtGui.QWidget(classifier)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 591, 71))
        self.groupBox.setObjectName("groupBox")
        self.music_file = QtGui.QLineEdit(self.groupBox)
        self.music_file.setGeometry(QtCore.QRect(0, 30, 481, 31))
        self.music_file.setObjectName("music_file")
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 90, 381, 321))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.hist_lable = QtGui.QLabel(self.groupBox_2)
        self.hist_lable.setGeometry(QtCore.QRect(20, 30, 361, 281))
        self.hist_lable.setAutoFillBackground(False)
        self.hist_lable.setStyleSheet("background-color: rgb(53, 57, 54);")
        self.hist_lable.setText("")
        self.hist_lable.setObjectName("hist_lable")
        self.convert = QtGui.QPushButton(self.centralwidget)
        self.convert.setGeometry(QtCore.QRect(240, 410, 141, 31))
        self.convert.setObjectName("convert")
        self.classify = QtGui.QPushButton(self.centralwidget)
        self.classify.setGeometry(QtCore.QRect(400, 410, 141, 31))
        self.classify.setObjectName("classify")
        self.gener = QtGui.QLineEdit(self.centralwidget)
        self.gener.setGeometry(QtCore.QRect(10, 500, 731, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.gener.setFont(font)
        self.gener.setText("")
        self.gener.setObjectName("gener")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 469, 391, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 90, 381, 321))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(10, 30, 361, 281))
        self.label.setStyleSheet("background-color: rgb(53, 57, 54);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.browse = QtGui.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(500, 40, 91, 31))
        self.browse.setObjectName("browse")
        classifier.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(classifier)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 27))
        self.menubar.setObjectName("menubar")
        classifier.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(classifier)
        self.statusbar.setObjectName("statusbar")
        classifier.setStatusBar(self.statusbar)

        self.retranslateUi(classifier)
        QtCore.QMetaObject.connectSlotsByName(classifier)

    def retranslateUi(self, classifier):
        classifier.setWindowTitle(QtGui.QApplication.translate("classifier", "classify music", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("classifier", "Music file :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("classifier", "Histogram :", None, QtGui.QApplication.UnicodeUTF8))
        self.convert.setText(QtGui.QApplication.translate("classifier", "convert", None, QtGui.QApplication.UnicodeUTF8))
        self.classify.setText(QtGui.QApplication.translate("classifier", "classify", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("classifier", "Gener :", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("classifier", "Bit Patten :", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("classifier", "browse", None, QtGui.QApplication.UnicodeUTF8))

