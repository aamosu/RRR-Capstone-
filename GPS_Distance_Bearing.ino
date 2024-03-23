#include <iostream>
#include <math.h>
double lat1 = 38.897113;
double lon1 = -77.049042;
double lat2 = 38.899722;
double lon2 = -77.047712;

//convert degrees to radians
double dtor(double fdegrees) {
  return(fdegrees * M_PI / 180);
}

//convert radians to degrees
double rtod(double fradians) {
  return(fradians * 180.0 / M_PI);
}

long CalcDistance(double lat1, double lon1, double lat2, double lon2) {
  double dlon, dlat, a, c;
  double dist = 0.0;
  dlon = dtor(lon2 - lon1);
  dlat = dtor(lat2 - lat1);
  a = pow(sin(dlat/2),2) + cos(dtor(lat1)) * cos(dtor(lat2)) * pow(sin(dlon/2),2);
  c = 2 * atan2(sqrt(a), sqrt(1-a));

  dist = 20925656.2 * c;  //radius of the earth (6378140 meters) in feet 20925656.2
  return( (long) dist + 0.5);
}

int CalcBearing(double lat1, double lon1, double lat2, double lon2) {
  lat1 = dtor(lat1);
  lon1 = dtor(lon1);
  lat2 = dtor(lat2);
  lon2 = dtor(lon2);

  //determine angle
  double bearing = atan2(sin(lon2-lon1)*cos(lat2), (cos(lat1)*sin(lat2))-(sin(lat1)*cos(lat2)*cos(lon2-lon1)));
  //convert to degrees
  bearing = rtod(bearing);
  //use mod to turn -90 = 270
  bearing = fmod((bearing + 360.0), 360);
  return (int) bearing + 0.5; //bearing returned is read as 0 degrees = North, 90 degrees = East ect.
}

int main() {
  //Serial.begin(9600);
  std::cout << "Distance towards Rocket from Robot is: " << CalcDistance(lat1, lon1, lat2, lon2) << " ft";
  std::cout << "\n";
  std::cout << "Bearing towards Rocket from Robot is: " << CalcBearing(lat1, lon1, lat2, lon2) << " degrees";
  return 0;
}
