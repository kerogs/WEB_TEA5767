#include <Wire.h>
#include <KS_TEA5767.h>
#include <ArduinoJson.h>

KS_TEA5767 radio;

float frequency = 104.5;
unsigned int serial = 9600;

void setup() {
  Serial.begin(serial);
  Wire.begin();
  radio.begin();

  radio.setFrequency(frequency);
}

void loop() {
  unsigned long currentTime = millis();

  // Serial.println("coucoucou");
  delay(1000);

  String message;
  while(!Serial.available()){
    message = Serial.read();
    if (message == "1") {
      sendRadioData();
    } else{
      Serial.println("unknow command");
    }
    // if(message != 1) {
    //   // message2Float
    //   float messageFloat = message.toFloat();
    //   frequency = messageFloat;
    //   radio.setFrequency(messageFloat);
    // }
  };
}

void sendRadioData() {
  StaticJsonDocument<512> doc;

  doc["frequency"] = frequency;  
  doc["sendInterval"] = 0;  

  JsonObject data = doc.createNestedObject("data");

  // Ajouter les informations dans l'objet "data"
  data["PLL"] = radio.getPLL() ? "LOCKED" : "UNLOCKED";
  data["RSSI"] = radio.getRSSI();
  data["RSSIdBm"] = radio.getRSSIdBm(radio.getRSSI());
  data["stereo"] = radio.getStereo() ? "STEREO" : "MONO";
  data["hex"] = radio.getHex();
  data["ASCII"] = radio.getASCII();

  serializeJson(doc, Serial);
  Serial.println();
}
