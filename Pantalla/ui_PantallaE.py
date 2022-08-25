# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PantallaEjtRmqB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(318, 176)
        icon = QIcon()
        icon.addFile(u"images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblniter = QLineEdit(self.centralwidget)
        self.lblniter.setObjectName(u"lblniter")
        self.lblniter.setGeometry(QRect(190, 40, 113, 20))
        self.lblnneuro = QLineEdit(self.centralwidget)
        self.lblnneuro.setObjectName(u"lblnneuro")
        self.lblnneuro.setGeometry(QRect(190, 90, 113, 20))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 161, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 161, 20))
        self.btnenviar = QPushButton(self.centralwidget)
        self.btnenviar.setObjectName(u"btnenviar")
        self.btnenviar.setGeometry(QRect(170, 140, 75, 23))
        self.btnentrenar = QPushButton(self.centralwidget)
        self.btnentrenar.setObjectName(u"btnentrenar")
        self.btnentrenar.setGeometry(QRect(50, 140, 75, 23))
        self.lblmensaje = QLabel(self.centralwidget)
        self.lblmensaje.setObjectName(u"lblmensaje")
        self.lblmensaje.setGeometry(QRect(30, 10, 261, 16))
        font = QFont()
        font.setFamily(u"Myanmar Text")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblmensaje.setFont(font)
        self.lblmensaje.setStyleSheet(u"\n"
"color:rgb(255, 85, 0)\n"
"")
        self.lblmensaje.setAlignment(Qt.AlignCenter)
        self.btnactualizar = QPushButton(self.centralwidget)
        self.btnactualizar.setObjectName(u"btnactualizar")
        self.btnactualizar.setGeometry(QRect(170, 140, 75, 23))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Red Neuronal", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingrese el n\u00famero de iteraciones:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ingrese el n\u00famero de neuronas:", None))
        self.btnenviar.setText(QCoreApplication.translate("MainWindow", u"Enviar", None))
        self.btnentrenar.setText(QCoreApplication.translate("MainWindow", u"Entrenar", None))
        self.lblmensaje.setText("")
        self.btnactualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
    # retranslateUi

