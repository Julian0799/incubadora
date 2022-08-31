"""import sys
sys.path.append("../incubadora/Pantalla/datos_entrenamiento")
from datos_entrenamiento import a,b
print(a)
import serial,time
ser=serial.Serial('COM6',38400)
print("conectado")"""
from datetime import datetime

ahora=datetime.now()
print(ahora)
hora=ahora.strftime('%H:%M:%S')
print(hora)

dia=datetime.today().strftime('%A')
print(dia)