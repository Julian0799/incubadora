import sys
import numpy as np
from pantalla import *

import serial
from PySide2 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAge as FigureCanvas
import matplotlib.pyplot as plt
class MiApp(QMainwindow):
    def _init_(self):
        super ()._init_()
        self.ui = Ui_Mainwindow()
        self.ui.setupUi(self)
                 
        self.grafica = Canvas grafica()
        
        
                       
                          
        self.ui.grafica_uno.addwidget(self.grafica)
        self.ui.grafica_dos.addWidget(self.grafica1)
        self.ui.grafica_tres.addWidget(self.grafica2)
        self.ui.grafica_cuatro.addwidget(self.grafica3)                                                          
"""
ser=serial.Serial("COM5", 34800)
edad = input('¿Encender led 1-->on #-->of ? ')
if edad=='1':
 ser.write(b'1')
else: 
 ser.write(b'0')

#print (edad)
#String=ser.readline()
#print(String)



while (1):
  while(ser.inWaiting()==0):
   datoString=ser.readline()
   a=datoString.splitlines()
   b=str(a[0])
   c=b.replace("d","")
   d=c.replace("'","")
   g=(d)
   print (g)

ser.close
"""