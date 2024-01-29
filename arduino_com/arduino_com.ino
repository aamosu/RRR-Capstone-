#include <Servo.h>
#include <math.h>

#define MAX_SERVOS 8
#define MAX_PULSE 2500
#define MIN_PULSE 500

Servo Servos[MAX_SERVOS];
int pulse0, pulse1, pulse2, pulse3, pulse4, pulse5, pulse6, pulse7;

unsigned long previousMillis = 0;
const long interval = 20;
double t;

const byte numChars = 32;
char receivedChars[numChars];
int spaceCounter = 0;

boolean newData = false;
char a;
int pulse;

void setup() {
  // put your setup code here, to run once:
  //BR
  Servos[0].attach(10);
  Servos[1].attach(2);

  //BL
  Servos[2].attach(3);
  Servos[3].attach(4);

  //FR
  Servos[4].attach(5);
  Servos[5].attach(11);

  //FL
  Servos[6].attach(7);
  Servos[7].attach(8);

  Serial.begin(9600);
}

void loop() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    //t = float(currentMillis) / 1000;

    getData();
    //Serial.print(pulse0);
    moveServos(pulse0, pulse1, pulse2, pulse3, pulse4, pulse5, pulse6, pulse7);
    newData = false;
  }
}

void moveServos(int pulse0, int pulse1, int pulse2, int pulse3, int pulse4, int pulse5, int pulse6, int pulse7) { 

  Servos[0].writeMicroseconds(pulse0);
  Servos[1].writeMicroseconds(pulse1);

  Servos[2].writeMicroseconds(pulse2);
  Servos[3].writeMicroseconds(pulse3);

  Servos[4].writeMicroseconds(pulse4);
  Servos[5].writeMicroseconds(pulse5);

  Servos[6].writeMicroseconds(pulse6);
  Servos[7].writeMicroseconds(pulse7);
}

void getData() {
  static boolean receiving = false;
  static byte index = 0;

  while (Serial.available() > 0 && newData == false) {
    char a = Serial.read();
    
    if (a == '<') {
      receiving = true;
      index = 0;
      memset(receivedChars, 0, numChars);
    } else if (receiving && a == '>') {
      receiving = false;
      newData = true;
    } else if (receiving) {
      receivedChars[index] = a;
      index++;
      if (index >= numChars) {
        index = numChars - 1;
      }
    }
  }
}

void parseData() {
  char *token = strtok(receivedChars, "#");
  
  pulse0 = atoi(token);
  token = strtok(NULL, "#");
  pulse1 = atoi(token);
  token = strtok(NULL, "#");
  pulse2 = atoi(token);
  token = strtok(NULL, "#");
  pulse3 = atoi(token);
  token = strtok(NULL, "#");
  pulse4 = atoi(token);
  token = strtok(NULL, "#");
  pulse5 = atoi(token);
  token = strtok(NULL, "#");
  pulse6 = atoi(token);
  token = strtok(NULL, "#");
  pulse7 = atoi(token);
}