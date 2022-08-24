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
#define temp_min              35      // Valor minimo de Temperatua
#define temp_max              36      // Valor maximo de Temperatura
#define hum_min               55        // Valor minimo de Humedad 
#define hum_max               85        // Valor maximo de Humedad
#define tiempo_intervalo      1500       // Cada 100ms predecir con la red neuronal
/////////////////////// <-- Parametros de la red neuronal --> //////////////////
#define neuronas_capa_entrada 3         // Neurona para Temp, Neurona para Hum y Neurona para el BIAS
#define neuronas_capa_oculta  36         // 3 neuronas ocultas y la neurona del BIAS
#define neuronas_capa_salida  3         // 3 neuronas de salida
double capa_oculta[neuronas_capa_oculta];
double capa_salida[neuronas_capa_salida];
double RNentradas[] = {0, 0, 0};
double RNsalidas[]  = {0, 0, 0, 0};
/////////////////////// <-- Pesos de la red neuronal --> ///////////////////////
//float pesos_capa_oculta[3][4] = {{-1.869347536358914, -2.7854217933156344, 0.6652998833400943, -1.869726603151382}, {3.45366547819369, -0.0010092662214519455, 0.004162847419093488, -3.4487180218141087}, {-1.0467434771615622, -4.334684607263233, 0.5361508699905841, -1.0450607102243399}};
//float pesos_capa_salida[4][3] = {{2.8753860908914586, 1.8174802929440972, -0.0076088340488911985}, {0.7156698407844756, 0.7187749734986515, 4.753507391743887}, {3.264578065935506, 3.264572585747721, 5.668682097503817}, {1.832208212996835, 2.8801172327621716, -0.009162338644393017}};
//float pesos_capa_oculta[3][36] = {{0.4723909734092833, -0.17280584045763545, -0.06770897424405203, 0.6659199183091601, -0.7391076348669368, -0.6671541368681381, 0.9079930195729397, -0.9701589875028293, -0.8437336707776131, -0.3302108324677054, 0.9811028357770454, 0.7617484485431867, -0.8549932092166508, -0.08076245668591592, 0.7038923727124239, 0.9377618329009896, 0.7342915526302111, 0.9286033973639785, 0.8069397230628772, 0.8791503997758977, 0.3822483854938895, -1.3846772327890708, 0.7923790550437588, 0.989335013568046, -0.1496478213331891, 0.5178294000039383, -0.028378298304834126, -0.7409192093245401, 0.8149004346099601, 0.11075906797831123, 0.6043622781388233, 1.1265203422873935, 0.942993777974445, -0.8859205879743483, 0.7411550604078835, -0.14789057032419844}, {0.17996387001400094, -0.6032769127435473, 0.8083864177239969, 0.2580917308646404, -0.9602006151731154, 1.6288939575885544, -1.8422243437893233, -0.9778796699192385, 1.5311206642915505, -0.015325200784497213, -0.12064788449726249, -0.016139358591283928, -1.465261959804406, 0.5894462413635925, 0.045552144209728404, 0.11653450243303896, -0.23768037491306007, 0.09787623786518773, 0.20831388533765682, -0.15188308097097394, -0.36728855338833266, 0.23760003348651326, -0.1912586056808891, 1.8532122212515865, 0.16809832838629835, 0.034384399418782526, 0.27620074044601917, -1.5758610615041224, 0.2193423046538045, -0.8263115338385606, -0.12088650110243948, -0.14995164883686427, 0.9007612776994545, -1.2476353672547358, 1.6977021337715492, -0.9023912755582343}, {-0.11310864677575584, 0.3629843922663496, -0.8491793685973367, -0.032782944259402653, 0.696186021875278, -0.1892019611535347, -0.08818405250776438, -0.002437846466223579, -0.20790109365128956, -0.6420384508542147, 0.12526537253401682, 0.932022100495721, 0.043342255225146675, 0.21994119917827237, 0.15850857003058635, 1.8287743440568545, -0.8808119966416521, -0.06854894232374335, -1.5950481397329683, 0.026913044654823637, 0.8177828360286501, -0.11883680601379096, 1.5027369008734233, 0.13972915785114215, 0.07171102512953094, 0.7745766416842309, 0.9023503034453669, 0.21917289909817667, -1.3583678131601098, 0.4336057601344134, 1.0702150467649285, -2.115273786939187, -0.4638543762943098, -0.8101943997540676, -0.16359908489415975, -0.0002159597298841169}};
//float pesos_capa_salida[36][3] = {{0.4102475389612772, -0.3096739700788772, -0.15356522554780408}, {-0.029439500244653673, -0.5372051159755392, -0.4244755116886216}, {0.6944701038143627, -0.19614082526701057, 0.724876164482796}, {0.5291466871172849, -0.6170122858853354, 1.0472191606955028}, {0.3878805495230681, -0.13147738764449415, 0.2603526600222792}, {1.0621413688375407, -1.0147268340576259, 0.761723324963208}, {-1.6037564808101787, -0.1509225022710514, 0.12927894757478486}, {0.5679035870551141, 0.13311474489249592, -0.9792291790859864}, {1.2093116921317457, -0.6715043726490381, -0.7792955934569168}, {-0.8204198674283809, -0.14529508362619314, 0.8253403607006037}, {-0.17509560549932526, 0.16161731577356342, 0.8965703131143995}, {1.1910883285101872, -0.7783001129884215, -1.0059502514657}, {0.9801940399881622, -0.5134195120831139, -0.0664167038607869}, {0.6962276720830516, 0.2717359170810297, -0.2923468820500657}, {0.623929302182533, 0.5365893331878117, 0.2892667880284969}, {-0.004514896028027288, 0.1672772186635923, -1.3384991612983046}, {0.10426736484521482, -0.6000272164166913, -0.40145978347317646}, {0.8051603674148686, -0.5147164701088232, 0.3274967203641922}, {0.005416655080193573, -0.7185735884948894, -1.1476765005552534}, {0.2911557553321598, 0.9477777529884559, 0.7534321566006728}, {-0.6611978245091065, 0.43371170366888956, -0.18176542026182535}, {-0.7471417463588462, 0.5847899848299022, -0.5427682766762186}, {-0.35263961646349634, -0.2709678303710479, -1.3421865004366642}, {-1.121758912738847, -1.3650372148664687, 0.30173024130498644}, {0.2806653818682526, -0.18813051892326718, -0.6700231465757861}, {0.17928627984369044, -0.4930902857698763, -0.3838709664113942}, {-0.30787855988069524, -0.37109550486135684, -0.05430268552361087}, {1.0663156376859522, 0.03930079981118298, 0.6674472357110314}, {0.8152116387186756, -0.8896692165123126, -0.9414585909386615}, {-1.0097381911142083, 1.0746297072433693, 0.05449044711371683}, {0.49705375579464384, -0.6125128357009435, -0.8464901406432435}, {-0.7682648514101363, 0.9640242966919988, -1.8277429706149309}, {0.7122618721136369, -0.8073394119538034, 1.0009172147301035}, {0.4358043473274983, 1.1598824210339633, 0.17596678080122918}, {-1.0220202570763604, -1.0557929552973095, -0.8489028683281732}, {-0.3136498839396814, 1.0625238501097265, 0.01697067090319965}};
float pesos_capa_oculta[3][36] = {{-1.0154563524971085, 1.1135562727366675, 0.6866045959756638, -1.195901333578544, 0.9997264160940112, 0.7671172568328608, 0.024853383076800867, -0.28835741978483176, -0.8922159659201706, -0.5285314191803984, 0.4711400673641437, -0.30150197671945483, 0.8309537101642024, 0.6314668417565416, 0.829971474940466, -0.7475384120960535, -0.1410572385370736, 0.35093395255713744, 0.8459034543079952, 0.21277836730556923, -0.5138121692359682, 0.5040245681187994, 0.2656495460047559, 0.5026136377585702, -0.0383393068290541, -0.9734152707040314, 0.576542521573534, -1.2139099606717083, -0.7780253843924234, 0.725456928703455, -0.7206000887864394, -1.35073646052926, 0.6189103604560102, 0.6019775685805926, -0.614005248974706, 0.8416903260395273}, {2.0107347635508948, 2.153827451253522, -0.10458953172814307, -0.20754668409750238, 1.8764436746118585, 0.7300134040008514, 0.040458186352619906, -0.076999996479599, -0.903071794319606, 0.0770548773454087, 0.5938072121862293, -0.19875376192560568, -0.22184092874735634, 0.7930326663244666, -1.3758468842207563, -1.264661517731953, -0.39237429577350763, 0.6992868436114505, -1.3026530139362928, 0.3589761771064634, 0.22050187607877342, 0.37115840108467363, -0.8015367744922166, -0.7233311912708091, 0.7216742692241103, -0.9383524323176654, -0.7362136452471727, 0.03221896983931052, 1.5691856167618101, -0.13058659545852108, 0.06113983234149112, 0.08794852322807281, 1.1498570682492182, -0.44871295895279334, -0.15843839772477367, 0.052127891433540165}, {0.01940313498436247, 0.22346946840949256, 0.5955802979267083, 0.6263043673023626, -0.19877821248775102, 0.1911337169651031, 0.2718966578197119, -1.0245648353871188, 0.7484044863683872, -0.8823770317304396, -0.821499414979286, 0.5739502836042273, 1.1225667956417837, -0.22476885000197028, -0.5893846699797601, 0.26644719729960703, 0.6888736934249061, -0.968642901324508, -0.07825783491276418, 1.155043488331826, -0.8239826995337257, 0.37100397446521416, 0.7527218139267379, -0.2740662573434268, 0.6893925888449615, 0.30220554961633145, 0.5746898299051902, -0.2739264106272582, 0.472990193880096, 0.3174880100801955, -0.369634837552142, 0.4634621406121702, 0.49741926005892384, 0.4686419442136146, -0.35274518315777054, 0.10887879296999065}};
float pesos_capa_salida[36][3] = {{1.5506464548531667, 0.9532872564940069, 0.20450391524197148}, {-1.3603921717630219, -1.2900496232635605, -0.15579692788936308}, {0.30859476302244865, -0.014777627574864487, -0.29665216749080303}, {-0.5044579860533502, -0.9865778916556237, 0.4702847562432901}, {-0.9129467947527411, -1.482495328006279, -0.25479331218045387}, {0.29476030887774224, -0.2572271449944936, 0.6411515457089986}, {0.08708202270625513, -0.6472334060994234, 0.638952814283772}, {-0.6361852791858913, 0.7319052674802776, 0.5890971909553572}, {0.5792442987265085, 0.1381132319007789, 0.27552897672132265}, {-0.4331437977946645, 0.5302700532399788, 0.9937089893679655}, {-0.32097655227544786, -0.24921573582960543, 1.0395346512504742}, {-0.8596350496494352, 0.8257936950232246, -0.49917298633114104}, {-0.3326299142498413, 0.4841242897600489, -0.8301067736563469}, {0.5021684509692744, -0.9938379945100019, -0.021782899588825358}, {-0.4781687444035301, -0.6854799561063678, -0.19875818705619036}, {0.1654065986433425, 1.0424092723853045, 0.15943753110420772}, {0.7177078538041542, 0.08390486056594876, -0.9045315181045889}, {0.4429551504660344, -0.23597218529709718, 0.5084769016084102}, {-0.15480672651745503, -0.9106821932230863, -0.5937664250524378}, {-0.5152279620988306, -0.8902341012416745, -1.0222474628683933}, {0.839304901855666, -0.909558412193103, 0.5308777456623329}, {0.18523844679771395, 0.08735999678145621, -0.6413644071589463}, {-0.8153555839606542, -0.8327667861490687, -0.24466403409786427}, {-0.06643293463847509, -0.27558216556847065, 0.8870729004177902}, {0.11344396127975363, 0.17828634633752932, -0.9480765305548363}, {0.8413708652655585, -0.5132139576260725, 0.10091988384628413}, {-0.44603628705659343, -0.4771836745654063, 0.40004522213891763}, {-0.9906273507281175, -0.7700872075049999, 0.32865099379609897}, {1.6122945857414073, 0.24351348927587513, -0.25892467163449995}, {0.1251800766441532, 0.12591025925390775, -0.5079818780843689}, {0.20771918552247665, -1.015031758502002, -0.440958045005456}, {-0.839820276440319, -0.45498859779707607, 0.5405019372891345}, {-0.31393219809998874, -0.40108450425860553, 0.32511915851132245}, {0.5109523484398983, -0.3020159099284111, -0.08820313841427303}, {-0.04929367324970908, -0.9049726398892849, 0.9656645191234501}, {1.0324916368063761, 1.0548241537459546, -0.265123978618414}};


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
    // Actuar sobre las salidas
    digitalWrite(pin_ventilador,      estado_ventilador);
    digitalWrite(pin_resistencia,     estado_resistencia);
    digitalWrite(pin_electrovalvula,  estado_electrovalvula); 
    Torito.println("Temp:" + String(temp)+ "°C" + "|" +"Hum:" + String(hum) + "% "+"Normalizadas>> Temp:" + String(estado_temp) + " Hum:" + String(estado_hum)+"Salida1:" + String(RNsalidas[0]) + " Salida2:" + String(RNsalidas[1]) + " Salida3:" + String(RNsalidas[2]));      
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
      sendCommand("AT+CIPSTART=0,\"TCP\",\""+ HOST +"\","+ PORT,15,"OK");
      sendCommand("AT+CIPSEND=0," +String(getData.length()+4),4,">");
      esp8266.println(getData);
      delay(1500);
      countTrueCommand++;
      sendCommand("AT+CIPCLOSE=0",5,"OK");
    }*/
    
    
   
    
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
  
}
 