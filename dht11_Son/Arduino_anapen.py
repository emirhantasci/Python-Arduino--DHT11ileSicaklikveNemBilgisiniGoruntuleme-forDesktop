# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Arduino_anapen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_anapencere(object):
    def setupUi(self, anapencere):
        anapencere.setObjectName("anapencere")
        anapencere.resize(944, 763)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dht11_700p.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        anapencere.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(anapencere)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 301, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 101, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 40, 141, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.port = QtWidgets.QComboBox(self.layoutWidget1)
        self.port.setObjectName("port")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.port.addItem("")
        self.verticalLayout_2.addWidget(self.port)
        self.baudrate = QtWidgets.QComboBox(self.layoutWidget1)
        self.baudrate.setObjectName("baudrate")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.baudrate.addItem("")
        self.verticalLayout_2.addWidget(self.baudrate)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 205, 251, 181))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.portac = QtWidgets.QPushButton(self.layoutWidget2)
        self.portac.setObjectName("portac")
        self.verticalLayout_3.addWidget(self.portac)
        self.portkapat = QtWidgets.QPushButton(self.layoutWidget2)
        self.portkapat.setObjectName("portkapat")
        self.verticalLayout_3.addWidget(self.portkapat)
        self.pb_cikis = QtWidgets.QPushButton(self.centralwidget)
        self.pb_cikis.setGeometry(QtCore.QRect(11, 538, 301, 161))
        self.pb_cikis.setStyleSheet("QPushButton{\n"
"font: 75 10pt \"Magneto\";\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));\n"
"}")
        self.pb_cikis.setObjectName("pb_cikis")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(330, 10, 601, 691))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.progressBar_1 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_1.setGeometry(QtCore.QRect(110, 100, 91, 271))
        self.progressBar_1.setAutoFillBackground(False)
        self.progressBar_1.setStyleSheet("QProgressBar {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);    \n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: rgb(255, 0, 0);   \n"
" }")
        self.progressBar_1.setProperty("value", 1)
        self.progressBar_1.setTextVisible(False)
        self.progressBar_1.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_1.setObjectName("progressBar_1")
        self.progressBar_2 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar_2.setGeometry(QtCore.QRect(400, 100, 91, 271))
        self.progressBar_2.setAutoFillBackground(False)
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }\n"
"\n"
" QProgressBar::chunk {\n"
"     background-color: rgb(85, 255, 255);\n"
" }")
        self.progressBar_2.setProperty("value", 1)
        self.progressBar_2.setTextVisible(False)
        self.progressBar_2.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(256, 80, 81, 321))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Scale.jpg"))
        self.label_9.setScaledContents(False)
        self.label_9.setObjectName("label_9")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(120, 400, 81, 41))
        self.label_7.setStyleSheet("QLabel{\n"
"font: 10pt \"Impact\";\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_88 = QtWidgets.QLabel(self.frame_2)
        self.label_88.setGeometry(QtCore.QRect(416, 400, 61, 31))
        self.label_88.setStyleSheet("QLabel{\n"
"font: 10pt \"Impact\";\n"
"}")
        self.label_88.setObjectName("label_88")
        self.layoutWidget3 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 20, 551, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_5.setStyleSheet("QLabel\n"
"\n"
" {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_6.setStyleSheet("QLabel\n"
"\n"
" {\n"
"     border: 2px solid;\n"
"     border-color: gray;\n"
"     border-radius: 5px;\n"
"     background-color: rgb(255, 255, 255);\n"
" }")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.tablWdht11 = QtWidgets.QTableWidget(self.frame_2)
        self.tablWdht11.setGeometry(QtCore.QRect(12, 441, 581, 241))
        self.tablWdht11.setRowCount(500)
        self.tablWdht11.setColumnCount(4)
        self.tablWdht11.setObjectName("tablWdht11")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 430, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        anapencere.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(anapencere)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 26))
        self.menubar.setObjectName("menubar")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        anapencere.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(anapencere)
        self.statusbar.setObjectName("statusbar")
        anapencere.setStatusBar(self.statusbar)
        self.actionHakk_nda = QtWidgets.QAction(anapencere)
        self.actionHakk_nda.setObjectName("actionHakk_nda")
        self.action_k = QtWidgets.QAction(anapencere)
        self.action_k.setObjectName("action_k")
        self.menuProgram.addAction(self.actionHakk_nda)
        self.menuProgram.addAction(self.action_k)
        self.menubar.addAction(self.menuProgram.menuAction())

        self.retranslateUi(anapencere)
        QtCore.QMetaObject.connectSlotsByName(anapencere)

    def retranslateUi(self, anapencere):
        _translate = QtCore.QCoreApplication.translate
        anapencere.setWindowTitle(_translate("anapencere", "DHT11"))
        self.label_3.setText(_translate("anapencere", "AYARLAR"))
        self.label.setText(_translate("anapencere", "Port:"))
        self.label_2.setText(_translate("anapencere", "Baud Rate"))
        self.port.setItemText(0, _translate("anapencere", "COM1"))
        self.port.setItemText(1, _translate("anapencere", "COM2"))
        self.port.setItemText(2, _translate("anapencere", "COM3"))
        self.port.setItemText(3, _translate("anapencere", "COM4"))
        self.port.setItemText(4, _translate("anapencere", "COM5"))
        self.port.setItemText(5, _translate("anapencere", "COM6"))
        self.port.setItemText(6, _translate("anapencere", "COM7"))
        self.port.setItemText(7, _translate("anapencere", "COM8"))
        self.port.setItemText(8, _translate("anapencere", "COM9"))
        self.baudrate.setItemText(0, _translate("anapencere", "1200"))
        self.baudrate.setItemText(1, _translate("anapencere", "2400"))
        self.baudrate.setItemText(2, _translate("anapencere", "4800"))
        self.baudrate.setItemText(3, _translate("anapencere", "9600"))
        self.portac.setText(_translate("anapencere", "Port Aç"))
        self.portkapat.setText(_translate("anapencere", "Port Kapat"))
        self.pb_cikis.setText(_translate("anapencere", "Cikis"))
        self.label_7.setText(_translate("anapencere", "ISI (C)"))
        self.label_88.setText(_translate("anapencere", "NEM(%)"))
        self.label_8.setText(_translate("anapencere", "TextLabel"))
        self.menuProgram.setTitle(_translate("anapencere", "Program"))
        self.actionHakk_nda.setText(_translate("anapencere", "Hakkında"))
        self.action_k.setText(_translate("anapencere", "Çıkış"))

