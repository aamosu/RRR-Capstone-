// Include the Arduino Serial library
#include <Arduino.h>
#include "ultrasonicFunc.h"
//#include "ultrasonicFunc.cpp"


// Pins for ultrasonic sensor
//left
const int trigPinUS0 = 13;
const int echoPinUS0 = 12;

//front middle
const int trigPinUS1 = 9;
const int echoPinUS1 = 8;

//right
const int trigPinUS2 = 5;
const int echoPinUS2 = 4;


void setup() {

  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);
  //Sesnor 1 
  ultrasonicSetup(0,trigPinUS0,echoPinUS0);
  //Sensor 2
  ultrasonicSetup(1,trigPinUS1,echoPinUS1);
  //Sensor 3
  ultrasonicSetup(2,trigPinUS2,echoPinUS2);

}

void loop() {

  int disSen0=ultrasonicLoop(0,trigPinUS0,echoPinUS0);
  int disSen1=ultrasonicLoop(1,trigPinUS1,echoPinUS1);
  int disSen2=ultrasonicLoop(2,trigPinUS2,echoPinUS2);
  Serial.println("L"+ String(disSen0));
  Serial.println("F"+ String(disSen1));
  Serial.println("R"+ String(disSen2));
  delay(5000);
}




