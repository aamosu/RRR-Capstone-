#include <Wire.h>
#include "TinyGPSPlus.h"
#include "SoftwareSerial.h"

SoftwareSerial serial_connection(30, 31); //RX from GPS into pin ~11, TX from GPS into pin ~10
TinyGPSPlus gps;

short x,y,z;
int maxX, maxY, maxZ;
int minX, minY, minZ;
int offX, offY, offZ;

float an, lat, lng;

void setup() {
  Serial.begin(115200);
  serial_connection.begin(9600);
  Wire.begin();
  Wire.beginTransmission(0x0d);
  Wire.write(0x09);
  Wire.write(0x05);
  Wire.write(0x00);
  Wire.write(0x01);
  Wire.endTransmission();
  maxX = -32767; maxY = -32767;
  maxZ = -32767;
  minX = 32767; minY = 32767;
  minZ = 32767;
  offX = 0; offY = 0; offZ = 0;
}

void get_Heading() {
  int reg[6];
  int i;
  Wire.beginTransmission(0x0d);
  Wire.write(0x00);
  Wire.endTransmission(false);
  Wire.requestFrom(0x0d,6);
  while(Wire.available() < 6) {
    delay(1);
  }
  for(i=0;i<6;i++) reg[i] = Wire.read();
  x = (reg[1] << 8) | reg[0];
  y = (reg[3] << 8) | reg[2];
  z = (reg[5] << 8) | reg[4];
  if (x > maxX) maxX = (int)x;
  if (x < minX) minX = (int)x;
  if (y > maxY) maxY = (int)y;
  if (y < minY) minY = (int)y;
  if (z > maxZ) maxZ = (int)z;
  if (z < minZ) minZ = (int)z;
  offX = (maxX + minX) / 2;
  offY = (maxY + minY) / 2;
  offZ = (maxZ + minZ) / 2;
  int fx = (int)x - offX;
  int fy = (int)y - offY;
  int fz = (int)z - offZ;
  an = atan2((float)y,(float)x);
  an = an * 180.0 / 3.14159;
  an = an + 180.0;
}

void print_GPS()
{
  while(serial_connection.available())
  {
    gps.encode(serial_connection.read());
  }
  if(gps.location.isUpdated())
  {
    lat = gps.location.lat();
    lng = gps.location.lng();
    String p2=",";
    Serial.println(an + p2 + lat + p2 + lng);
  }
}

void loop() {
  get_Heading();
  print_GPS();
}
