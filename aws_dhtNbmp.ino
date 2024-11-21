// del useless data(temp(F), altitude, heat index)

#include "DHT.h"
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BMP280.h>

// DHT Sensor
#define DHTPIN 8     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT22   // DHT 22 (AM2302) used
DHT dht(DHTPIN, DHTTYPE);

// BMP280 Sensor
#define BMP_SCK  (13)
#define BMP_MISO (12)
#define BMP_MOSI (11)
#define BMP_CS   (10)
Adafruit_BMP280 bmp; // I2C

void setup() {
  Serial.begin(9600);
  
  dht.begin();
  unsigned status = bmp.begin();

  if (!status) {
    Serial.println(F("Could not find a valid BMP280 sensor, check wiring or try a different address!"));
    while (1) delay(10);
  }

  // BMP280 default settings
  bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode */
                  Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
                  Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
                  Adafruit_BMP280::FILTER_X16,      /* Filtering */
                  Adafruit_BMP280::STANDBY_MS_500); /* Standby time */
}

void loop() {
  // Wait 2 seconds between measurements
  delay(2000);

  // Reading data from DHT sensor
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Check if any reads failed
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Reading data from BMP280 sensor
  float bmpTemp = bmp.readTemperature();
  float bmpPressure = bmp.readPressure();

  // Print DHT sensor data
  Serial.print(h);
  Serial.print(F(" "));
  Serial.print(t);
  Serial.print(F(" "));

  // Print BMP280 sensor data
  Serial.print(bmpTemp);
  Serial.print(F(" "));
  Serial.print(bmpPressure);
  Serial.print(F(" "));