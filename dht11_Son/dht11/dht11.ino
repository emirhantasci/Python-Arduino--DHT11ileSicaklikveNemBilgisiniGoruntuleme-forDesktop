
//dht11 for python
#include <dht11.h>

dht11 DHT11;

void setup()
{
  DHT11.attach(2);
  Serial.begin(9600);
  
}

void loop()
{ 
  int chk = DHT11.read();

  Serial.print((int)DHT11.humidity, DEC);
  Serial.print(" ve ");
  Serial.println((int)DHT11.temperature, DEC);

  delay(1000);
}
