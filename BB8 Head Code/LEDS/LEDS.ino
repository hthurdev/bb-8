#include "FastLED.h"
#include "definitions.h"

int incomingByte = 0;

void setup() {
  FastLED.addLeds<WS2801, RGB>(leds, NUM_LEDS);
  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) {
      incomingByte = Serial.read();
        if (incomingByte == s1) {
          //
        }
        else if (incomingByte == s2) {
          //
        }
        else {
          psiStatic();
          hpStatic();
          eyeStatic);
          logicOneStatic();
          logicTwoStatic();
          logicThreeStatic();
        }
  }
 
  FastLED.show();
}
