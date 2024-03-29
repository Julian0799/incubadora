/////////////////////// <--Incluir librerias --> ////////////////////////////////
#include <DHT.h>                        // Para el sensor DHT
#include <DHT_U.h>                      // Para el sensor DHT
#include <SoftwareSerial.h>             // Para el Bluethoo Y wifi
#include <Adafruit_MLX90614.h>          // Sensor Termometro Digital
#include <Servo.h>                      // Servomotor
#include <LiquidCrystal.h>              // Para Pantalla  
/////////////////////// <-- Instanciar objeto --> ///////////////////////////////
Adafruit_MLX90614 termometroIR = Adafruit_MLX90614();
/////////////////////// <-- Definir pines de entrada --> ////////////////////////
#define RXW                   2         // D2: Wifi
#define TXW                   3         // D3: Wifi
#define RXB                   2         // D2: Bluethoo 
#define TXB                   3         // D3: Bluethoo 
#define pin_sensor_dht        8         // D8: Sensor de Humedad
/////////////////////// <-- Definir pines de salida --> ////////////////////////
#define pin_ventilador        3         // D3: Rele del ventilador
#define pin_resistencia       4         // D4: Rele de la resistencia
#define pin_electrovalvula    5         // D5: Rele de la electrovalvula
#define pin_motor             6         // D5: Rele de motor
LiquidCrystal lcd(12, 13, 8, 9, 10, 11);
/////////////////////// <-- Control del servomotor --> /////////////////////////
Servo servoMotor;
/////////////////////// <-- Definicion de constantes --> ///////////////////////
#define temp_min              36.5      // Valor minimo de Temperatua
#define temp_max              37.8      // Valor maximo de Temperatura
#define hum_min               55        // Valor minimo de Humedad
#define hum_max               85        // Valor maximo de Humedad
#define tiempo_intervalo      1000       // Cada 100ms predecir con la red neuronal
/////////////////////// <-- Parametros de la red neuronal --> //////////////////
#define neuronas_capa_entrada 3         // Neurona para Temp, Neurona para Hum y Neurona para el BIAS
#define neuronas_capa_oculta  4         // 3 neuronas ocultas y la neurona del BIAS
#define neuronas_capa_salida  3         // 3 neuronas de salida
double capa_oculta[neuronas_capa_oculta];
double capa_salida[neuronas_capa_salida];
double RNentradas[] = {0, 0, 0};
double RNsalidas[]  = {0, 0, 0, 0};
/////////////////////// <-- Pesos de la red neuronal --> ///////////////////////
float pesos_capa_oculta[3][4] = {{-1.869347536358914, -2.7854217933156344, 0.6652998833400943, -1.869726603151382}, {3.45366547819369, -0.0010092662214519455, 0.004162847419093488, -3.4487180218141087}, {-1.0467434771615622, -4.334684607263233, 0.5361508699905841, -1.0450607102243399}};
float pesos_capa_salida[4][3] = {{2.8753860908914586, 1.8174802929440972, -0.0076088340488911985}, {0.7156698407844756, 0.7187749734986515, 4.753507391743887}, {3.264578065935506, 3.264572585747721, 5.668682097503817}, {1.832208212996835, 2.8801172327621716, -0.009162338644393017}};
/////////////////////// <-- Declaracion de objetos --> /////////////////////////
DHT dht(pin_sensor_dht, DHT11);         // Objeto para el DHT
SoftwareSerial Torito(RXB,TXB);         // objeto Bluethooo
SoftwareSerial esp8266(RXW,TXW);        // objeto Wifi 
/////////////////////// <-- Declaracion de variables globales --> /////////////
float temp, hum;
int estado_temp, estado_hum;
int estado_ventilador = 0, estado_resistencia = 0, estado_electrovalvula = 0;
unsigned long millis_intervalo;
unsigned long tiempo_anterior;
/////////////////////// <-- Declaracion de variables de RED --> ///////////////
String AP = "Jose vallejo";             // Nombre de red
String PASS = "0402135222";             // Contraseña
String API = "K3FL3G4J2ZP5OWZO";        // Write API KEY
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
  // Iniciar puerto serial Bluethoo
  Torito.begin(38400);
  // Iniciar puerto serial de WIFI
  esp8266.begin(9600);
  sendCommand("AT",5,"OK");
  sendCommand("AT+CWMODE=1",5,"OK");
  sendCommand("AT+CWJAP=\""+ AP +"\",\""+ PASS +"\"",20,"OK");
  //indicamos que es una pantalla lcd 16x2
  lcd.begin (16, 2); 
  // Configuracion de pines
  pinMode(pin_ventilador,     OUTPUT);
  pinMode(pin_resistencia,    OUTPUT);
  pinMode(pin_electrovalvula, OUTPUT);
  pinMode(pin_motor, OUTPUT);
  // Iniciar sensor DHT
  dht.begin();
  delay(500);
   // Prueba inicial del sensor DHT
  int aux_hum = dht.readHumidity();
  int aux_tem = dht.readTemperature();
  // Iniciar termómetro infrarrojo con Arduino
  termometroIR.begin();
  tiempo_anterior=millis();
  // Iniciar Servo
  servoMotor.attach(9);

}

