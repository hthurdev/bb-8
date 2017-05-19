#include "FastLED.h"
#include "definitions.h"

void setup() {
  FastLED.addLeds<WS2801, RGB>(leds, NUM_LEDS);
  Serial.begin(9600);  
}

void loop() {
  
}

FastLED.show();
}
