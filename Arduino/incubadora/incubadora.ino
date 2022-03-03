#include <SoftwareSerial.h>
//Paso 1
#include "DHT.h"

//Paso 2
#define DHTPIN 2
#define DHTTYPE DHT11
SoftwareSerial Torito(10,11);
//10 TXD
//11 RDX
int Led=5;
DHT dht(DHTPIN, DHTTYPE);

void setup(){
  //Paso 4
  Serial.begin(9600);
  Serial.println("DHTxx test!");
  dht.begin();
  Serial.println("Listo");
  Torito.begin(38400);
  pinMode(Led,OUTPUT);
  
}
void loop(){
  if(Torito.available()){//habilitado
    char leer=Torito.read();    
    if(leer=='1'){
      digitalWrite(Led,HIGH);
    }
    if(leer=='0'){
      digitalWrite(Led,LOW);
    }
    delay(2000);
    
    //Paso 5
    float h = dht.readHumidity();
    
    //Paso 6
    float t = dht.readTemperature();
    
    //Paso 7
    float f = dht.readTemperature(true);

    //Paso 8
    if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
    }

    //Paso 9
    float hif = dht.computeHeatIndex(f, h);
    float hic = dht.computeHeatIndex(t, h, false);

    //Paso 10
    Serial.print("Humidity: ");
    Serial.print(h);
    Serial.print(" %\t");
    Serial.print("Temperature: ");
    Serial.print(t);
    Serial.print(" *C ");
    Serial.print(f);
    Serial.print(" *F\t");
    Serial.print("Heat index: ");
    Serial.print(hic);
    Serial.print(" *C ");
    Serial.print(hif);
    Serial.println(" *F");
    
  }
  /*if(Serial.available()){
    Torito.write(Serial.read());
  }*/

}
