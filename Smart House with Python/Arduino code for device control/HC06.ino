#include <SoftwareSerial.h>
SoftwareSerial HC06(10, 11); //HC06-TX Pin 10, HC06-RX to Arduino Pin 11

int C1 = 7; //Use whatever pins you want 
int C2 = 6;
int C3 = 8;
int C4 = 9;

const int brightnessLevels[] = {
  0,    // Input value 0 corresponds to brightness level 0
  25,   // Input value 1 corresponds to brightness level 25
  50,   // Input value 2 corresponds to brightness level 50
  75,  // Input value 3 corresponds to brightness level 100
  100,  // Input value 4 corresponds to brightness level 150
};

void setup() {
  HC06.begin(9600); //Baudrate 9600 , Choose your own baudrate 
  pinMode(C1, OUTPUT);
  pinMode(C2, OUTPUT);
  pinMode(C3, OUTPUT);
  pinMode(C4, OUTPUT);

}

void loop() {

  if(HC06.available() > 0) //When HC06 receive something
  {
    char receive = HC06.read(); //Read from Serial Communication
    int brightness = map(receive, 0, 255, 1, 4);
    if(receive == '1') //If received data is 1, turn on the LED and send back the sensor data
    {
      digitalWrite(C2, LOW);
      HC06.println("Light off");
    }
    else if(receive == '2'){
      analogWrite(C2, brightnessLevels[brightness]); 
      HC06.println("Light on 50%");
    }
    else if(receive == '3'){
      digitalWrite(C2, HIGH);
      HC06.println("Light on 100%");
    }
    else if(receive == '4'){
      digitalWrite(C1, HIGH); 
      HC06.println("Fan on");
    }
    else if(receive == '5'){
      digitalWrite(C1, LOW); 
      HC06.println("Fan off");
    }
    else if(receive == '6'){
      digitalWrite(C3, HIGH); 
      HC06.println("Unlocked");
    }
    else if(receive == '7'){
      digitalWrite(C3, LOW); 
      HC06.println("Locked");
    }
    else if(receive == '8'){
      digitalWrite(C4, HIGH); 
      HC06.println("Garden lights on");
    }
    else if(receive == '9'){
      digitalWrite(C4, LOW); 
      HC06.println("Garden lights off");
    }
    
  }

}
