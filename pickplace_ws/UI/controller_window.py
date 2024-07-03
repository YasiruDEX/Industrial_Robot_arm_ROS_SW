# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controller_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(200, 130)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(200, 130))
        Form.setMaximumSize(QtCore.QSize(346, 158))
        self.move_to_initial_position_pushButton = QtWidgets.QPushButton(Form)
        self.move_to_initial_position_pushButton.setGeometry(QtCore.QRect(10, 10, 171, 25))
        self.move_to_initial_position_pushButton.setObjectName("move_to_initial_position_pushButton")
        self.pick_up_pushButton = QtWidgets.QPushButton(Form)
        self.pick_up_pushButton.setGeometry(QtCore.QRect(10, 40, 171, 25))
        self.pick_up_pushButton.setObjectName("pick_up_pushButton")
        self.place_on_red_pushButton = QtWidgets.QPushButton(Form)
        self.place_on_red_pushButton.setGeometry(QtCore.QRect(10, 100, 171, 25))
        self.place_on_red_pushButton.setObjectName("place_on_red_pushButton")
        self.grab_pushButton = QtWidgets.QPushButton(Form)
        self.grab_pushButton.setGeometry(QtCore.QRect(10, 70, 81, 25))
        self.grab_pushButton.setObjectName("grab_pushButton")
        self.open_pushButton = QtWidgets.QPushButton(Form)
        self.open_pushButton.setGeometry(QtCore.QRect(100, 70, 81, 25))
        self.open_pushButton.setObjectName("open_pushButton")

        self.retranslateUi(Form)
        self.move_to_initial_position_pushButton.clicked.connect(Form.Move_to_initial_position)
        self.pick_up_pushButton.clicked.connect(Form.Pick_up_the_block)
        self.place_on_red_pushButton.clicked.connect(Form.Place_on_red)
        self.grab_pushButton.clicked.connect(Form.Grab)
        self.open_pushButton.clicked.connect(Form.Open)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "controller"))
        self.move_to_initial_position_pushButton.setText(_translate("Form", "Move to initial position"))
        self.pick_up_pushButton.setText(_translate("Form", "Move the arm"))
        self.place_on_red_pushButton.setText(_translate("Form", "Place on a red cylinder"))
        self.grab_pushButton.setText(_translate("Form", "Grab"))
        self.open_pushButton.setText(_translate("Form", "Open"))
