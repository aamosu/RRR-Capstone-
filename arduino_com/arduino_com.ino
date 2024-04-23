#include <Servo.h>
#include <math.h>

#define MAX_SERVOS 12
#define MAX_PULSE 2500
#define MIN_PULSE 500

Servo Servos[MAX_SERVOS];
volatile int pulse0, pulse1, pulse2, pulse3, pulse4, pulse5, pulse6, pulse7, pulse8, pulse9,pulse10,pulse11;

const float theta1_forward[] = {54.46, 111.95, 179.82, 255.49, 211.65, 153.1, 145.67, 131.3, 109.68, 67.23, 54.46};
const float theta2_forward[] = {26.51, -32.61, -77.32, -5.09, 64.22, 124.77, 102.46, 67.34, 46.67, 33.1, 26.51};

const float theta1_updown[] = {77.47, 75.96, 121.52, 150.8, 179.8, 243.43};
const float theta2_updown[] = {101.68, 103.09, 56.03, 26.63, -3.22, -65.06};



const float theta1_turn[] = {121.52, 172.36, 220.93, 220.93, 172.36, 121.52, 121.52, 121.52, 121.52, 121.52, 121.52};
const float theta2_turn[] = {56.03, 4.52, -50.52, -50.52, 4.52, 56.03, 56.03, 56.03, 56.03, 56.03, 56.03};
const float theta3_turn[] = {54.46, 49.79, 54.78, 75.49, 94.66, 98.13, 88.36, 78.69, 69.62, 61.5, 54.46};

bool forward = false;
bool move_Backward = true;
bool turn_Right = false;
bool turn_Left = false;
bool _stop = false;

volatile int i = 0;
const int n = 11;
const int zero_index = 5;
volatile int j = zero_index;
volatile int k = 5;
volatile int m = 0;

void setup() {
  // put your setup code here, to run once:
  //FR
  Servos[0].attach(13);
  Servos[1].attach(2);
  Servos[2].attach(3,400,600);

  //FL
  Servos[3].attach(4);
  Servos[4].attach(5);
  Servos[5].attach(6,400,600);

  //BR
  Servos[6].attach(7,400, 600); //BR1 //neutral position at angle 135 degrees
  Servos[7].attach(8);
  Servos[8].attach(9);

  //BL
  Servos[9].attach(10,400,600);
  Servos[10].attach(11);
  Servos[11].attach(12);  
  
  Serial.begin(9600);
}

