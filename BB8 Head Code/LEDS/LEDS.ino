#include "FastLED.h"
#include "definitions.h"



void setup() {
  FastLED.addLeds<WS2801, RGB>(leds, NUM_LEDS);
}

void loop() {
  PSI();
  HP();
  eye();
  logicOne();
  logicTwo();
  logicThree();
 
  FastLED.show();
}
