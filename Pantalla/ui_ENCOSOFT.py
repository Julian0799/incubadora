# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dise�oencosoftldcZas.ui'
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
        MainWindow.resize(1465, 921)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frm_titulo = QFrame(self.frame)
        self.frm_titulo.setObjectName(u"frm_titulo")
        self.frm_titulo.setMaximumSize(QSize(16777215, 40))
        self.frm_titulo.setStyleSheet(u"background-color: rgb(8, 69, 148);")
        self.frm_titulo.setFrameShape(QFrame.StyledPanel)
        self.frm_titulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_titulo)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_10 = QLabel(self.frm_titulo)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_10)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_11 = QLabel(self.frm_titulo)
        self.label_11.setObjectName(u"label_11")
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setBold(True)
        font1.setWeight(75)
        self.label_11.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_11)


        self.verticalLayout.addWidget(self.frm_titulo)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"alternate-background-color: rgb(21, 21, 22);\n"
"background-color: rgb(21, 21, 22);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMaximumSize(QSize(250, 16777215))
        self.frame_14.setStyleSheet(u"background-color: rgb(36, 40, 46);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_4 = QFrame(self.frame_14)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(60, 16777215))
        font2 = QFont()
        font2.setFamily(u"Microsoft Sans Serif")
        font2.setPointSize(10)
        self.label_12.setFont(font2)
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_12.setPixmap(QPixmap(u"../../Incubadora_Tesis/Pantalla/images/logo.png"))
        self.label_12.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        font3 = QFont()
        font3.setFamily(u"Microsoft Sans Serif")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_13)


        self.verticalLayout_11.addWidget(self.frame_4)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMaximumSize(QSize(350, 90))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_15)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.frame_15)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.cbxpuerto = QComboBox(self.frame_15)
        self.cbxpuerto.setObjectName(u"cbxpuerto")
        self.cbxpuerto.setMaximumSize(QSize(300, 40))
        font4 = QFont()
        font4.setPointSize(10)
        self.cbxpuerto.setFont(font4)
        self.cbxpuerto.setStyleSheet(u"background-color: rgb(225, 225, 225);")

        self.gridLayout_2.addWidget(self.cbxpuerto, 1, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMaximumSize(QSize(350, 90))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_16)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.cbxvelocidad = QComboBox(self.frame_16)
        self.cbxvelocidad.setObjectName(u"cbxvelocidad")
        self.cbxvelocidad.setMaximumSize(QSize(300, 40))
        self.cbxvelocidad.setFont(font4)
        self.cbxvelocidad.setStyleSheet(u"background-color: rgb(225, 225, 225);")

        self.gridLayout_3.addWidget(self.cbxvelocidad, 1, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_16)

        self.frame_13 = QFrame(self.frame_14)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_13)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnactualizar = QPushButton(self.frame_13)
        self.btnactualizar.setObjectName(u"btnactualizar")
        self.btnactualizar.setMaximumSize(QSize(125, 16777215))
        self.btnactualizar.setFont(font2)
        self.btnactualizar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(146, 84, 200);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 79);\n"
"border-radius:20px;\n"
"}")

        self.gridLayout.addWidget(self.btnactualizar, 3, 0, 1, 1)

        self.btnconectar = QPushButton(self.frame_13)
        self.btnconectar.setObjectName(u"btnconectar")
        self.btnconectar.setMaximumSize(QSize(125, 16777215))
        self.btnconectar.setFont(font2)
        self.btnconectar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(57, 174, 169);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 79);\n"
"border-radius:20px;\n"
"}")
        self.btnconectar.setIconSize(QSize(15, 15))
        self.btnconectar.setCheckable(False)
        self.btnconectar.setAutoRepeat(False)
        self.btnconectar.setAutoDefault(False)
        self.btnconectar.setFlat(False)

        self.gridLayout.addWidget(self.btnconectar, 0, 0, 1, 1)

        self.btndesconectar = QPushButton(self.frame_13)
        self.btndesconectar.setObjectName(u"btndesconectar")
        self.btndesconectar.setEnabled(True)
        self.btndesconectar.setMaximumSize(QSize(125, 16777215))
        self.btndesconectar.setFont(font2)
        self.btndesconectar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(254, 85, 121);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 79);\n"
