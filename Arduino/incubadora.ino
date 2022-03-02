/*#include <SoftwareSerial.h>
SoftwareSerial Torito(10,11);
//10 TXD
//11 RDX
int Led=5;
void setup(){
  Serial.begin(9600);
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
    
  }
  /*if(Serial.available()){
    Torito.write(Serial.read());
  }*/

//}