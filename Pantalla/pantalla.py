#Importamos librerias
import sys
from ui_ENCOSOFT import * #interfaz
from comunicacion_serial import Comunicacion
from PySide2.QtCore import QTimer
import serial, serial.tools.list_ports
import re
import pymongo
#datos de conexion 
host="localhost"
puerto="27017"
tiempo="1000"
url="mongodb://"+host+":"+puerto+"/"
#acceder base de datos
bd="incubadora"
tabla="lecturas"
#Generamos un hilo
# Import Library
from tkinter import *
# Create Object
root = Tk()
# Set title
root.title("Main Window")
# Set Geometry
root.geometry("200x200")
root.withdraw()

#Clase donde se maneja los witgets
class Incuabdora(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Escondemos los botones 
        self.ui.btndesconectar.setVisible(False)
        self.ui.btnterminar.setVisible(False)
        self.ui.lblverde.setVisible(False)
        self.ui.lblestado.setText("Estado: Desconectado")
        self.ui.btniniciar.setEnabled(False)
        #Establecer comunicación
        self.serial=Comunicacion()
        self.puertos_disponible() 
        #Añadimos las listas al cuadro de lista
        self.ui.cbxvelocidad.addItems(self.serial.baudrates)
        self.ui.cbxvelocidad.setCurrentText("38400")
        #Codigo de botones
        self.ui.btnconectar.clicked.connect(self.conectar)
        self.ui.btnactualizar.clicked.connect(self.puertos_disponible)
        self.ui.btndesconectar.clicked.connect (self.desconectar)
        self.ui.btniniciar.clicked.connect (self.iniciar)
        self.ui.btnterminar.clicked.connect (self.terminar)
    #Funciones
    def conectar(self):
        port = self.ui.cbxpuerto.currentText()
        baud = self.ui.cbxvelocidad.currentText()
        self.serial.arduino.port=port
        self.serial.arduino.baudrate=baud
        self.serial.conexion_serial()
        self.ui.lblestado.setText("Estado: Conectado")
        self.ui.lblrojo.setVisible(False)
        self.ui.lblverde.setVisible(True)
        self.ui.btndesconectar.setVisible(True)
        self.ui.btnconectar.setVisible(False)
        self.ui.btniniciar.setEnabled(True)
    def desconectar(self):
        self.serial.desconectar()
        self.ui.lblestado.setText("Estado: Desconectado")
        self.ui.lblverde.setVisible(False)
        self.ui.lblrojo.setVisible(True)
        self.ui.btndesconectar.setVisible(False)
        self.ui.btnconectar.setVisible(True)
        self.ui.btnterminar.setVisible(False)
        self.ui.btniniciar.setVisible(True)
        self.ui.btniniciar.setEnabled(False)   
    def puertos_disponible(self):
        self.serial.puertos_disponibles()
        self.ui.cbxpuerto.clear()
        self.ui.cbxpuerto.addItems(self.serial.puertos)
    def iniciar(self):
        self.serial.conexion_serial()
        self.ui.btnterminar.setVisible(True)
        self.ui.btniniciar.setVisible(False)
        self.ui.btnentrenar.setEnabled(False)
        while True:
         #for i in range (1):
            packet = self.serial.arduino.readline()
            print(packet.decode('utf'))
            a=([float(s) for s in re.findall(r'-?\d+\.?\d*', packet.decode('utf'))])
            print(a)
            
            #b=packet
            
            #archivo=open("lecturas.txt","a")
            
            #archivo.write((str(b))+"\n")
            
            #archivo.close()
            
            for x in range(len(a)-9):
                t=(a[0])
                h=(a[1])
                nt=int((a[2]))
                nh=int((a[3]))
                sv=int((a[5]))
                sr=int((a[7]))
                se=int((a[9]))
                print (t)
                print (h)
                print (nt)
                print (nh)
                print (sv)
                print (sr)
                print (se)
                #conexion al servidor
                try:
                    cliente=pymongo.MongoClient(url,serverSelectionTimeoutMS=tiempo)
                    baseDatos=cliente[bd]
                    datatabla=baseDatos[tabla]
                    datatabla.insert_one({
                        "temperatura": t,
                        "humedad": h,
                        "nortemp": nt,
                        "norhum": nh,
                        "salidav": sv,
                        "salidar": sr,
                        "salidae": se
                    }) 
                    #cliente.server_info()
                    #print("conexión a mongo exitosa")
                    #cliente.close()
                    
                except pymongo.errors.ServerSelectionTimeoutError as error_tiempo:
                    print("tiempo exedido"+error_tiempo)
                except pymongo.errors.ConnectionFailure as errorConexion:
                    print("Fallo al conectarse"+errorConexion)
                self.ui.lbltemperatura.setText(str(t)+" °C")
                self.ui.lblhumedad.setText(str(h)+" %")
                if (t<36.5):
                    self.ui.lblfocos.setStyleSheet("background:#FCFFA6;border: 2px solid a000000")
                    self.ui.lblventilador.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                    self.ui.lbldt.setStyleSheet("background:orange;border: 2px solid a000000")
                    self.ui.lble.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                    self.ui.lblit.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                        
                        
                else:
                    if (t>37.8):
                        self.ui.lblventilador.setStyleSheet("background:#B8FFF9;border: 2px solid a000000")
                        self.ui.lblfocos.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                        self.ui.lblit.setStyleSheet("background:red;border: 2px solid a000000")
                        self.ui.lble.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                        self.ui.lbldt.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                    else:
                        if(t>=36.5 and t<=37.8): 
                            self.ui.lblfocos.setStyleSheet("background:#FCFFA6;border: 2px solid a000000")
                            self.ui.lblventilador.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                            self.ui.lble.setStyleSheet("background:green;border: 2px solid a000000")
                            self.ui.lbldt.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                            self.ui.lblit.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                if (h<55):
                    print('humedad baja')
                    self.ui.lbldh.setStyleSheet("background:orange;border: 2px solid a000000")
                    self.ui.lblfocos.setStyleSheet("background:#FFFDDE;border: 2px solid a000000")
                    self.ui.lblelectrovalula.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                    self.ui.lblhe.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                    self.ui.lblih.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                else:
                    if (h>85):
                        print('humedad alta')
                        self.ui.lblih.setStyleSheet("background:red;border: 2px solid a000000")
                        self.ui.lblelectrovalula.setStyleSheet("background:#FF5959;border: 2px solid a000000")
                        self.ui.lblfocos.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                        self.ui.lblhe.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                        self.ui.lbldh.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                    else:
                        if(h>=55 and h<=85):
                            print('humedad estable') 
                            self.ui.lblhe.setStyleSheet("background:green;border: 2px solid a000000") 
                            self.ui.lbldh.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
                            self.ui.lblih.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
            
            root.update()    
    def terminar(self):
        #Escondemos los botones
        self.serial.desconectar()
        self.ui.lblestado.setText("Estado: Desconectado")
        self.ui.lblrojo.setVisible(True)
        self.ui.lblverde.setVisible(False)
        self.ui.btndesconectar.setVisible(False)
        self.ui.btnterminar.setVisible(False)
        self.ui.btnconectar.setVisible(True)
        self.ui.btniniciar.setVisible(True)
        self.ui.btnentrenar.setEnabled(True)
        self.ui.btniniciar.setEnabled(False)
        #limpiamos lbls
        self.ui.lbltemperatura.setText("°C")
        self.ui.lblhumedad.setText("%")
        self.ui.lblventilador.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
        self.ui.lblfocos.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
        self.ui.lblelectrovalula.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
        self.ui.lblhe.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
        self.ui.lble.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
        self.ui.lbldh.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
        self.ui.lbldt.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
        self.ui.lblit.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")
        self.ui.lblih.setStyleSheet("color: rgb(255, 255, 255);background-color: rgb(36, 40, 46);border: 2px solid a000000")



#Codigo para ejecutar la aplicación
if __name__ == "__main__":
  app=QApplication(sys.argv)   
  mi_app=Incuabdora()
  mi_app.show()
  sys.exit(app.exec_())   
# Execute Tkinter
root.mainloop()
