# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ENCOSOFTYbzqvr.ui'
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
        MainWindow.resize(1982, 912)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frm_titulo = QFrame(self.frame)
        self.frm_titulo.setObjectName(u"frm_titulo")
        self.frm_titulo.setMaximumSize(QSize(16777215, 40))
        self.frm_titulo.setStyleSheet(u"background-color: rgb(8, 69, 148);")
        self.frm_titulo.setFrameShape(QFrame.StyledPanel)
        self.frm_titulo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frm_titulo)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_9 = QLabel(self.frm_titulo)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.frm_titulo)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Arial Black")
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frm_titulo)

        self.frm_cuerpo = QFrame(self.frame)
        self.frm_cuerpo.setObjectName(u"frm_cuerpo")
        self.frm_cuerpo.setFrameShape(QFrame.StyledPanel)
        self.frm_cuerpo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_cuerpo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frm_cuerpo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(240, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u"Pantalla/images/Recurso3.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_7)

        self.lbltemperatura = QLabel(self.frame_2)
        self.lbltemperatura.setObjectName(u"lbltemperatura")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.lbltemperatura.setFont(font3)
        self.lbltemperatura.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbltemperatura)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setPixmap(QPixmap(u"Pantalla/images/Recurso1.5.png"))
        self.label_8.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_8)

        self.lblhumedad = QLabel(self.frame_2)
        self.lblhumedad.setObjectName(u"lblhumedad")
        self.lblhumedad.setFont(font3)
        self.lblhumedad.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblhumedad)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frm_cuerpo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.grafica = QVBoxLayout()
        self.grafica.setObjectName(u"grafica")

        self.verticalLayout_6.addLayout(self.grafica)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbldt = QLabel(self.frame_7)
        self.lbldt.setObjectName(u"lbldt")
        self.lbldt.setFont(font)
        self.lbldt.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lbldt.setAlignment(Qt.AlignCenter)
        self.lbldt.setMargin(3)

        self.horizontalLayout_5.addWidget(self.lbldt)

        self.lble = QLabel(self.frame_7)
        self.lble.setObjectName(u"lble")
        self.lble.setFont(font)
        self.lble.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lble.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lble)

        self.lblit = QLabel(self.frame_7)
        self.lblit.setObjectName(u"lblit")
        self.lblit.setFont(font)
        self.lblit.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.lblit)


        self.verticalLayout_6.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbldh = QLabel(self.frame_6)
        self.lbldh.setObjectName(u"lbldh")
        self.lbldh.setFont(font)
        self.lbldh.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lbldh.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lbldh)

        self.lblhe = QLabel(self.frame_6)
        self.lblhe.setObjectName(u"lblhe")
        self.lblhe.setFont(font)
        self.lblhe.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblhe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lblhe)

        self.lblih = QLabel(self.frame_6)
        self.lblih.setObjectName(u"lblih")
        self.lblih.setFont(font)
        self.lblih.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblih.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lblih)


        self.verticalLayout_6.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frm_cuerpo)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(240, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_5)

        self.lblventilador = QLabel(self.frame_4)
        self.lblventilador.setObjectName(u"lblventilador")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.lblventilador.setFont(font4)
        self.lblventilador.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblventilador.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblventilador)

        self.lblfocos = QLabel(self.frame_4)
        self.lblfocos.setObjectName(u"lblfocos")
        self.lblfocos.setFont(font4)
        self.lblfocos.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblfocos.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblfocos)

        self.lblelectrovalula = QLabel(self.frame_4)
        self.lblelectrovalula.setObjectName(u"lblelectrovalula")
        self.lblelectrovalula.setFont(font4)
        self.lblelectrovalula.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border radus:20px;\n"
"border: 2px solid a000000;}")
        self.lblelectrovalula.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblelectrovalula)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMouseTracking(False)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnentrenar = QPushButton(self.frame_5)
        self.btnentrenar.setObjectName(u"btnentrenar")
        palette = QPalette()
        brush = QBrush(QColor(36, 161, 156, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btnentrenar.setPalette(palette)
        font5 = QFont()
        font5.setFamily(u"Arial")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setWeight(50)
        self.btnentrenar.setFont(font5)
        self.btnentrenar.setAutoFillBackground(False)
        self.btnentrenar.setStyleSheet(u"background-color: rgb(36, 161, 156);")
        self.btnentrenar.setAutoDefault(False)
        self.btnentrenar.setFlat(False)

        self.horizontalLayout_3.addWidget(self.btnentrenar)

        self.btniniciar = QPushButton(self.frame_5)
        self.btniniciar.setObjectName(u"btniniciar")
        palette1 = QPalette()
        brush1 = QBrush(QColor(228, 88, 38, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.btniniciar.setPalette(palette1)
        self.btniniciar.setFont(font5)
        self.btniniciar.setStyleSheet(u"background-color: rgb(228, 88, 38);")

        self.horizontalLayout_3.addWidget(self.btniniciar)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.frm_cuerpo)

        self.verticalLayout_2.setStretch(0, 1)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btnentrenar.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ENCOSOFT", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Gesti\u00f3n de Incubadora", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Sensores", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Temperatura", None))
        self.label_7.setText("")
        self.lbltemperatura.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Humedad", None))
        self.label_8.setText("")
        self.lblhumedad.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Estado de la Incubadora", None))
        self.lbldt.setText(QCoreApplication.translate("MainWindow", u"Descenso de Temperatura", None))
        self.lble.setText(QCoreApplication.translate("MainWindow", u"Temperatura Estable", None))
        self.lblit.setText(QCoreApplication.translate("MainWindow", u"Incremento de la Temperatura", None))
        self.lbldh.setText(QCoreApplication.translate("MainWindow", u"Descenso de la Humedad", None))
        self.lblhe.setText(QCoreApplication.translate("MainWindow", u"Humedad Estable", None))
        self.lblih.setText(QCoreApplication.translate("MainWindow", u"Incremento de la Humedad ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.lblventilador.setText(QCoreApplication.translate("MainWindow", u"Ventilador", None))
        self.lblfocos.setText(QCoreApplication.translate("MainWindow", u"Focos", None))
        self.lblelectrovalula.setText(QCoreApplication.translate("MainWindow", u"Electrovalvula", None))
        self.btnentrenar.setText(QCoreApplication.translate("MainWindow", u"Entrenar", None))
        self.btniniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
    # retranslateUi

