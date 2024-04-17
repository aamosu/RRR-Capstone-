// Include the Arduino Serial library
#include <Arduino.h>
#include "ultrasonicFunc.h"

#include "GPS.h"
#include "Gyro.h"
//#include "ultrasonicFunc.cpp"


// Pins for ultrasonic sensor
//left
const int trigPinUS0 = 45;
const int echoPinUS0 = 44;

//front middle
const int trigPinUS1 = 23;
const int echoPinUS1 = 22;

//right
const int trigPinUS2 = 39;
const int echoPinUS2 = 38;


void setup() {

  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);
  //Sesnor 1 
  ultrasonicSetup(0,trigPinUS0,echoPinUS0);
  //Sensor 2
  ultrasonicSetup(1,trigPinUS1,echoPinUS1);
  //Sensor 3
  ultrasonicSetup(2,trigPinUS2,echoPinUS2);

  GPSSetup();
  GyroSetup();

}

void loop() {

  int disSen0=ultrasonicLoop(0,trigPinUS0,echoPinUS0);
  int disSen1=ultrasonicLoop(1,trigPinUS1,echoPinUS1);
  int disSen2=ultrasonicLoop(2,trigPinUS2,echoPinUS2);
  float 
  Serial.print("F"+ String(disSen1));
  Serial.print("L"+ String(disSen0));
  Serial.print("R"+ String(disSen2));
  Serial.println("");
  delay(2000);
}




