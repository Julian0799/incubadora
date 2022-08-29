//Nuevo entrenamiento
float pesos_capa_oculta[3][36] = {{-1.0154563524971085, 1.1135562727366675, 0.6866045959756638, -1.195901333578544, 0.9997264160940112, 0.7671172568328608, 0.024853383076800867, -0.28835741978483176, -0.8922159659201706, -0.5285314191803984, 0.4711400673641437, -0.30150197671945483, 0.8309537101642024, 0.6314668417565416, 0.829971474940466, -0.7475384120960535, -0.1410572385370736, 0.35093395255713744, 0.8459034543079952, 0.21277836730556923, -0.5138121692359682, 0.5040245681187994, 0.2656495460047559, 0.5026136377585702, -0.0383393068290541, -0.9734152707040314, 0.576542521573534, -1.2139099606717083, -0.7780253843924234, 0.725456928703455, -0.7206000887864394, -1.35073646052926, 0.6189103604560102, 0.6019775685805926, -0.614005248974706, 0.8416903260395273}, {2.0107347635508948, 2.153827451253522, -0.10458953172814307, -0.20754668409750238, 1.8764436746118585, 0.7300134040008514, 0.040458186352619906, -0.076999996479599, -0.903071794319606, 0.0770548773454087, 0.5938072121862293, -0.19875376192560568, -0.22184092874735634, 0.7930326663244666, -1.3758468842207563, -1.264661517731953, -0.39237429577350763, 0.6992868436114505, -1.3026530139362928, 0.3589761771064634, 0.22050187607877342, 0.37115840108467363, -0.8015367744922166, -0.7233311912708091, 0.7216742692241103, -0.9383524323176654, -0.7362136452471727, 0.03221896983931052, 1.5691856167618101, -0.13058659545852108, 0.06113983234149112, 0.08794852322807281, 1.1498570682492182, -0.44871295895279334, -0.15843839772477367, 0.052127891433540165}, {0.01940313498436247, 0.22346946840949256, 0.5955802979267083, 0.6263043673023626, -0.19877821248775102, 0.1911337169651031, 0.2718966578197119, -1.0245648353871188, 0.7484044863683872, -0.8823770317304396, -0.821499414979286, 0.5739502836042273, 1.1225667956417837, -0.22476885000197028, -0.5893846699797601, 0.26644719729960703, 0.6888736934249061, -0.968642901324508, -0.07825783491276418, 1.155043488331826, -0.8239826995337257, 0.37100397446521416, 0.7527218139267379, -0.2740662573434268, 0.6893925888449615, 0.30220554961633145, 0.5746898299051902, -0.2739264106272582, 0.472990193880096, 0.3174880100801955, -0.369634837552142, 0.4634621406121702, 0.49741926005892384, 0.4686419442136146, -0.35274518315777054, 0.10887879296999065}};
float pesos_capa_salida[36][3] = {{1.5506464548531667, 0.9532872564940069, 0.20450391524197148}, {-1.3603921717630219, -1.2900496232635605, -0.15579692788936308}, {0.30859476302244865, -0.014777627574864487, -0.29665216749080303}, {-0.5044579860533502, -0.9865778916556237, 0.4702847562432901}, {-0.9129467947527411, -1.482495328006279, -0.25479331218045387}, {0.29476030887774224, -0.2572271449944936, 0.6411515457089986}, {0.08708202270625513, -0.6472334060994234, 0.638952814283772}, {-0.6361852791858913, 0.7319052674802776, 0.5890971909553572}, {0.5792442987265085, 0.1381132319007789, 0.27552897672132265}, {-0.4331437977946645, 0.5302700532399788, 0.9937089893679655}, {-0.32097655227544786, -0.24921573582960543, 1.0395346512504742}, {-0.8596350496494352, 0.8257936950232246, -0.49917298633114104}, {-0.3326299142498413, 0.4841242897600489, -0.8301067736563469}, {0.5021684509692744, -0.9938379945100019, -0.021782899588825358}, {-0.4781687444035301, -0.6854799561063678, -0.19875818705619036}, {0.1654065986433425, 1.0424092723853045, 0.15943753110420772}, {0.7177078538041542, 0.08390486056594876, -0.9045315181045889}, {0.4429551504660344, -0.23597218529709718, 0.5084769016084102}, {-0.15480672651745503, -0.9106821932230863, -0.5937664250524378}, {-0.5152279620988306, -0.8902341012416745, -1.0222474628683933}, {0.839304901855666, -0.909558412193103, 0.5308777456623329}, {0.18523844679771395, 0.08735999678145621, -0.6413644071589463}, {-0.8153555839606542, -0.8327667861490687, -0.24466403409786427}, {-0.06643293463847509, -0.27558216556847065, 0.8870729004177902}, {0.11344396127975363, 0.17828634633752932, -0.9480765305548363}, {0.8413708652655585, -0.5132139576260725, 0.10091988384628413}, {-0.44603628705659343, -0.4771836745654063, 0.40004522213891763}, {-0.9906273507281175, -0.7700872075049999, 0.32865099379609897}, {1.6122945857414073, 0.24351348927587513, -0.25892467163449995}, {0.1251800766441532, 0.12591025925390775, -0.5079818780843689}, {0.20771918552247665, -1.015031758502002, -0.440958045005456}, {-0.839820276440319, -0.45498859779707607, 0.5405019372891345}, {-0.31393219809998874, -0.40108450425860553, 0.32511915851132245}, {0.5109523484398983, -0.3020159099284111, -0.08820313841427303}, {-0.04929367324970908, -0.9049726398892849, 0.9656645191234501}, {1.0324916368063761, 1.0548241537459546, -0.265123978618414}};
/////////////////////// <-- Parametros de la red neuronal --> //////////////////
#define neuronas_capa_entrada 3         // Neurona para Temp, Neurona para Hum y Neurona para el BIAS
#define neuronas_capa_oculta   36        // 3 neuronas ocultas y la neurona del BIAS
#define neuronas_capa_salida  3         // 3 neuronas de salida
/////////////////////// <--Incluir librerias --> ////////////////////////////////
#include <LiquidCrystal.h>              // Para Pantalla  
#include <Wire.h>
#include <DHT.h>                        // Para el sensor DHT
#include <DHT_U.h>                      // Para el sensor DHT
#include <SoftwareSerial.h>             // Para el Bluethoo Y wifi
#include <Adafruit_MLX90614.h>          // Sensor Termometro Digital
#include <Servo.h>                      // Servomotor

