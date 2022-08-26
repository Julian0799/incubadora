#Importamos librerias
import sys
from ui_PantallaE import * #interfaz
from comunicacion_serial import Comunicacion
from PySide2.QtCore import QTimer
import serial, serial.tools.list_ports
import re
# Importar librerias
import numpy as np                  # Biblioteca para crear vectores y matrices grandes multidimensionales
import matplotlib.pyplot as plt     # BIblioteca para crear graficos
import pymongo
#datos de conexion 
host="localhost"
puerto="27017"
tiempo="1000"
url="mongodb://"+host+":"+puerto+"/"
#acceder base de datos
bd="incubadora"
tabla="lecturas"
vector=[]
vector2=[]


#Arduino 
#


#Clase donde se maneja los witgets
class Entrenar(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Escondemos los botones 
        self.ui.btnentrenar.setVisible(False)
        self.ui.btnactualizar.setVisible(False)
        self.ui.btnenviar.clicked.connect (self.enviar)
        self.ui.btnentrenar.clicked.connect (self.entrenar)
        self.ui.btnactualizar.clicked.connect (self.actualizar)
        
    #Funciones
    def enviar(self):
        
        iteracion=(self.ui.lblniter.text())
        neuronas=(self.ui.lblnneuro.text())
        def numero(cadena):
            try:
                int (cadena)
                return True
            except ValueError:
                return False
        if numero(iteracion)and numero(neuronas):
            global val
            global val2
            val=int(iteracion)
            val2=int(neuronas) 
            self.ui.btnenviar.setVisible(False)
            self.ui.btnactualizar.setVisible(True)
            self.ui.lblniter.setEnabled(False)
            self.ui.lblnneuro.setEnabled(False)
            self.ui.btnentrenar.setVisible(True)
            self.ui.lblniter.setText('')
            self.ui.lblnneuro.setText('')  
            self.ui.lblmensaje.setText("")
            
        else:
            self.ui.lblmensaje.setText("INCORRECTO")
            self.ui.lblniter.setText('')
            self.ui.lblnneuro.setText('') 
            
        
    def actualizar(self):
        self.ui.lblniter.setText('')
        self.ui.lblnneuro.setText('')  
        self.ui.btnenviar.setVisible(True)
        self.ui.btnactualizar.setVisible(False)
        self.ui.lblniter.setEnabled(True)
        self.ui.lblnneuro.setEnabled(True)
    
    def entrenar (self):
        global val
        global val2         
        # Creamos la clase del modelo de la red neuronal
        class NeuralNetwork:
            
            # Rutina: Inicio
            def __init__(self, layers, activation='tanh'):
                
                
                # Si la funcion de activacion es sigmoid
                if activation == 'sigmoid':
                    self.activation = sigmoid
                    self.activation_prime = sigmoid_derivada
                # Si la funcion de activacion es tanh
                elif activation == 'tanh':
                    self.activation = tanh
                    self.activation_prime = tanh_derivada

                # Inicializar los pesos
                self.weights = []
                self.deltas = []
                # Capas = [2,3,3]
                # asigno valores aleatorios (-1,1) a capa de entrada y capa oculta
                for i in range(1, len(layers) - 1):
                    r = 2*np.random.random((layers[i-1] + 1, layers[i] + 1)) -1
                    self.weights.append(r)
                # Asigno aleatorios (-1,1) a capa de salida
                r = 2*np.random.random( (layers[i] + 1, layers[i+1])) - 1
                self.weights.append(r)

            # Rutina: Entrenar modelo
            def fit(self, X, y, learning_rate=0.2, epochs=100000):
                # Agrego columna de unos a las entradas X
                # Con esto agregamos la unidad de Bias a la capa de entrada
                ones = np.atleast_2d(np.ones(X.shape[0]))
                X = np.concatenate((ones.T, X), axis=1)
                
                for k in range(epochs):
                    i = np.random.randint(X.shape[0])
                    a = [X[i]]

                    for l in range(len(self.weights)):
                            dot_value = np.dot(a[l], self.weights[l])
                            activation = self.activation(dot_value)
                            a.append(activation)
                    # Calculo la diferencia en la capa de salida y el valor obtenido
                    error = y[i] - a[-1]
                    deltas = [error * self.activation_prime(a[-1])]
                    
                    # Empezamos en el segundo layer hasta el ultimo
                    # (Una capa anterior a la de salida)
                    for l in range(len(a) - 2, 0, -1): 
                        deltas.append(deltas[-1].dot(self.weights[l].T)*self.activation_prime(a[l]))
                    self.deltas.append(deltas)

                    # Invertir: [level3(output)->level2(hidden)]  => [level2(hidden)->level3(output)]
                    deltas.reverse()

                    # Backpropagation
                    # 1. Multiplcar los delta de salida con las activaciones de entrada para obtener el gradiente del peso.
                    # 2. Actualizo el peso restandole un porcentaje del gradiente
                    for i in range(len(self.weights)):
                        layer = np.atleast_2d(a[i])
                        delta = np.atleast_2d(deltas[i])
                        self.weights[i] += learning_rate * layer.T.dot(delta)

                    if k % 10000 == 0: print('epochs:', k)

            # Rutina: Prediccion
            def predict(self, x): 
                ones = np.atleast_2d(np.ones(x.shape[0]))
                a = np.concatenate((np.ones(1).T, np.array(x)), axis=0)
                for l in range(0, len(self.weights)):
                    a = self.activation(np.dot(a, self.weights[l]))
                return a

            # Rutina: Imrpimir pesos
            def print_weights(self):
                print("Listado pesos de conexiones:")
                for i in range(len(self.weights)):
                    print(self.weights[i])

            # Rutina: Obtener pesos
            def get_weights(self):
                return self.weights
            
            # Rutina: Obtener deltas
            def get_deltas(self):
                return self.deltas

        # Funciones de activacion: Al crear la red, podremos elegir entre usar la funcion sigmoid o tanh
        def sigmoid(x):
            return 1.0/(1.0 + np.exp(-x))
        def sigmoid_derivada(x):
            return sigmoid(x)*(1.0-sigmoid(x))
        def tanh(x):
            return np.tanh(x)
        def tanh_derivada(x):
            return 1.0 - x**2

        # Red para controlar Temperatura y Humedad con Ventilador, Resistencia y Electrovalvula 
        # Capa de entrada: 2 neuronas
        # Capa de oculta:  3 neuronas
        # Capa de salida:  3 neuronas 
        # Funcion de activacion: tanh
        suma=0
        contador=0
        for x in range(val):
            suma=suma+1
        
        for x in range(val2):
            contador=contador+1
        
        nn = NeuralNetwork([2,contador,3],activation ='tanh')

        #conexion al servidor
        try:
            cliente=pymongo.MongoClient(url,serverSelectionTimeoutMS=tiempo)
            baseDatos=cliente[bd]
            datatabla=baseDatos[tabla]
            #traer entradas
            for documento in datatabla.find():
                n=str(documento["nortemp"])
                m=str(documento["norhum"])
                val=[int(n),int(m)]
                vector.append(val)
            #print(vector)    
            #traer salidas
            
            for documento in datatabla.find():
                s1=str(documento["salidav"])
                s2=str(documento["salidar"])
                s3=str(documento["salidae"])
                val2=[int(s1),int(s2),int(s3)]
                vector2.append(val2)
            #print (vector2)
                    
        except pymongo.errors.ServerSelectionTimeoutError as error_tiempo:
            print("tiempo exedido"+error_tiempo)
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse"+errorConexion)
        # Las entradas corresponden a: [Temperatura, Humedad]
        X = np.array(vector)

        # Las salidas corresponden a: [Ventilador, Resistencia, Electrovalvula]
        y = np.array(vector2)

        # Entrenar modelo con las entradas y salidas
        nn.fit(X, y, learning_rate=0.03,epochs=suma)

        # Prediccion de prueba 
        index=0
        for e in X:
            prediccion = nn.predict(e)
            print("X:",e,"esperado:",y[index],"obtenido:",  (int)(round(prediccion[0])), (int)(round(prediccion[1])), (int)(round(prediccion[2])))
            #print("X:",e,"y:",y[index],"Network:",prediccion)
            index=index+1

        # Rutina para convertir valor a String
        def to_str(name, W):
            s = str(W.tolist()).replace('[', '{').replace(']', '}')
            return 'float '+name+'['+str(W.shape[0])+']['+str(W.shape[1])+'] = ' + s + ';'

        # Obtenermos los pesos entrenados para poder usarlos en el codigo de arduino
        pesos = nn.get_weights()
        print('\n')
        print('Pesos de capa oculta y capa de salida:')
        print(to_str('pesos_capa_oculta', pesos[0]))
        print(to_str('pesos_capa_salida', pesos[1]))
        archivo=open("ENCOSOFTV2.0/ENCOSOFTV2.0.ino","w")
        archivo.write("//Nuevo entrenamiento\n")
        archivo.write((to_str('pesos_capa_oculta', pesos[0]))+"\n")
        archivo.write((to_str('pesos_capa_salida', pesos[1]))+"\n")
        archivo.write(
'''/////////////////////// <-- Parametros de la red neuronal --> //////////////////
#define neuronas_capa_entrada 3         // Neurona para Temp, Neurona para Hum y Neurona para el BIAS
#define neuronas_capa_oculta  36         // 3 neuronas ocultas y la neurona del BIAS
#define neuronas_capa_salida  3         // 3 neuronas de salida
/////////////////////// <--Incluir librerias --> ////////////////////////////////
#include <LiquidCrystal.h>              // Para Pantalla  
#include <Wire.h>
#include <DHT.h>                        // Para el sensor DHT
#include <DHT_U.h>                      // Para el sensor DHT
#include <SoftwareSerial.h>             // Para el Bluethoo Y wifi
#include <Adafruit_MLX90614.h>          // Sensor Termometro Digital
#include <Servo.h>                      // Servomotor

//Crear el objeto LCD con los números correspondientes (rs, en, d4, d5, d6, d7)
LiquidCrystal lcd(7, 8, 3, 4, 5, 6);
/////////////////////// <-- Instanciar objeto --> ///////////////////////////////
Adafruit_MLX90614 termometroIR = Adafruit_MLX90614();
/////////////////////// <-- Definir pines de entrada --> ////////////////////////
//#define RXW                   10         // D2: Wifi VERDE
//#define TXW                   11         // D3: Wifi AMARILLO
#define RXB                   45         // D2: Bluethoo AMARILLO
#define TXB                   47         // D3: Bluethoo TOMATE
#define pin_sensor_dht        52         // D8: Sensor de Humedad
#define pin_sensor_dht1       53         // D8: Sensor de Humedad
/////////////////////// <-- Definir pines de salida --> ////////////////////////
#define pin_ventilador        24         // D3: Rele del ventilador
#define pin_resistencia       22         // D4: Rele de la resistencia
#define pin_electrovalvula    26         // D5: Rele de la electrovalvula
#define pin_motor             28         // D5: Rele de motor

/////////////////////// <-- Control del servomotor --> /////////////////////////
Servo servoMotor;
/////////////////////// <-- Definicion de constantes --> ///////////////////////
#define temp_min              34      // Valor minimo de Temperatua
#define temp_max              36      // Valor maximo de Temperatura
#define hum_min               55        // Valor minimo de Humedad 
#define hum_max               85        // Valor maximo de Humedad
#define tiempo_intervalo      1500       // Cada 100ms predecir con la red neuronal

double capa_oculta[neuronas_capa_oculta];
double capa_salida[neuronas_capa_salida];
double RNentradas[] = {0, 0, 0};
double RNsalidas[]  = {0, 0, 0, 0};

/////////////////////// <-- Declaracion de objetos --> /////////////////////////
DHT dht(pin_sensor_dht, DHT11);         // Objeto para el DHT
DHT dht2(pin_sensor_dht1, DHT11);   

SoftwareSerial esp8266(10,11);        // objeto Wifi 
SoftwareSerial Torito(RXB,TXB);         // objeto Bluethooo
/////////////////////// <-- Declaracion de variables globales --> /////////////
float temp, hum,hum1, hum2;
int estado_temp, estado_hum;
int estado_ventilador = 0, estado_resistencia = 0, estado_electrovalvula = 0;
unsigned long millis_intervalo;
unsigned long tiempo_anterior;
/////////////////////// <-- Declaracion de variables de RED --> ///////////////
String AP = "Tesis";             // Nombre de red
String PASS = "0401739404";             // Contraseña
String API = "WVKB1NNN01S513O4";        // Write API KEY
String HOST = "api.thingspeak.com";     //Broker
String PORT = "80";
String field = "field1";
String field2 = "field2";
int countTrueCommand;
int countTimeCommand; 
boolean found = false; 

///////////////////////////////////////////////////////////////////////////////
void setup() {
  // put your setup code here, to run once:
  // Iniciar puerto serial
  Serial.begin(9600);
  
  // Iniciar puerto serial de WIFI
  esp8266.begin(115200);
  // Iniciar puerto serial Bluethoo
  Torito.begin(38400);
  /*sendCommand("AT",5,"OK");
  sendCommand("AT+CWMODE=1",5,"OK");
  sendCommand("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"",20,"OK");*/
  //indicamos que es una pantalla lcd 16x2
  // Inicializar el LCD con el número de  columnas y filas del LCD
  lcd.begin(16, 2);
  lcd.setCursor (0, 0);
  // Escribimos el Mensaje en el LCD.
  lcd.print("Hola Mundo");
     // Configuracion de pines
  pinMode(pin_ventilador,     OUTPUT);
  pinMode(pin_resistencia,    OUTPUT);
  pinMode(pin_electrovalvula, OUTPUT);
  pinMode(pin_motor, OUTPUT);
  // Iniciar sensor DHT
  dht.begin();
  dht2.begin();
  //delay(500);
   // Prueba inicial del sensor DHT
  int aux_hum = dht.readHumidity();
  int aux_hum2 = dht2.readHumidity();
  //int aux_tem = dht.readTemperature();
  // Iniciar termómetro infrarrojo con Arduino
  termometroIR.begin();
  tiempo_anterior=millis();
  // Iniciar Servo
  servoMotor.attach(9);
  

}

void loop() {
  
  
  // Cada intervalor de tiempo predecir con la red neuronal
  if (millis() > millis_intervalo) {
    millis_intervalo = millis() + tiempo_intervalo;
    // Obtener mediciones
    Obtener_Mediciones();
    // Normalizar mediciones [-1,1]
    estado_temp = Normalizar(temp, temp_min, temp_max);
    estado_hum  = Normalizar(hum, hum_min, hum_max);
    /*if((millis()-tiempo_anterior)>= 4000){ //3600000
      tiempo_anterior=millis();
      Servot();
    }*/
    Serial.println();
    Serial.println("Mediciones>> Temp:" + String(temp) + "C Hum:" + String(hum) + "%");
    Serial.println("Normalizadas>> Temp:" + String(estado_temp) + " Hum:" + String(estado_hum));
    
     // Predecir
    Predecir();
    Torito.println("Temp:" + String(temp)+ "°C" + "|" +"Hum:" + String(hum) + "% "+"Normalizadas>> Temp:" + String(estado_temp) + " Hum:" + String(estado_hum)+"Salida1:" + String(RNsalidas[0]) + " Salida2:" + String(RNsalidas[1]) + " Salida3:" + String(RNsalidas[2])); 
        // Actuar sobre las salidas
    digitalWrite(pin_ventilador,      estado_ventilador);
    digitalWrite(pin_resistencia,     estado_resistencia);
    digitalWrite(pin_electrovalvula,  estado_electrovalvula); 
         
    /*Serial.print(estado_ventilador);
    Serial.print(estado_resistencia);    
    Serial.print(estado_electrovalvula);*/
    lcd.clear () ;
    lcd.setCursor (0, 0);
    lcd.print ("Temp: ");
    lcd.setCursor (6, 0);
    lcd.print (String(temp) + "C");
    lcd.setCursor (0, 1);
    lcd.print ("Hum: ");
    lcd.setCursor (6, 1);
    lcd.print (String(hum) + "%");
    /*if((millis()-tiempo_anterior)>= 1500){ //3600000
      tiempo_anterior=millis();
      String getData = "GET /update?api_key="+ API +"&"+ field +"="+String(temp)+"&"+ field2 +"="+String(hum);;
      sendCommand("AT+CIPMUX=1",5,"OK");
      sendCommand("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT,15,"OK");
      sendCommand("AT+CIPSEND=0," +String(getData.length()+4),4,">");
      esp8266.println(getData);
      delay(1500);
      countTrueCommand++;
      sendCommand("AT+CIPCLOSE=0",5,"OK");
    }
    */
    
   
    
  }
  
  
   
}

// Funcion: Obtener mediciones
void Obtener_Mediciones() {
  // Obtener Temperatura en °C
  float temperaturaAmbiente = termometroIR.readAmbientTempC();
  float temperaturaObjeto = termometroIR.readObjectTempC();
  temp=temperaturaAmbiente;
  // Obtener Humedad en %
  hum1 = dht.readHumidity();
  hum2 = dht2.readHumidity();
  hum=(hum1+hum2)/2;
  if ((hum >= 0) && (temp <= 100)) {} else hum = 0;
}

// Funcion: Normalizar variables
int Normalizar(float variable, float val_min, float val_max) {
  int estado;
  if (variable < val_min) estado = -1;
  else if (variable > val_max) estado = 1;
  else estado = 0;
  return estado;
}

// Funcion: Predecir el modelo de red neuronal con los pesos generados en Python
void Predecir() {
  // Llamamos a la red FEEDFORWARD con las entradas
  RNentradas[0] = 1.0;            // Unidad para el BIAS
  RNentradas[1] = estado_temp;    // Temperatura
  RNentradas[2] = estado_hum;     // Humedad
  Procesar_Capas();               // Procesar modelo

  // Procesar las salidas de la red neuronal
  RNsalidas[0] = round(capa_salida[0]);
  RNsalidas[1] = round(capa_salida[1]);
  RNsalidas[2] = round(capa_salida[2]);
  Serial.println("Salida1:" + String(RNsalidas[0]) + " Salida2:" + String(RNsalidas[1]) + " Salida3:" + String(RNsalidas[2]));

  // Definir estados de los actuadores
  if (RNsalidas[0] != -1) {
    estado_ventilador     = RNsalidas[0];
  }
  if (RNsalidas[1] != -1) {
    estado_resistencia    = RNsalidas[1];
  }
  if (RNsalidas[2] != -1) {
    estado_electrovalvula = RNsalidas[2];
  }
}

// Funcion: Procesar capas de la red neuronal
void Procesar_Capas() {
  double acumulacion;

  // Calcular las activaciones en las capas ocultas
  for (int i = 0 ; i < neuronas_capa_oculta ; i++ ) {
    acumulacion = 0;//HiddenWeights[InputNodes][i] ;
    for (int j = 0 ; j < neuronas_capa_entrada ; j++ ) {
      acumulacion += RNentradas[j] * pesos_capa_oculta[j][i] ;
    }
    //capa_oculta[i] = 1.0 / (1.0 + exp(-acumulacion)); // Funcion de activacion: Sigmoid
    capa_oculta[i] = tanh(acumulacion);   // Funcion de activacion: tanh
  }

  //  Calcular activacion y error en la capa de Salida
  for (int i = 0 ; i < neuronas_capa_salida ; i++ ) {
    acumulacion = 0;//OutputWeights[HiddenNodes][i];
    for (int j = 0 ; j < neuronas_capa_oculta ; j++ ) {
      acumulacion += capa_oculta[j] * pesos_capa_salida[j][i] ;
    }
    capa_salida[i] = tanh(acumulacion) ;  // Funcion de activacion: tanh
  }
}
//Enviar comandos a consola
void sendCommand(String command, int maxTime, char readReplay[]) {
  Serial.print(countTrueCommand);
  Serial.print(". at command => ");
  Serial.print(command);
  Serial.print(" ");
  while(countTimeCommand < (maxTime*1))
  {
    esp8266.println(command);//at+cipsend
    if(esp8266.find(readReplay))//ok
    {
      found = true;
      break;
    }
  
    countTimeCommand++;
  }
  
  if(found == true)
  {
    Serial.println("Conectado");
    countTrueCommand++;
    countTimeCommand = 0;
  }
  
  if(found == false)
  {
    Serial.println("Fallido");
    countTrueCommand = 0;
    countTimeCommand = 0;
  }
  
  found = false;
 }
 //volteo automatico
void Servot() {
  
    for (int pos = 50; pos >15 ; pos -=7 ) { 
    // in steps of 1 degree
    servoMotor.write(pos);
    delay(1000); 
    }
    for (int pos = 15; pos < 140; pos +=7 ) { 
    // in steps of 1 degree
    servoMotor.write(pos);
    delay(1000); // tell servo to go to position in variable 'pos'
                           
    }
    for (int pos = 140; pos >50; pos -=7 ) { 
    // in steps of 1 degree
    servoMotor.write(pos);  
    delay(1000); // tell servo to go to position in variable 'pos'
    
    }
  
}''')
        archivo.close()

        # Graficas datos de entrenamiento
        deltas = nn.get_deltas()
        valores=[]
        index=0
        for arreglo in deltas:
            valores.append(arreglo[1][0] + arreglo[1][1])
            index=index+1

        plt.plot(range(len(valores)), valores, color='b')
        plt.ylim([0, 0.4])
        plt.ylabel('Coste')
        plt.xlabel('Epocas')
        plt.tight_layout()
        plt.show()
        
        self.ui.btnentrenar.setVisible(False)
        self.ui.btnenviar.setVisible(True)
        self.ui.lblniter.setEnabled(True)
        self.ui.lblnneuro.setEnabled(True)
        
    

#Codigo para ejecutar la aplicación
if __name__ == "__main__":
  app=QApplication(sys.argv)   
  mi_app=Entrenar()
  mi_app.show()
  sys.exit(app.exec_())   