"border-radius:20px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btndesconectar, 1, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_18)


        self.horizontalLayout_4.addWidget(self.frame_14)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_5 = QFrame(self.frame_12)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(False)
        font5.setWeight(50)
        self.frame_2.setFont(font5)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.frame_12)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.grafica = QVBoxLayout()
        self.grafica.setObjectName(u"grafica")

        self.verticalLayout_4.addLayout(self.grafica)

        self.verticalSpacer_2 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.frame_19 = QFrame(self.frame_8)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_20 = QFrame(self.frame_19)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setStyleSheet(u"background-color: rgb(36, 40, 46);")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_20)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.frame_20)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_5.setFont(font7)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.frame_20)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(150, 150))
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setPixmap(QPixmap(u"../../Incubadora_Tesis/Pantalla/images/Recurso3.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.lbltemperatura = QLabel(self.frame_20)
        self.lbltemperatura.setObjectName(u"lbltemperatura")
        self.lbltemperatura.setMaximumSize(QSize(16777215, 50))
        self.lbltemperatura.setFont(font7)
        self.lbltemperatura.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbltemperatura.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lbltemperatura, 2, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_20)

        self.horizontalSpacer_3 = QSpacerItem(30, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"background-color: rgb(36, 40, 46);")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_21)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_6 = QLabel(self.frame_21)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setFont(font7)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_21)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(150, 150))
        self.label_8.setFrameShadow(QFrame.Raised)
        self.label_8.setPixmap(QPixmap(u"../../Incubadora_Tesis/Pantalla/images/Recurso1.5.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 1, 0, 1, 1)

        self.lblhumedad = QLabel(self.frame_21)
        self.lblhumedad.setObjectName(u"lblhumedad")
        self.lblhumedad.setMaximumSize(QSize(16777215, 50))
        self.lblhumedad.setFont(font7)
        self.lblhumedad.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lblhumedad.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lblhumedad, 2, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_21)


        self.verticalLayout_4.addWidget(self.frame_19)


        self.verticalLayout_7.addWidget(self.frame_8)

        self.frame_17 = QFrame(self.frame_12)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(300, 50))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lblestado = QLabel(self.frame_17)
        self.lblestado.setObjectName(u"lblestado")
        self.lblestado.setMaximumSize(QSize(190, 70))
        self.lblestado.setFont(font3)
        self.lblestado.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.lblestado)

        self.lblverde = QLabel(self.frame_17)
        self.lblverde.setObjectName(u"lblverde")
        self.lblverde.setMaximumSize(QSize(25, 30))
        self.lblverde.setPixmap(QPixmap(u"../../Incubadora_Tesis/Pantalla/images/verde.png"))
        self.lblverde.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.lblverde)

        self.lblrojo = QLabel(self.frame_17)
        self.lblrojo.setObjectName(u"lblrojo")
        self.lblrojo.setMaximumSize(QSize(25, 30))
        self.lblrojo.setPixmap(QPixmap(u"../../Incubadora_Tesis/Pantalla/images/rojo.png"))
        self.lblrojo.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.lblrojo)


        self.verticalLayout_7.addWidget(self.frame_17)


        self.horizontalLayout_4.addWidget(self.frame_12)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(500, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_14)

        self.frame_7 = QFrame(self.frame_9)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbldt = QLabel(self.frame_7)
        self.lbldt.setObjectName(u"lbldt")
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setWeight(75)
        font8.setKerning(True)
        self.lbldt.setFont(font8)
        self.lbldt.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lbldt.setAlignment(Qt.AlignCenter)
        self.lbldt.setWordWrap(True)
        self.lbldt.setMargin(3)

        self.horizontalLayout_5.addWidget(self.lbldt)

        self.lble = QLabel(self.frame_7)
        self.lble.setObjectName(u"lble")
        font9 = QFont()
        font9.setFamily(u"Arial")
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setWeight(75)
        self.lble.setFont(font9)
        self.lble.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lble.setAlignment(Qt.AlignCenter)
        self.lble.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lble)

        self.lblit = QLabel(self.frame_7)
        self.lblit.setObjectName(u"lblit")
        self.lblit.setFont(font9)
        self.lblit.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblit.setAlignment(Qt.AlignCenter)
        self.lblit.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.lblit)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbldh = QLabel(self.frame_6)
        self.lbldh.setObjectName(u"lbldh")
        self.lbldh.setFont(font9)
        self.lbldh.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lbldh.setAlignment(Qt.AlignCenter)
        self.lbldh.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.lbldh)

        self.lblhe = QLabel(self.frame_6)
        self.lblhe.setObjectName(u"lblhe")
        self.lblhe.setFont(font9)
        self.lblhe.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblhe.setAlignment(Qt.AlignCenter)
        self.lblhe.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.lblhe)

        self.lblih = QLabel(self.frame_6)
        self.lblih.setObjectName(u"lblih")
        self.lblih.setFont(font9)
        self.lblih.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblih.setAlignment(Qt.AlignCenter)
        self.lblih.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.lblih)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_9)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lblventilador = QLabel(self.frame_11)
        self.lblventilador.setObjectName(u"lblventilador")
        self.lblventilador.setFont(font9)
        self.lblventilador.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblventilador.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lblventilador)

        self.lblfocos = QLabel(self.frame_11)
        self.lblfocos.setObjectName(u"lblfocos")
        self.lblfocos.setFont(font9)
        self.lblfocos.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblfocos.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lblfocos)

        self.lblelectrovalula = QLabel(self.frame_11)
        self.lblelectrovalula.setObjectName(u"lblelectrovalula")
        self.lblelectrovalula.setFont(font9)
        self.lblelectrovalula.setStyleSheet(u"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 40, 46);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblelectrovalula.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.lblelectrovalula)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMouseTracking(False)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnentrenar = QPushButton(self.frame_10)
        self.btnentrenar.setObjectName(u"btnentrenar")
        self.btnentrenar.setMaximumSize(QSize(125, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(57, 174, 169, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(21, 21, 22, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.btnentrenar.setPalette(palette)
        font10 = QFont()
        font10.setFamily(u"Arial")
        font10.setPointSize(10)
        font10.setBold(False)
        font10.setWeight(50)
        self.btnentrenar.setFont(font10)
        self.btnentrenar.setAutoFillBackground(False)
        self.btnentrenar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(57, 174, 169);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 79);\n"
"border-radius:20px;\n"
"}")
        self.btnentrenar.setAutoDefault(False)
        self.btnentrenar.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btnentrenar)

        self.btnterminar = QPushButton(self.frame_10)
        self.btnterminar.setObjectName(u"btnterminar")
        self.btnterminar.setMaximumSize(QSize(125, 16777215))
        self.btnterminar.setFont(font4)
        self.btnterminar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(254, 85, 121);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 79);\n"
"border-radius:20px;\n"
"}")
        self.btnterminar.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btnterminar)

        self.btniniciar = QPushButton(self.frame_10)
        self.btniniciar.setObjectName(u"btniniciar")
        self.btniniciar.setMaximumSize(QSize(125, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush6 = QBrush(QColor(254, 85, 121, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush2)
        brush7 = QBrush(QColor(255, 255, 255, 128))
        brush7.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush2)
        brush8 = QBrush(QColor(255, 255, 255, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush2)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        self.btniniciar.setPalette(palette1)
        self.btniniciar.setFont(font10)
        self.btniniciar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(254, 85, 121);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(53, 53, 79);\n"
"border-radius:20px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.btniniciar)


        self.verticalLayout_5.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btnconectar.setDefault(False)
        self.btnentrenar.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Incubadora", None))
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Comunicaci\u00f3n Serial", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Baud Rate:", None))
        self.btnactualizar.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnconectar.setText(QCoreApplication.translate("MainWindow", u"Conectar", None))
        self.btndesconectar.setText(QCoreApplication.translate("MainWindow", u"Desconectar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ESTADO DE LA INCUBADORA", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sensores", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.label_7.setText("")
        self.lbltemperatura.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Humedad", None))
        self.label_8.setText("")
        self.lblhumedad.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.lblestado.setText(QCoreApplication.translate("MainWindow", u"Estado:             ", None))
        self.lblverde.setText("")
        self.lblrojo.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Estados", None))
        self.lbldt.setText(QCoreApplication.translate("MainWindow", u"Descenso de Temperatura", None))
        self.lble.setText(QCoreApplication.translate("MainWindow", u"Temperatura Estable", None))
        self.lblit.setText(QCoreApplication.translate("MainWindow", u"Incremento de la Temperatura", None))
        self.lbldh.setText(QCoreApplication.translate("MainWindow", u"Descenso de la Humedad", None))
        self.lblhe.setText(QCoreApplication.translate("MainWindow", u"Humedad       Estable", None))
        self.lblih.setText(QCoreApplication.translate("MainWindow", u"Incremento de la Humedad ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.lblventilador.setText(QCoreApplication.translate("MainWindow", u"Ventilador", None))
        self.lblfocos.setText(QCoreApplication.translate("MainWindow", u"Resistencia", None))
        self.lblelectrovalula.setText(QCoreApplication.translate("MainWindow", u"Electrovalvula", None))
        self.btnentrenar.setText(QCoreApplication.translate("MainWindow", u"Entrenar", None))
        self.btnterminar.setText(QCoreApplication.translate("MainWindow", u"Terminar", None))
        self.btniniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
    # retranslateUi