//Crear el objeto LCD con los n�meros correspondientes (rs, en, d4, d5, d6, d7)
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
#define temp_min              36.5      // Valor minimo de Temperatua
#define temp_max              37.8      // Valor maximo de Temperatura
#define hum_min               55        // Valor minimo de Humedad 
#define hum_max               85        // Valor maximo de Humedad
#define tiempo_intervalo      3000       // Cada 100ms predecir con la red neuronal

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
String PASS = "0401739404";             // Contrase�a
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
  sendCommand("AT+CWJAP=""+ AP +"",""+ PASS +""",20,"OK");*/
  //indicamos que es una pantalla lcd 16x2
  // Inicializar el LCD con el n�mero de  columnas y filas del LCD
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
  // Iniciar term�metro infrarrojo con Arduino
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
      // Actuar sobre las salidas
    digitalWrite(pin_ventilador,      estado_ventilador);
    digitalWrite(pin_resistencia,     estado_resistencia);
    digitalWrite(pin_electrovalvula, estado_electrovalvula );
    /*if(RNsalidas[2]==-1){
      estado_electrovalvula=1;      
      digitalWrite(pin_electrovalvula, estado_electrovalvula );   
    } else if(RNsalidas[2]==1){
      estado_electrovalvula=0; 
      digitalWrite(pin_electrovalvula, estado_electrovalvula );
    }
     else{
      estado_electrovalvula=0; 
      digitalWrite(pin_electrovalvula, estado_electrovalvula );  
    }*/
     
    Torito.println("Temp:" + String(temp)+ "C" + "|" +"Hum:" + String(hum) + "% "+"Normalizadas>> Temp:" + String(estado_temp) + " Hum:" + String(estado_hum)+"Salida1:" + String(RNsalidas[0]) + " Salida2:" + String(RNsalidas[1]) + " Salida3:" + String(RNsalidas[2])); 
          
    Serial.print(estado_ventilador);
    Serial.print(estado_resistencia);  
    Serial.print(estado_electrovalvula);
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
      sendCommand("AT+CIPSTART=0,"TCP",""+ HOST +"","+ PORT,15,"OK");
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
  // Obtener Temperatura en �C
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
  
}