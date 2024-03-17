#ifndef ULTRASONICFUNC_H
#define ULTRASONICFUNC_H

void ultrasonicSetup(char USnum, const int trigPin, const int echoPin);
int ultrasonicLoop(char USnum, const int trigPin, const int echoPin);

#endif