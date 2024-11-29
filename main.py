from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
import sys
import pygame
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(322, 528)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 20, 21, 391))
        self.pushButton.setObjectName("pushButton")
        self.Notes = QtWidgets.QButtonGroup(MainWindow)
        self.Notes.setObjectName("Notes")
        self.Notes.addButton(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 20, 21, 391))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Notes.addButton(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 20, 21, 391))
        self.pushButton_3.setObjectName("pushButton_3")
        self.Notes.addButton(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(150, 20, 21, 391))
        self.pushButton_4.setObjectName("pushButton_4")
        self.Notes.addButton(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 20, 21, 391))
        self.pushButton_5.setObjectName("pushButton_5")
        self.Notes.addButton(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 20, 21, 391))
        self.pushButton_6.setObjectName("pushButton_6")
        self.Notes.addButton(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 20, 21, 391))
        self.pushButton_7.setObjectName("pushButton_7")
        self.Notes.addButton(self.pushButton_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фортепиано"))
        self.pushButton.setText(_translate("MainWindow", "D"))
        self.pushButton_2.setText(_translate("MainWindow", "F"))
        self.pushButton_3.setText(_translate("MainWindow", "G"))
        self.pushButton_4.setText(_translate("MainWindow", "H"))
        self.pushButton_5.setText(_translate("MainWindow", "J"))
        self.pushButton_6.setText(_translate("MainWindow", "K"))
        self.pushButton_7.setText(_translate("MainWindow", "L"))


class Piano(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.params = {"D": "note-do.wav",
                       "F": "note-re.wav",
                       "G": "note-mi.wav",
                       "H": "note-fa.wav",
                       "J": "note-sol.wav",
                       "K": "note-lya.wav",
                       "L": "note-si.wav"}
        self.ru_params = {"В": "D",
                          "А": "F",
                          "П": "G",
                          "Р": "H",
                          "О": "J",
                          "Л": "K",
                          "Д": "L"}
        pygame.init()
        pygame.mixer.init()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        for btn in self.Notes.buttons():
            btn.clicked.connect(self.play_sound)

    def play_sound(self):
        filename = self.params[self.sender().text()]
        filename = os.path.abspath(filename)
        pygame.mixer.Sound(filename).play()

    def keyPressEvent(self, event: QKeyEvent):
        key_code = event.key()
        try:
            key = chr(key_code)
            if key in self.ru_params:
                key = self.ru_params[key]
            for btn in self.Notes.buttons():
                if btn.text() == key:
                    btn.animateClick()
        except ValueError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Piano()
    window.show()
    sys.exit(app.exec())
