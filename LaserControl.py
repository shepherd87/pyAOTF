# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaserControl.ui'
#
# Created: Wed Dec 25 14:29:35 2013
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(556, 579)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.laserLine1Label = QtGui.QLabel(self.centralwidget)
        self.laserLine1Label.setGeometry(QtCore.QRect(30, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine1Label.setFont(font)
        self.laserLine1Label.setObjectName(_fromUtf8("laserLine1Label"))
        self.laserLine1Shutter = QtGui.QCheckBox(self.centralwidget)
        self.laserLine1Shutter.setGeometry(QtCore.QRect(100, 40, 81, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine1Shutter.setFont(font)
        self.laserLine1Shutter.setObjectName(_fromUtf8("laserLine1Shutter"))
        self.laserLine1PowerSlider = QtGui.QSlider(self.centralwidget)
        self.laserLine1PowerSlider.setGeometry(QtCore.QRect(201, 49, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.laserLine1PowerSlider.setFont(font)
        self.laserLine1PowerSlider.setProperty("value", 0)
        self.laserLine1PowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.laserLine1PowerSlider.setObjectName(_fromUtf8("laserLine1PowerSlider"))
        self.laserLine1PulseDuration = QtGui.QLineEdit(self.centralwidget)
        self.laserLine1PulseDuration.setGeometry(QtCore.QRect(360, 20, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine1PulseDuration.setFont(font)
        self.laserLine1PulseDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine1PulseDuration.setObjectName(_fromUtf8("laserLine1PulseDuration"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 20, 16, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.laserLine1Pulse = QtGui.QPushButton(self.centralwidget)
        self.laserLine1Pulse.setGeometry(QtCore.QRect(360, 50, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine1Pulse.setFont(font)
        self.laserLine1Pulse.setObjectName(_fromUtf8("laserLine1Pulse"))
        self.laserLine1PowerEdit = QtGui.QLineEdit(self.centralwidget)
        self.laserLine1PowerEdit.setGeometry(QtCore.QRect(231, 28, 69, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine1PowerEdit.setFont(font)
        self.laserLine1PowerEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine1PowerEdit.setObjectName(_fromUtf8("laserLine1PowerEdit"))
        self.laserLine2Label = QtGui.QLabel(self.centralwidget)
        self.laserLine2Label.setGeometry(QtCore.QRect(30, 100, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine2Label.setFont(font)
        self.laserLine2Label.setObjectName(_fromUtf8("laserLine2Label"))
        self.laserLine2Shutter = QtGui.QCheckBox(self.centralwidget)
        self.laserLine2Shutter.setGeometry(QtCore.QRect(100, 100, 81, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine2Shutter.setFont(font)
        self.laserLine2Shutter.setObjectName(_fromUtf8("laserLine2Shutter"))
        self.laserLine2Pulse = QtGui.QPushButton(self.centralwidget)
        self.laserLine2Pulse.setGeometry(QtCore.QRect(360, 110, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine2Pulse.setFont(font)
        self.laserLine2Pulse.setObjectName(_fromUtf8("laserLine2Pulse"))
        self.laserLine3Shutter = QtGui.QCheckBox(self.centralwidget)
        self.laserLine3Shutter.setGeometry(QtCore.QRect(101, 158, 81, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine3Shutter.setFont(font)
        self.laserLine3Shutter.setObjectName(_fromUtf8("laserLine3Shutter"))
        self.laserLine3Pulse = QtGui.QPushButton(self.centralwidget)
        self.laserLine3Pulse.setGeometry(QtCore.QRect(360, 170, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine3Pulse.setFont(font)
        self.laserLine3Pulse.setObjectName(_fromUtf8("laserLine3Pulse"))
        self.laserLine4Shutter = QtGui.QCheckBox(self.centralwidget)
        self.laserLine4Shutter.setGeometry(QtCore.QRect(101, 229, 81, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine4Shutter.setFont(font)
        self.laserLine4Shutter.setObjectName(_fromUtf8("laserLine4Shutter"))
        self.laserLine4Pulse = QtGui.QPushButton(self.centralwidget)
        self.laserLine4Pulse.setGeometry(QtCore.QRect(360, 240, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine4Pulse.setFont(font)
        self.laserLine4Pulse.setObjectName(_fromUtf8("laserLine4Pulse"))
        self.laserLine5Shutter = QtGui.QCheckBox(self.centralwidget)
        self.laserLine5Shutter.setGeometry(QtCore.QRect(101, 306, 81, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine5Shutter.setFont(font)
        self.laserLine5Shutter.setObjectName(_fromUtf8("laserLine5Shutter"))
        self.laserLine5Pulse = QtGui.QPushButton(self.centralwidget)
        self.laserLine5Pulse.setGeometry(QtCore.QRect(360, 310, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine5Pulse.setFont(font)
        self.laserLine5Pulse.setObjectName(_fromUtf8("laserLine5Pulse"))
        self.laserLine2PowerSlider = QtGui.QSlider(self.centralwidget)
        self.laserLine2PowerSlider.setGeometry(QtCore.QRect(200, 110, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.laserLine2PowerSlider.setFont(font)
        self.laserLine2PowerSlider.setProperty("value", 0)
        self.laserLine2PowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.laserLine2PowerSlider.setObjectName(_fromUtf8("laserLine2PowerSlider"))
        self.laserLine3PowerSlider = QtGui.QSlider(self.centralwidget)
        self.laserLine3PowerSlider.setGeometry(QtCore.QRect(201, 162, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.laserLine3PowerSlider.setFont(font)
        self.laserLine3PowerSlider.setProperty("value", 0)
        self.laserLine3PowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.laserLine3PowerSlider.setObjectName(_fromUtf8("laserLine3PowerSlider"))
        self.laserLine4PowerSlider = QtGui.QSlider(self.centralwidget)
        self.laserLine4PowerSlider.setGeometry(QtCore.QRect(201, 231, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.laserLine4PowerSlider.setFont(font)
        self.laserLine4PowerSlider.setProperty("value", 0)
        self.laserLine4PowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.laserLine4PowerSlider.setObjectName(_fromUtf8("laserLine4PowerSlider"))
        self.laserLine5PowerSlider = QtGui.QSlider(self.centralwidget)
        self.laserLine5PowerSlider.setGeometry(QtCore.QRect(201, 306, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.laserLine5PowerSlider.setFont(font)
        self.laserLine5PowerSlider.setProperty("value", 0)
        self.laserLine5PowerSlider.setOrientation(QtCore.Qt.Horizontal)
        self.laserLine5PowerSlider.setObjectName(_fromUtf8("laserLine5PowerSlider"))
        self.laserLine3Label = QtGui.QLabel(self.centralwidget)
        self.laserLine3Label.setGeometry(QtCore.QRect(30, 157, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine3Label.setFont(font)
        self.laserLine3Label.setObjectName(_fromUtf8("laserLine3Label"))
        self.laserLine4Label = QtGui.QLabel(self.centralwidget)
        self.laserLine4Label.setGeometry(QtCore.QRect(30, 233, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine4Label.setFont(font)
        self.laserLine4Label.setObjectName(_fromUtf8("laserLine4Label"))
        self.laserLine5Label = QtGui.QLabel(self.centralwidget)
        self.laserLine5Label.setGeometry(QtCore.QRect(30, 305, 61, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine5Label.setFont(font)
        self.laserLine5Label.setObjectName(_fromUtf8("laserLine5Label"))
        self.laserLine2PowerEdit = QtGui.QLineEdit(self.centralwidget)
        self.laserLine2PowerEdit.setGeometry(QtCore.QRect(230, 80, 69, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine2PowerEdit.setFont(font)
        self.laserLine2PowerEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine2PowerEdit.setObjectName(_fromUtf8("laserLine2PowerEdit"))
        self.laserLine2PulseDuration = QtGui.QLineEdit(self.centralwidget)
        self.laserLine2PulseDuration.setGeometry(QtCore.QRect(360, 80, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine2PulseDuration.setFont(font)
        self.laserLine2PulseDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine2PulseDuration.setObjectName(_fromUtf8("laserLine2PulseDuration"))
        self.laserLine3PowerEdit = QtGui.QLineEdit(self.centralwidget)
        self.laserLine3PowerEdit.setGeometry(QtCore.QRect(231, 141, 69, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine3PowerEdit.setFont(font)
        self.laserLine3PowerEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine3PowerEdit.setObjectName(_fromUtf8("laserLine3PowerEdit"))
        self.laserLine3PulseDuration = QtGui.QLineEdit(self.centralwidget)
        self.laserLine3PulseDuration.setGeometry(QtCore.QRect(360, 140, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine3PulseDuration.setFont(font)
        self.laserLine3PulseDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine3PulseDuration.setObjectName(_fromUtf8("laserLine3PulseDuration"))
        self.laserLine4PowerEdit = QtGui.QLineEdit(self.centralwidget)
        self.laserLine4PowerEdit.setGeometry(QtCore.QRect(231, 210, 69, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine4PowerEdit.setFont(font)
        self.laserLine4PowerEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine4PowerEdit.setObjectName(_fromUtf8("laserLine4PowerEdit"))
        self.laserLine4PulseDuration = QtGui.QLineEdit(self.centralwidget)
        self.laserLine4PulseDuration.setGeometry(QtCore.QRect(360, 210, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine4PulseDuration.setFont(font)
        self.laserLine4PulseDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine4PulseDuration.setObjectName(_fromUtf8("laserLine4PulseDuration"))
        self.laserLine5PowerEdit = QtGui.QLineEdit(self.centralwidget)
        self.laserLine5PowerEdit.setGeometry(QtCore.QRect(231, 285, 69, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine5PowerEdit.setFont(font)
        self.laserLine5PowerEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine5PowerEdit.setObjectName(_fromUtf8("laserLine5PowerEdit"))
        self.laserLine5PulseDuration = QtGui.QLineEdit(self.centralwidget)
        self.laserLine5PulseDuration.setGeometry(QtCore.QRect(360, 280, 167, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.laserLine5PulseDuration.setFont(font)
        self.laserLine5PulseDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.laserLine5PulseDuration.setObjectName(_fromUtf8("laserLine5PulseDuration"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 70, 501, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 130, 501, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(30, 200, 501, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(30, 270, 501, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setBold(True)
        font.setWeight(75)
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(30, 350, 491, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.line_5.setFont(font)
        self.line_5.setFrameShadow(QtGui.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setMidLineWidth(0)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.status = QtGui.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(30, 510, 481, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName(_fromUtf8("status"))
        self.line_7 = QtGui.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(32, 410, 499, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.line_7.setFont(font)
        self.line_7.setFrameShadow(QtGui.QFrame.Plain)
        self.line_7.setLineWidth(2)
        self.line_7.setMidLineWidth(0)
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(32, 485, 499, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.line_8.setFont(font)
        self.line_8.setFrameShadow(QtGui.QFrame.Plain)
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.seq1Laser1Intensity = QtGui.QLineEdit(self.centralwidget)
        self.seq1Laser1Intensity.setGeometry(QtCore.QRect(233, 431, 91, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seq1Laser1Intensity.setFont(font)
        self.seq1Laser1Intensity.setObjectName(_fromUtf8("seq1Laser1Intensity"))
        self.seq1Laser2Intensity = QtGui.QLineEdit(self.centralwidget)
        self.seq1Laser2Intensity.setGeometry(QtCore.QRect(431, 431, 91, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seq1Laser2Intensity.setFont(font)
        self.seq1Laser2Intensity.setObjectName(_fromUtf8("seq1Laser2Intensity"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(132, 462, 62, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.repeatPulseIndicator = QtGui.QCheckBox(self.centralwidget)
        self.repeatPulseIndicator.setEnabled(True)
        self.repeatPulseIndicator.setGeometry(QtCore.QRect(382, 372, 128, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.repeatPulseIndicator.setFont(font)
        self.repeatPulseIndicator.setCheckable(True)
        self.repeatPulseIndicator.setObjectName(_fromUtf8("repeatPulseIndicator"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(31, 371, 131, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.selectLaserLine = QtGui.QComboBox(self.centralwidget)
        self.selectLaserLine.setGeometry(QtCore.QRect(170, 371, 91, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectLaserLine.setFont(font)
        self.selectLaserLine.setObjectName(_fromUtf8("selectLaserLine"))
        self.selectLaserLine.addItem(_fromUtf8(""))
        self.selectLaserLine.addItem(_fromUtf8(""))
        self.selectLaserLine.addItem(_fromUtf8(""))
        self.selectLaserLine.addItem(_fromUtf8(""))
        self.selectLaserLine.addItem(_fromUtf8(""))
        self.repeatPulseDuration = QtGui.QLineEdit(self.centralwidget)
        self.repeatPulseDuration.setGeometry(QtCore.QRect(275, 371, 101, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.repeatPulseDuration.setFont(font)
        self.repeatPulseDuration.setAlignment(QtCore.Qt.AlignCenter)
        self.repeatPulseDuration.setObjectName(_fromUtf8("repeatPulseDuration"))
        self.seq1NCycles = QtGui.QLineEdit(self.centralwidget)
        self.seq1NCycles.setGeometry(QtCore.QRect(200, 463, 73, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seq1NCycles.setFont(font)
        self.seq1NCycles.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.seq1NCycles.setCursorPosition(2)
        self.seq1NCycles.setAlignment(QtCore.Qt.AlignCenter)
        self.seq1NCycles.setObjectName(_fromUtf8("seq1NCycles"))
        self.seq1Action = QtGui.QPushButton(self.centralwidget)
        self.seq1Action.setGeometry(QtCore.QRect(364, 462, 75, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seq1Action.setFont(font)
        self.seq1Action.setObjectName(_fromUtf8("seq1Action"))
        self.seq1Stop = QtGui.QPushButton(self.centralwidget)
        self.seq1Stop.setEnabled(False)
        self.seq1Stop.setGeometry(QtCore.QRect(445, 462, 75, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seq1Stop.setFont(font)
        self.seq1Stop.setObjectName(_fromUtf8("seq1Stop"))
        self.seq1Laser1Label = QtGui.QComboBox(self.centralwidget)
        self.seq1Laser1Label.setGeometry(QtCore.QRect(133, 431, 91, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seq1Laser1Label.setFont(font)
        self.seq1Laser1Label.setObjectName(_fromUtf8("seq1Laser1Label"))
        self.seq1Laser1Label.addItem(_fromUtf8(""))
        self.seq1Laser1Label.addItem(_fromUtf8(""))
        self.seq1Laser1Label.addItem(_fromUtf8(""))
        self.seq1Laser1Label.addItem(_fromUtf8(""))
        self.seq1Laser1Label.addItem(_fromUtf8(""))
        self.seq1Laser2Label = QtGui.QComboBox(self.centralwidget)
        self.seq1Laser2Label.setGeometry(QtCore.QRect(330, 431, 91, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.seq1Laser2Label.setFont(font)
        self.seq1Laser2Label.setObjectName(_fromUtf8("seq1Laser2Label"))
        self.seq1Laser2Label.addItem(_fromUtf8(""))
        self.seq1Laser2Label.addItem(_fromUtf8(""))
        self.seq1Laser2Label.addItem(_fromUtf8(""))
        self.seq1Laser2Label.addItem(_fromUtf8(""))
        self.seq1Laser2Label.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(33, 431, 94, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 556, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.seq1Laser2Label.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Laser Control", None))
        self.laserLine1Label.setText(_translate("MainWindow", "405 nm", None))
        self.laserLine1Shutter.setText(_translate("MainWindow", "Shutter", None))
        self.laserLine1PulseDuration.setText(_translate("MainWindow", "0.01", None))
        self.label.setText(_translate("MainWindow", "0", None))
        self.label_2.setText(_translate("MainWindow", "99", None))
        self.laserLine1Pulse.setText(_translate("MainWindow", "Pulse", None))
        self.laserLine1PowerEdit.setText(_translate("MainWindow", "0", None))
        self.laserLine2Label.setText(_translate("MainWindow", "488 nm", None))
        self.laserLine2Shutter.setText(_translate("MainWindow", "Shutter", None))
        self.laserLine2Pulse.setText(_translate("MainWindow", "Pulse", None))
        self.laserLine3Shutter.setText(_translate("MainWindow", "Shutter", None))
        self.laserLine3Pulse.setText(_translate("MainWindow", "Pulse", None))
        self.laserLine4Shutter.setText(_translate("MainWindow", "Shutter", None))
        self.laserLine4Pulse.setText(_translate("MainWindow", "Pulse", None))
        self.laserLine5Shutter.setText(_translate("MainWindow", "Shutter", None))
        self.laserLine5Pulse.setText(_translate("MainWindow", "Pulse", None))
        self.laserLine3Label.setText(_translate("MainWindow", "532 nm", None))
        self.laserLine4Label.setText(_translate("MainWindow", "561 nm", None))
        self.laserLine5Label.setText(_translate("MainWindow", "640 nm", None))
        self.laserLine2PowerEdit.setText(_translate("MainWindow", "0", None))
        self.laserLine2PulseDuration.setText(_translate("MainWindow", "0.01", None))
        self.laserLine3PowerEdit.setText(_translate("MainWindow", "0", None))
        self.laserLine3PulseDuration.setText(_translate("MainWindow", "0.01", None))
        self.laserLine4PowerEdit.setText(_translate("MainWindow", "0", None))
        self.laserLine4PulseDuration.setText(_translate("MainWindow", "0.01", None))
        self.laserLine5PowerEdit.setText(_translate("MainWindow", "0", None))
        self.laserLine5PulseDuration.setText(_translate("MainWindow", "0.01", None))
        self.status.setText(_translate("MainWindow", "Status...", None))
        self.label_5.setText(_translate("MainWindow", "Cycles :", None))
        self.repeatPulseIndicator.setText(_translate("MainWindow", "Start Pulsing", None))
        self.label_3.setText(_translate("MainWindow", "Repeat Pulsing:", None))
        self.selectLaserLine.setItemText(0, _translate("MainWindow", "405 nm", None))
        self.selectLaserLine.setItemText(1, _translate("MainWindow", "488 nm", None))
        self.selectLaserLine.setItemText(2, _translate("MainWindow", "532 nm", None))
        self.selectLaserLine.setItemText(3, _translate("MainWindow", "561 nm", None))
        self.selectLaserLine.setItemText(4, _translate("MainWindow", "640 nm", None))
        self.repeatPulseDuration.setText(_translate("MainWindow", "10", None))
        self.seq1NCycles.setText(_translate("MainWindow", "10", None))
        self.seq1Action.setText(_translate("MainWindow", "Action", None))
        self.seq1Stop.setText(_translate("MainWindow", "Stop", None))
        self.seq1Laser1Label.setItemText(0, _translate("MainWindow", "405 nm", None))
        self.seq1Laser1Label.setItemText(1, _translate("MainWindow", "488 nm", None))
        self.seq1Laser1Label.setItemText(2, _translate("MainWindow", "532 nm", None))
        self.seq1Laser1Label.setItemText(3, _translate("MainWindow", "561 nm", None))
        self.seq1Laser1Label.setItemText(4, _translate("MainWindow", "640 nm", None))
        self.seq1Laser2Label.setItemText(0, _translate("MainWindow", "405 nm", None))
        self.seq1Laser2Label.setItemText(1, _translate("MainWindow", "488 nm", None))
        self.seq1Laser2Label.setItemText(2, _translate("MainWindow", "532 nm", None))
        self.seq1Laser2Label.setItemText(3, _translate("MainWindow", "561 nm", None))
        self.seq1Laser2Label.setItemText(4, _translate("MainWindow", "640 nm", None))
        self.label_4.setText(_translate("MainWindow", "Sequence1:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

