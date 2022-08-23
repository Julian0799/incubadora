from distutils.log import set_verbosity
from tokenize import Hexnumber
import pymongo
import numpy as np
#datos de conexion 
host="localhost"
puerto="27017"
tiempo="1000"
url="mongodb://"+host+":"+puerto+"/"
#acceder base de datos
bd="incubadora"
tabla="lecturas"
#variables
"""temp=float(input("ingrese la temperatura"))
hum=float(input("ingrese la humedad"))
nt=int(input("ingrese la normalizacion"))
nh=int(input("ingrese la normalizacion"))
sv=int(input("ingrese la normalizacion"))
sr=int(input("ingrese la normalizacion"))
se=int(input("ingrese la normalizacion"))
"""
val=[]
#conexion al servidor
try:
    cliente=pymongo.MongoClient(url,serverSelectionTimeoutMS=tiempo)
    baseDatos=cliente[bd]
    datatabla=baseDatos[tabla]
    print ("Aqui las entradas")
    for documento in datatabla.find():
        n=str(documento["nortemp"])
        m=str(documento["norhum"])
        val=[int(n),int(m)]
        X = np.array(val)
        print(X)
    #traer salidas
    print ("\nAqui las salidas")
    for documento in datatabla.find():
        s1=str(documento["salidav"])
        s2=str(documento["salidar"])
        s3=str(documento["salidae"])
        val2=[int(s1),int(s2),int(s3)]
        y = np.array(val2)
        print(y)    
     
    """"datatabla.insert_one({
        "temperatura": temp,
        "humedad": hum,
        "nortemp": nt,
        "norhum": nh,
        "salidav": sv,
        "salidar": sr,
        "salidae": se
    }) """
    #cliente.server_info()
    #print("conexión a mongo exitosa")
    #cliente.close()
       
except pymongo.errors.ServerSelectionTimeoutError as error_tiempo:
    print("tiempo exedido"+error_tiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse"+errorConexion)