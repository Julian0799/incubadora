from bdb import Breakpoint
import sys
from timeit import repeat #libreria basica
from unicodedata import name
from ui_ENCOSOFT import * #interfaz
from PySide2 import QtCore 
import serial
import time
import numpy as np
import re
from tkinter import Canvas #grafica
from unicodedata import name
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
try:
    ser = serial.Serial ("com4",38400)
    print("Conectado") 
             
except TimeoutError:
    print ("error")
finally:
    print ("done")
    

class Incuabdora(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  
        #self.ui.btniniciar.setEnabled()
        #self.ui.btniniciar.setVisible(False)
        self.ui.btnentrenar.clicked.connect(self.btn_entrenar)
        self.ui.btniniciar.clicked.connect(self.btn_Iniciar)
        #self.ser= serial.Serial ("com4",38400)
        
        #grafica
        self.grafica=Canvas_grafica()  
        self.ui.grafica.addWidget(self.grafica)
    #///////////////////////////////////////// 
    def btn_entrenar(self):
        print("Function 1 is active")
        import entrenamiento
        #self.ui.btniniciar.setEnabled(True)
        #self.ui.btnentrenar.setEnabled(False)
    #/////////////////////////////////////////
    def btn_Iniciar(self):
        #self.ui.btnterminar.setVisible(True)  
        
        for i in range(1):
            
            if ser.in_waiting:
                packet = ser.readline()
                #print(packet.decode('utf'))
                a=([float(s) for s in re.findall(r'-?\d+\.?\d*', packet.decode('utf'))])
                #print(a)
                for x in range(len(a)-1):
                    t=(a[0])
                    h=(a[1])
                    print (t)
                    print (h)
                    self.ui.lbltemperatura.setText(str(t)+" °C")
                    self.ui.lblhumedad.setText(str(h)+" %")
                    if (t<36.5):
                        self.ui.lblfocos.setStyleSheet("background:#FCFFA6;border: 2px solid a000000")
                        self.ui.lblventilador.setStyleSheet("background:white;border: 2px solid a000000")
                        self.ui.lbldt.setStyleSheet("background:orange;border: 2px solid a000000")
                        self.ui.lble.setStyleSheet("background:white;border: 2px solid a000000")
                        self.ui.lblit.setStyleSheet("background:white;border: 2px solid a000000")
                        
                        
                    else:
                        if (t>37.8):
                            self.ui.lblventilador.setStyleSheet("background:#B8FFF9;border: 2px solid a000000")
                            self.ui.lblfocos.setStyleSheet("background:white;border: 2px solid a000000")
                            self.ui.lblit.setStyleSheet("background:red;border: 2px solid a000000")
                            self.ui.lble.setStyleSheet("background:white;border: 2px solid a000000")
                            self.ui.lbldt.setStyleSheet("background:white;border: 2px solid a000000")
                        else:
                            if(t>=36.5 and t<=37.8): 
                                self.ui.lblfocos.setStyleSheet("background:#FCFFA6;border: 2px solid a000000")
                                self.ui.lblventilador.setStyleSheet("background:white;border: 2px solid a000000")
                                self.ui.lble.setStyleSheet("background:green;border: 2px solid a000000")
                                self.ui.lbldt.setStyleSheet("background:white;border: 2px solid a000000")
                                self.ui.lblit.setStyleSheet("background:white;border: 2px solid a000000")
                    if (h<55):
                        print('humedad baja')
                        self.ui.lbldh.setStyleSheet("background:orange;border: 2px solid a000000")
                        self.ui.lblfocos.setStyleSheet("background:#FFFDDE;border: 2px solid a000000")
                        self.ui.lblelectrovalula.setStyleSheet("background:#FFB5B5;border: 2px solid a000000")
                        self.ui.lblhe.setStyleSheet("background:white;border: 2px solid a000000")
                        self.ui.lblih.setStyleSheet("background:white;border: 2px solid a000000")
                    else:
                        if (h>85):
                            print('humedad alta')
                            self.ui.lblih.setStyleSheet("background:red;border: 2px solid a000000")
                            self.ui.lblelectrovalula.setStyleSheet("background:#FF5959;border: 2px solid a000000")
                            self.ui.lblfocos.setStyleSheet("background:white;border: 2px solid a000000")
                            self.ui.lblhe.setStyleSheet("background:white;border: 2px solid a000000")
                            self.ui.lbldh.setStyleSheet("background:white;border: 2px solid a000000")
                        else:
                            if(h>=55 and h<=85):
                                print('humedad estable') 
                                self.ui.lblhe.setStyleSheet("background:green;border: 2px solid a000000") 
                                self.ui.lbldh.setStyleSheet("background:white;border: 2px solid a000000")
                                self.ui.lblih.setStyleSheet("background:white;border: 2px solid a000000")
            
class Canvas_grafica(FigureCanvas):
    def __init__(self,parent=None):
      self.fig , self.ax = plt.subplots(1, dpi=100, figsize=(5, 5),
          sharey=True, facecolor='white') 
      super().__init__(self.fig)
      self.fig.suptitle('Grafica de Datos',size=9)
      np.random. seed(20)
      y = np.random.randn(150).cumsum()
      self.ax = plt.axes()
      plt.plot(y, color='magenta')
                       
            
        

      
if __name__ == "__main__":
  app=QApplication(sys.argv)   
  mi_app=Incuabdora()
  mi_app.show()
  sys.exit(app.exec_())   