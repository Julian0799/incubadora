// Incluir librerias
#include <DHT.h>                        // Para el sensor DHT
#include <DHT_U.h>                      // Para el sensor DHT
#include <SoftwareSerial.h>             // Para el Bluethoo

// Definir pines de entrada
#define pin_sensor_lm35       A0        // A0: Sensor de Temperatura
#define pin_sensor_dht        8         // D2: Sensor de Humedad
  // Incluímos la librería para poder controlar el servo
#include <Servo.h>
 
// Declaramos la variable para controlar el servo
Servo servoMotor;
// Definir pines de salida
#define pin_ventilador        3         // D3: Rele del ventilador
#define pin_resistencia       4         // D4: Rele de la resistencia
#define pin_electrovalvula    5         // D5: Rele de la electrovalvula
#define pin_motor             6         // D5: Rele de motor

// Definicion de constantes
#define temp_min              36.5      // Valor minimo de Temperatua
#define temp_max              37.8      // Valor maximo de Temperatura
#define hum_min               55        // Valor minimo de Humedad
#define hum_max               85      // Valor maximo de Humedad
#define tiempo_intervalo      100       // Cada 100ms predecir con la red neuronal

// Parametros de la red neuronal
#define neuronas_capa_entrada 3         // Neurona para Temp, Neurona para Hum y Neurona para el BIAS
#define neuronas_capa_oculta  4         // 3 neuronas ocultas y la neurona del BIAS
#define neuronas_capa_salida  3         // 3 neuronas de salida
double capa_oculta[neuronas_capa_oculta];
double capa_salida[neuronas_capa_salida];
double RNentradas[] = {0, 0, 0};
double RNsalidas[]  = {0, 0, 0, 0};
// Pesos
float pesos_capa_oculta[3][4] = {{-1.869347536358914, -2.7854217933156344, 0.6652998833400943, -1.869726603151382}, {3.45366547819369, -0.0010092662214519455, 0.004162847419093488, -3.4487180218141087}, {-1.0467434771615622, -4.334684607263233, 0.5361508699905841, -1.0450607102243399}};
float pesos_capa_salida[4][3] = {{2.8753860908914586, 1.8174802929440972, -0.0076088340488911985}, {0.7156698407844756, 0.7187749734986515, 4.753507391743887}, {3.264578065935506, 3.264572585747721, 5.668682097503817}, {1.832208212996835, 2.8801172327621716, -0.009162338644393017}};

// Declaracion de objetos
DHT dht(pin_sensor_dht, DHT11);       // Objeto para el DHT
SoftwareSerial Torito(10,11);         // objeto Bluethooo
//10 TXD                              //pin conexión
//11 RDX                             // pin conexión
// Declaracion de variables globales
float temp, hum;
int estado_temp, estado_hum;
int estado_ventilador = 0, estado_resistencia = 0, estado_electrovalvula = 0, estado_motor = 0;
unsigned long millis_intervalo;

void setup() {
  // Iniciar puerto serial
  Serial.begin(9600);
  Torito.begin(38400);
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
    Serial.println();
    Serial.println("Mediciones>> Temp:" + String(temp) + "C "+"Hum:" + String(hum) + "%");
    Torito.println("Temp:" + String(temp)+ "°C" + "|" +"Hum:" + String(hum) + "%");
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
    //servo();
    
  }
}

// Funcion: Obtener mediciones
void Obtener_Mediciones() {
  // Obtener Temperatura en °C
  float total_analog = 0;
  for (int i = 0; i < 5; i++) { // Leer pin analogico 5 veces y tomar el promedio
    total_analog += analogRead(pin_sensor_lm35);
    delay(500);
  }
  float temp2 = (5.0 * (total_analog / 5.0) * 100.0) / 1024.0;

  // Obtener Humedad en %
  hum = dht.readHumidity();
  if ((hum >= 0) && (temp <= 100)) {} else hum = 0;
    float t= dht.readTemperature();
    temp=t;
  Serial.print("Temperatura: ");
  Serial.print(temp2);
  Serial.print(" *C ");
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
  delay(10000);
     for (int pos = 70; pos >50 ; pos -=7 ) { 
    // in steps of 1 degree
    servoMotor.write(pos);              // tell servo to go to position in variable 'pos'
    delay(1000);                       // waits 15ms for every swept degree
  }

  for (int pos = 50; pos < 85; pos +=7 ) { 
    // in steps of 1 degree
    servoMotor.write(pos);              // tell servo to go to position in variable 'pos'
    delay(1000);                       // waits 15ms for every swept degree
  }
  for (int pos = 85; pos >70; pos -=7) { 
    // in steps of 1 degree
    servoMotor.write(pos);              // tell servo to go to position in variable 'pos'
    delay(1000);                       // waits 15ms for every swept degree
  }
  
}
