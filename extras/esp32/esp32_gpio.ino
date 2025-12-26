#include <Arduino.h>

// Simple ESP32 sketch to listen on Serial for commands of the form:
// GPIO <pin> <state>\n  e.g. "GPIO 2 1" to set pin 2 HIGH

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("ESP32 GPIO controller ready");
}

String readLine() {
  String s;
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') break;
    if (c == '\r') continue;
    s += c;
  }
  return s;
}

void loop() {
  if (Serial.available()) {
    String line = readLine();
    line.trim();
    if (line.length() == 0) return;
    // parse
    if (line.startsWith("GPIO ")) {
      int firstSpace = line.indexOf(' ');
      int secondSpace = line.indexOf(' ', firstSpace + 1);
      if (secondSpace > firstSpace) {
        String pinStr = line.substring(firstSpace + 1, secondSpace);
        String stateStr = line.substring(secondSpace + 1);
        int pin = pinStr.toInt();
        int state = stateStr.toInt();
        pinMode(pin, OUTPUT);
        digitalWrite(pin, state ? HIGH : LOW);
        Serial.print("OK GPIO "); Serial.print(pin); Serial.print(" "); Serial.println(state);
      } else {
        Serial.println("ERR malformed");
      }
    } else {
      Serial.println("IGNORE");
    }
  }
  delay(10);
}
