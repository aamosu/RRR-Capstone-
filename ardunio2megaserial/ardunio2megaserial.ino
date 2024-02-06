// Include the Arduino Serial library
#include <Arduino.h>

// Functions
import 

void setup() {

  // Initialize serial communication at 9600 baud rate
  Serial.begin(9600);
  sendData(ultrasonicData,GPSData,IMUGPS,LiDarData);
}

void loop() {

    int ultrasonicData= ultrasonic();
    long long float GPSData= GPS();
    float IMUData= IMU();
    float LiDarData= Lidar();
}

void sendData(int sensor1Value, long long float sensor2Value,float sensor1Value, float sensor2Value) {



}
