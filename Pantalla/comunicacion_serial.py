from PySide2.QtCore import QObject #pyqtSignal para pyqt5
import serial, serial.tools.list_ports
#Hilos para comunicacion
from threading import Thread, Event
from tkinter import StringVar ##rescibir datos en string
import re

class Comunicacion(QObject):
    def __init__(self):
        super().__init__()
        self.arduino= serial.Serial()
        self.arduino.timeout= 2

        self.baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']
        self.puertos =[]
        self.t=[]
        self.h=[]

         

    def puertos_disponibles(self):
        self.puertos=[port.device for port in serial.tools.list_ports.comports()]

    def conexion_serial(self):
        try:
            self.arduino.open()
            print('si Conectar')
        except:
            print('Error al Conectar')

    def enviar_datos(self, data):
        if (self.arduino.is_open):
            self.datos = str(data) + "\n"
            self.arduino.write(self.datos.encode())
        else:
            print ('No Conectado')

    #def recibir_datos(self):
        
                  
             

    def desconectar(self):
        self.arduino.close()

