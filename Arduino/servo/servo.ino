// Incluímos la librería para poder controlar el servo
#include <Servo.h>
 
// Declaramos la variable para controlar el servo
Servo servoMotor;
 
void setup() {
  // Iniciamos el servo para que empiece a trabajar con el pin 9
  servoMotor.attach(9);
}
 
void loop() {
  
  
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
  delay(3600000);
 
 /*
  // Desplazamos a la posición 180º
  servoMotor.write(45);
  // Esperamos 1 segundo
  delay(5000);
  // Desplazamos a la posición 180º
  servoMotor.write(105);
  // Esperamos 1 segundo
  delay(5000); 
 */
  
}
