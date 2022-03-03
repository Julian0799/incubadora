import numpy as np
import serial
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