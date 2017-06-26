int PinNullBtn = 0 ;
int PinOneBtn = 1 ;
int PinTwoBtn = 2 ;
int PinThreeBtn = 3 ;
int PinFourBtn = 4 ;
int PinFiveBtn = 5 ;
int PinSixBtn = 6 ;
int PinSevenBtn = 7 ;
int PinEightBtn = 8 ;
int PinNineBtn = 9 ;
int InputZero = 0 ;
int InputOne = 0 ;
int InputTwo = 0 ;
int InputThree = 0 ;
int InputFour = 0 ;
int InputFive = 0 ;
int InputSix = 0 ;
int InputSeven = 0 ;
int InputEight = 0 ; 
int InputNine = 0 ;

void setup() {
  Serial.begin(9600) ;
pinMode(PinNullBtn, INPUT) ;
pinMode(PinTwoBtn, INPUT) ;
pinMode(PinOneBtn, INPUT) ;
pinMode(PinThreeBtn, INPUT) ;
pinMode(PinFourBtn, INPUT) ;
pinMode(PinFiveBtn, INPUT) ;
pinMode(PinSixBtn, INPUT) ;
pinMode(PinSevenBtn, INPUT) ;
pinMode(PinEightBtn, INPUT) ;
pinMode(PinNineBtn, INPUT) ;
}

void loop() {
InputZero = digitalRead(PinNullBtn) ;
InputOne = digitalRead(PinOneBtn) ;
InputTwo = digitalRead(PinTwoBtn) ;
InputThree = digitalRead(PinThreeBtn) ;
InputFour = digitalRead(PinFourBtn) ;
InputFive = digitalRead(PinFiveBtn) ;
InputSix = digitalRead(PinSixBtn) ;
InputSeven = digitalRead(PinSevenBtn) ;
InputEight = digitalRead(PinEightBtn) ;
InputNine = digitalRead(PinNineBtn) ;

if ( InputZero= "HIGH" )
{
  Serial.println("a") ; 
} 
else if ( InputTwo = "HIGH" )
{ 
  Serial.println("b") ;
}
else if ( InputOne = "HIGH" )
{ 
  Serial.println("c") ;
}
else if ( InputThree = "HIGH" )
{ 
  Serial.println("d") ;
}
else if ( InputFour = "HIGH" )
{ 
  Serial.println("e") ;
}
else if ( InputFive = "HIGH" )
{ 
  Serial.println("f") ;
}
else if ( InputSix = "HIGH" )
{ 
  Serial.println("g") ;
}
else if ( InputSeven = "HIGH" )
{ 
  Serial.println("h") ;
}
else if ( InputEight = "HIGH" )
{ 
  Serial.println("i") ;
}
else if ( InputNine = "HIGH" )
{ 
  Serial.println("j") ;
}
}
