const int FtrigPin = 22;
const int FechoPin = 23;
const int LtrigPin = 27;
const int LechoPin = 26;
const int RtrigPin = 24;
const int RechoPin = 25;
const int BtrigPin = 29;
const int BechoPin = 28;

// defines variables
long Fduration;
long Lduration;
long Rduration;
long Bduration;
int Fdistance; //in cm
int Ldistance; //in cm
int Rdistance; //in cm
int Bdistance; //in cm
void setup() {
  pinMode(FtrigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(FechoPin, INPUT); // Sets the echoPin as an Input
  pinMode(LtrigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(LechoPin, INPUT); // Sets the echoPin as an Input
  pinMode(RtrigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(RechoPin, INPUT); // Sets the echoPin as an Input
  pinMode(BtrigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(BechoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
}

void loop() {
  // Clears the trigPin
  digitalWrite(FtrigPin, LOW);
  digitalWrite(LtrigPin, LOW);
  digitalWrite(RtrigPin, LOW);
  digitalWrite(BtrigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(FtrigPin, HIGH);
  digitalWrite(LtrigPin, HIGH);
  digitalWrite(RtrigPin, HIGH);
  digitalWrite(BtrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(FtrigPin, LOW);
  digitalWrite(LtrigPin, LOW);
  digitalWrite(RtrigPin, LOW);
  digitalWrite(BtrigPin, LOW);
  // Reads the echoPin, returns the sound wave travel time in microseconds
  Fduration = pulseIn(FechoPin, HIGH);
  Lduration = pulseIn(LechoPin, HIGH);
  Rduration = pulseIn(RechoPin, HIGH);
  Bduration = pulseIn(BechoPin, HIGH);
  // Calculating the distance
  Fdistance = Fduration * 0.034 / 2;
  Ldistance = Lduration * 0.034 / 2;
  Rdistance = Rduration * 0.034 / 2;
  Bdistance = Bduration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  Serial.print("F");
  Serial.print(Fdistance);
  Serial.println("");
  Serial.print("L");
  Serial.print(Ldistance);
  Serial.println("");
  Serial.print("R");
  Serial.print(Rdistance);
  Serial.println("");
  Serial.print("B");
  Serial.print(Bdistance);
  Serial.println("");
  delay(1000);
}
