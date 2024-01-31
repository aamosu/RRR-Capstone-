#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
Servo servo7;
Servo servo8;

int pos = 0;
int time1 = 0;
int time2 = 0;

void setup() {
  servo1.attach(10,400,2000);
  servo2.attach(2,400,2000);
  servo3.attach(3,400,2000);
  servo4.attach(4,400,2000);
  servo5.attach(5,400,2000);
  servo6.attach(11,400,2000);
  servo7.attach(7,400,2000);
  servo8.attach(8,400,2000);
  Serial.begin(9600);
}

void loop() {
  while(time1 < 10){
    //Manual Forward movement
    //Back Right
    servo8.write(0);  
    servo7.write(45);

    //Front Left
    servo2.write(180);    
    servo1.write(135);
    delay(1000);

    servo7.write(135);
    servo1.write(45);
    delay(100);

    servo8.write(180);
    servo2.write(0);
    delay(50);

    //Back Left 
    servo6.write(180);    
    servo5.write(190);

    //Front Right
    servo4.write(0);    
    servo3.write(45);
    delay(1000);

    servo5.write(80);
    servo3.write(135);
    delay(100);

    servo6.write(0);
    servo4.write(180);
    delay(50);
    time1 += 1;
  }
  while(time2 < 5){
    //Turn
    time2 += 1;
  }
  time1 = 0;
  time2 = 0;
}