void loop() {
  // put your main code here, to run repeatedly:
   // Cada intervalor de tiempo predecir con la red neuronal
  if (millis() > millis_intervalo) {
    millis_intervalo = millis() + tiempo_intervalo;
    // Obtener mediciones
    Obtener_Mediciones();
    // Normalizar mediciones [-1,1]
    estado_temp = Normalizar(temp, temp_min, temp_max);
    estado_hum  = Normalizar(hum, hum_min, hum_max);
    Serial.println();
    Serial.println("Mediciones>> Temp:" + String(temp) + "ºC "+"Hum:" + String(hum) + "%");
    Torito.println("Temp:" + String(temp)+ "°C" + "|" +"Hum:" + String(hum) + "%");
    lcd.clear () ;
    lcd.setCursor (0, 0);
    lcd.print ("Temp: ");
    lcd.setCursor (6, 0);
    lcd.print (String(temp) + "C");
    lcd.setCursor (0, 1);
    lcd.print ("Hum: ");
    lcd.setCursor (6, 1);
    lcd.print (String(hum) + "%");
    //delay (1000);
    String getData = "GET /update?api_key="+ API +"&"+ field +"="+String(temp)+"&"+ field2 +"="+String(hum);;
    sendCommand("AT+CIPMUX=1",5,"OK");
    sendCommand("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT,15,"OK");
    sendCommand("AT+CIPSEND=0," +String(getData.length()+4),4,">");
    esp8266.println(getData);
    //delay(1500);
    countTrueCommand++;
    sendCommand("AT+CIPCLOSE=0",5,"OK");
    Serial.println("Normalizadas>> Temp:" + String(estado_temp) + " Hum:" + String(estado_hum));
    if (estado_hum=1){
      pinMode(pin_motor, HIGH);
    }else{
      pinMode(pin_motor, OUTPUT);
    }
    // Predecir
    Predecir();
    // Actuar sobre las salidas
    digitalWrite(pin_ventilador,      estado_ventilador);
    digitalWrite(pin_resistencia,     estado_resistencia);
    digitalWrite(pin_electrovalvula,  estado_electrovalvula);
    servo();
    
  }
}
// Funcion: Obtener mediciones
void Obtener_Mediciones() {
  // Obtener Temperatura en °C
  float temperaturaAmbiente = termometroIR.readAmbientTempC();
  float temperaturaObjeto = termometroIR.readObjectTempC();
  temp=temperaturaAmbiente;
  // Obtener Humedad en %
  hum = dht.readHumidity();
  if ((hum >= 0) && (temp <= 100)) {} else hum = 0;
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
    Serial.println("OYI");
    countTrueCommand++;
    countTimeCommand = 0;
  }
  
  if(found == false)
  {
    Serial.println("Fail");
    countTrueCommand = 0;
    countTimeCommand = 0;
  }
  
  found = false;
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
  Serial.println("Salida1:" + String(RNsalidas[1]) + " Salida2:" + String(RNsalidas[0]) + " Salida3:" + String(RNsalidas[2]));

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
//volteo automatico
void servo() {
  if((millis()-tiempo_anterior)>=1000){
    tiempo_anterior=millis();
    for (int pos = 70; pos >50 ; pos -=7 ) { 
    // in steps of 1 degree
    servoMotor.write(pos);
    }
    for (int pos = 50; pos < 85; pos +=7 ) { 
    // in steps of 1 degree
    servoMotor.write(pos);              // tell servo to go to position in variable 'pos'
                           
    }
    for (int pos = 85; pos >70; pos -=7) { 
    // in steps of 1 degree
    servoMotor.write(pos);              // tell servo to go to position in variable 'pos'
    
    }
  }
}