void loop() {
  if(forward == true){
    Serial.println("Forward");
    goForward();
    
  }
  if(turn_Right == true){
    turnRight();
  }
  if(turn_Left == true){
    turnLeft();
  }
  if(move_Backward == true){
    turnBack();
  }
  if(_stop == true){
    stop();
  }

}
void goForward(){
  // FR
    pulse0 = (int)(7.4074 * (135 - theta2_forward[j])) + 400;
    pulse1 = (int)(7.4074 * (225 - theta1_forward[j])) + 400;
    pulse2 = 15;

    // FL
    pulse3 = (int)(7.4074 * (225 - theta1_forward[k])) + 400;
    pulse4 = (int)(7.4074 * (135 - theta2_forward[k])) + 400;
    pulse5 = 15;

    // BR
    pulse6 = 15;
    pulse7 = (int)(7.4074 * (135 - theta2_forward[m])) + 400;
    pulse8 = (int)(7.4074 * (225 - theta1_forward[m])) + 400;

    // BL
    pulse9 = 15;
    pulse10 = (int)(7.4074 * (225 - theta1_forward[i])) + 400;
    pulse11 = (int)(7.4074 * (135 - theta2_forward[i])) + 400;

    moveServos(pulse0, pulse1, pulse2, pulse3, pulse4, pulse5, pulse6, pulse7,pulse8,pulse9,pulse10,pulse11);
    
    Serial.println(String(k)+" "+String(m));

    if(i == n -1){i=1;}
    else{i+=1;}
    if(j == 1){j = n - 1;}  
    else{j -= 1;}
    if(k == n -1){k=1;}
    else{k+=1;}
    if(m <= 1){m = n - 1;}  
    else{m -= 1;}
    delay(150);
}
void turnRight(){
  while(turn_Right==true){
    Serial.println("Right Turn");


    // FR
    pulse0 = (int)(7.4074 * (135 - theta2_forward[j])) + 400;
    pulse1 = (int)(7.4074 * (225 - theta1_forward[j])) + 400;
    pulse2 = 15;

    // FL
    pulse3 = (int)(7.4074 * (225 - theta1_forward[k])) + 400;
    pulse4 = (int)(7.4074 * (135 - theta2_forward[k])) + 400;
    pulse5 = 30;

    // BR
    pulse6 = 15;
    pulse7 = (int)(7.4074 * (135 - theta2_forward[m])) + 400;
    pulse8 = (int)(7.4074 * (225 - theta1_forward[m])) + 400;

    // BL
    pulse9 = 0;
    pulse10 = (int)(7.4074 * (225 - theta1_forward[i])) + 400;
    pulse11 = (int)(7.4074 * (135 - theta2_forward[i])) + 400;
    moveServos(pulse0, pulse1, pulse2, pulse3, pulse4, pulse5, pulse6, pulse7,pulse8,pulse9,pulse10,pulse11);
    Serial.println(String(i)+" "+String(j));

    if(i == n -1){i=1;}
    else{i+=1;}
    if(j == 1){j = n - 1;}  
    else{j -= 1;}
    if(k == n -1){k=1;}
    else{k+=1;}
    if(m <= 1){m = n - 1;}  
    else{m -= 1;}

    delay(65);
  }
}
void turnLeft(){
  while(turn_Left ==true){
    Serial.println("Left Turn");
    // FR
    pulse0 = (int)(7.4074 * (135 - theta2_forward[j])) + 400;
    pulse1 = (int)(7.4074 * (225 - theta1_forward[j])) + 400;
    pulse2 = 15;

    // FL
    pulse3 = (int)(7.4074 * (225 - theta1_forward[k])) + 400;
    pulse4 = (int)(7.4074 * (135 - theta2_forward[k])) + 400;
    pulse5 = 22;

    // BR
    pulse6 = 15;
    pulse7 = (int)(7.4074 * (135 - theta2_forward[m])) + 400;
    pulse8 = (int)(7.4074 * (225 - theta1_forward[m])) + 400;

    // BL
    pulse9 = 7;
    pulse10 = (int)(7.4074 * (225 - theta1_forward[i])) + 400;
    pulse11 = (int)(7.4074 * (135 - theta2_forward[i])) + 400;

    moveServos(pulse0, pulse1, pulse2, pulse3, pulse4, pulse5, pulse6, pulse7,pulse8,pulse9,pulse10,pulse11);
    Serial.println(String(i)+" "+String(j));

    if(i == n -1){i=1;}
    else{i+=1;}
    if(j == 1){j = n - 1;}  
    else{j -= 1;}
    if(k == n -1){k=1;}
    else{k+=1;}
    if(m <= 1){m = n - 1;}  
    else{m -= 1;}

    delay(65);
  }
}
void turnBack(){
  while(move_Backward==true){
    Serial.println("Backward");
    // FR
    pulse0 = (int)(7.4074 * (135 - theta2_forward[i])) + 400;
    pulse1 = (int)(7.4074 * (225 - theta1_forward[i])) + 400;
    pulse2 = 15;

    // FL
    pulse3 = (int)(7.4074 * (225 - theta1_forward[m])) + 400;
    pulse4 = (int)(7.4074 * (135 - theta2_forward[m])) + 400;
    pulse5 = 15;

    // BR
    pulse6 = 15;
    pulse7 = (int)(7.4074 * (135 - theta2_forward[k])) + 400;
    pulse8 = (int)(7.4074 * (225 - theta1_forward[k])) + 400;

    // BL
    pulse9 = 15;
    pulse10 = (int)(7.4074 * (225 - theta1_forward[j])) + 400;
    pulse11 = (int)(7.4074 * (135 - theta2_forward[j])) + 400;

    moveServos(pulse0, pulse1, pulse2, pulse3, pulse4, pulse5, pulse6, pulse7,pulse8,pulse9,pulse10,pulse11);
    Serial.println(String(k)+" "+String(m));

    if(i == n -1){i=1;}
    else{i+=1;}
    if(j == 1){j = n - 1;}  
    else{j -= 1;}
    if(k == n -1){k=1;}
    else{k+=1;}
    if(m <= 1){m = n - 1;}  
    else{m -= 1;}
    delay(150);
  }
}
void stop(){
  // FR
  pulse0 = (int)(7.4074 * (180)) + 400;
  pulse1 = (int)(7.4074 * (90)) + 400;
  pulse2 = 15;

  // FL
  pulse3 = (int)(7.4074 * (90)) + 400;
  pulse4 = (int)(7.4074 * (180)) + 400;
  pulse5 = 15;

  // BR
  pulse6 = 15;
  pulse7 = (int)(7.4074 * (180)) + 400;
  pulse8 = (int)(7.4074 * (90)) + 400;

  // BL
  pulse9 = 15;
  pulse10 = (int)(7.4074 * 90) + 400;
  pulse11 = (int)(7.4074 * 180) + 400;
}


void moveServos(int pulse0, int pulse1, int pulse2, int pulse3, int pulse4, int pulse5, int pulse6, int pulse7,int pulse8,int pulse9,int pulse10,int pulse11) { 

  Servos[0].writeMicroseconds(pulse0);
  Servos[1].writeMicroseconds(pulse1);
  Servos[2].write(pulse2);

  Servos[3].writeMicroseconds(pulse3);
  Servos[4].writeMicroseconds(pulse4);
  Servos[5].write(pulse5);

  Servos[6].write(pulse6);
  Servos[7].writeMicroseconds(pulse7);
  Servos[8].writeMicroseconds(pulse8);

  Servos[9].write(pulse9);
  Servos[10].writeMicroseconds(pulse10);
  Servos[11].writeMicroseconds(pulse11);

}

