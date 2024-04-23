
#include <Servo.h>
#include <math.h>

#define MAX_SERVOS 12
#define MAX_PULSE 2500
#define MIN_PULSE 500
#define PULSE_SCALE 7.4074
#define BASE_PULSE 4000
#define SERIAL_BUFFER_SIZE 32

enum MovementCommand { STOP, FORWARD, BACKWARD, TURN_RIGHT, TURN_LEFT, NONE };

struct MovementAngle {
    float theta1;
    float theta2;
};

Servo Servos[MAX_SERVOS];
volatile int pulses[MAX_SERVOS];

MovementCommand currentCommand = NONE;
MovementCommand lastCommand = NONE;
String commando;
char command;

const MovementAngle forwardAngles[] = {
    {54.46, 26.51}, {111.95, -32.61}, {179.82, -77.32}, {255.49, -5.09}, 
    {211.65, 64.22}, {153.1, 124.77}, {145.67, 102.46}, {131.3, 67.34}, 
    {109.68, 46.67}, {67.23, 33.1}, {54.46, 26.51}
};

void setup() {
    for (int i = 0; i < MAX_SERVOS; i++) {
        Servos[i].attach(2 + i);  // Example pin assignment
    }
    Serial.begin(115200);
}

void loop() {


    if (Serial.available() > 0) {
        commando = Serial.readStringUntil('\n');
        commando.trim();
        if (commando.length() > 0) {
            handleSerialCommands(commando);
            delay(10);
            performMovement();
        }
    }

    if (currentCommand != lastCommand) {
        executeStop();  // Stop previous movement immediately on command change
        lastCommand = currentCommand;  // Update lastCommand to the new command
        delay(10);
        performMovement();
    }

/*

  handleSerialCommands("F");
  performMovement();
  delay(100);

  handleSerialCommands("B");
  performMovement();
  
  //delay(100);  // Adjust delay as needed
*/
  delay(1);  // Adjust delay as needed
}

void handleSerialCommands(String commando) {
   char command = commando.charAt(0);
    Serial.println("Received Command: " + commando);
    switch (command) {
        case 'F': currentCommand = FORWARD; break;
        case 'B': currentCommand = BACKWARD; break;
        case 'R': currentCommand = TURN_RIGHT; break;
        case 'L': currentCommand = TURN_LEFT; break;
        case 'S': currentCommand = STOP; break;
        default: 
            Serial.println("Unknown command: " + String(command));
            break;
    }
}

void performMovement() {
    static int index = 0;
    if (currentCommand == STOP) {
        executeStop();
        return;
    }

    switch (currentCommand) {
        case FORWARD: executeForward(index); break;
        case BACKWARD: executeBackward(index); break;
        case TURN_RIGHT: executeTurnRight(index); break;
        case TURN_LEFT: executeTurnLeft(index); break;
        default: break;
    }
    index = (index + 1) % (sizeof(forwardAngles) / sizeof(forwardAngles[0]));
}

void executeForward(int index) {
  while(currentCommand==FORWARD){
    Serial.println("Moving Forward");
    setMovement(forwardAngles[index].theta1, forwardAngles[index].theta2);
  }
}

void executeBackward(int index) {
  while(currentCommand==BACKWARD){
    Serial.println("Moving Backward");
    setMovement(forwardAngles[index].theta1, forwardAngles[index].theta2);
  }
}

void executeTurnRight(int index) {
    Serial.println("Turning Right");
    setMovement(forwardAngles[index].theta1, forwardAngles[index].theta2);
}

void executeTurnLeft(int index) {
    Serial.println("Turning Left");
    setMovement(forwardAngles[index].theta1, forwardAngles[index].theta2);
}

void executeStop() {
  while(currentCommand==STOP){
    Serial.println("STOP");
    for (int i = 0; i < MAX_SERVOS; i++) {
        Servos[i].writeMicroseconds(BASE_PULSE);  // Neutral position or safe stop
    }

  }
}

void setMovement(float theta1, float theta2) {
    for (int i = 0; i < MAX_SERVOS; i += 3) {
        pulses[i] = BASE_PULSE + (int)(PULSE_SCALE * (180 - theta1));
        pulses[i + 1] = BASE_PULSE + (int)(PULSE_SCALE * (90 - theta2));
        Servos[i].writeMicroseconds(pulses[i]);
        Servos[i + 1].writeMicroseconds(pulses[i + 1]);
        Servos[i + 2].write(90);  // Default for the third servo in each group
    }
}
