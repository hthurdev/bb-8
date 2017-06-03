#ifndef soundDefinitions_h
#define soundDefinitions_h

#include "WaveHC.h"
#include "waveUtil.h"

int button1 = 1;
int button2 = 2;
int button3 = 3;
int button4 = 4;

int button1state = 0;
int button2state = 0;
int button3state = 0;
int button4state = 0;

void angry() {
  playcomplete("angry.wav")
}

void giddy() {
  playcomplete("giddy.wav")
}

void happyStatic() {
  playcomplete("happyStatic.wav")
}

void yes() {
  playcomplete("yes.wav")  
}

void yahoo() {
  playcomplete("yahoo.wav")  
}
void firmware() {
  playcomplete("firmware.wav")
}

void headturn() {
  playcomplete("headturn.wav")
}

void poke() {
  playcomplete("poke.wav")
}

void newFirmware() {
  playcomplete("newFirmware.wav")
}

void proximity() {
  playcomplete("proximity.wav")
}

void readyy() {
  playcomplete("readyy.wav")
}

void upset() {
  playcomplete("upset.wav")
}

void waggle() {
  playcomplete("waggle.wav")
}

#endif
