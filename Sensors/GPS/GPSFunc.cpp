double GPSLatLngMPHFeet (){

  while(serial_connection.available())
  {
    gps.encode(serial_connection.read());
  }
  if(gps.location.isUpdated())
  {
    Serial.println("Satellite Count:");
    Serial.println(gps.satellites.value()); //32 bit unsigned int (32)
    Serial.println("Latitude:");
    Serial.println(gps.location.lat(), 6); //lattitude in degrees (double)
    Serial.println("Longitude:");
    Serial.println(gps.location.lng(), 6); //longitude in degrees (double)
    Serial.println("Speed MPH:"); //NOTE***** for speed we should delay the 
    //gps pulse as speed calculation is less accurate the shorter between gps pulses
    //or we can just use readings from the IMU
    Serial.println(gps.speed.mph()); //speed in miles per hour (double)
    Serial.println("Altitude Feet:");
    Serial.println(gps.altitude.feet()); //altitude in feet, relative to sea level, (double)
    Serial.println("");

    Serial.println()
  }


}