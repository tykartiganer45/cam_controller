#include <Wire.h>

#include <Adafruit_MCP23017.h>


Adafruit_MCP23017 mcp1;


String command, value, value2;
float v, vals, val, val2, i, x;

byte pin[] = {0,1,4,5,6,7,8,10,11,12};

byte pinCount = sizeof(pin) / sizeof(pin[0]);

void setup() {
  // put your setup code here, to run once:
  Serial.begin((unsigned char)115200);
  mcp1.begin();

  for (int x = 0; x < 16; x++)
  {
    mcp1.pinMode(x, OUTPUT);
    mcp1.digitalWrite(x, HIGH);
  }

  for (byte i = 0; i < pinCount; i++)
  {
    pinMode(pin[i], OUTPUT);
    digitalWrite(pin[i], HIGH);
  }
//  pinMode(0, OUTPUT);
//  pinMode(1, OUTPUT);
//  pinMode(11, OUTPUT);
//  pinMode(12, OUTPUT);
//  pinMode(4, OUTPUT);
//  pinMode(5, OUTPUT);
//  pinMode(6, OUTPUT);
//  pinMode(7, OUTPUT);
//  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(13, INPUT);
//  pinMode(10, OUTPUT);

//  digitalWrite(0, HIGH);
//  digitalWrite(1, HIGH);
//  digitalWrite(4, HIGH);
//  digitalWrite(5, HIGH);
//  digitalWrite(6, HIGH);
//  digitalWrite(7, HIGH);
//  digitalWrite(8, HIGH);
  digitalWrite(9, LOW);
//  digitalWrite(10, HIGH);
//  digitalWrite(11,HIGH);
//  digitalWrite(12, HIGH);
;

}
void PowerOn() {
      digitalWrite(0, LOW);
      delay(3000);
      digitalWrite(0, HIGH);
      delay(500);
      digitalWrite(0, LOW);
      delay(500);
      digitalWrite(0, HIGH);
  
}

void PowerOff() {
      digitalWrite(1, LOW);
      delay(3000);
      digitalWrite(1, HIGH);
      delay(500);
      digitalWrite(1, LOW);
      delay(500);
      digitalWrite(1, HIGH);
}
void Record() {
      digitalWrite(11, LOW);
      delay(300); //Change Delay
      digitalWrite(11, HIGH);
}

void Stop() {
      digitalWrite(11, LOW);
      delay(300); //Change Delay
      digitalWrite(11, HIGH);
}

void ZoomIn() {
      digitalWrite(12, LOW);
      delay(vals);
      digitalWrite(12, HIGH);
      delay(100);
      digitalWrite(12, LOW);
      delay(100);
      digitalWrite(12, HIGH);
  
}

void Capture() {
      digitalWrite(5,LOW);
      delay(100);
      digitalWrite(5,HIGH);
      
  
}

void ZoomOut() {
      digitalWrite(4, LOW);
      delay(vals);
      digitalWrite(4, HIGH);
      delay(100);
      digitalWrite(4, LOW);
      delay(100);
      digitalWrite(4, HIGH);
}

void Menu() {
      digitalWrite(6,LOW);
      delay(500);
      digitalWrite(6,HIGH);
      delay(500);
      digitalWrite(6,LOW);
      delay(500);
      digitalWrite(6,HIGH);
}

void Move() {
      digitalWrite(7,LOW);
      delay(20);
      digitalWrite(7,HIGH);
      delay(20);
      digitalWrite(7,LOW);
      delay(20);
      digitalWrite(7,HIGH);
      delay(1000);
}

void Ex() {
      digitalWrite(8,LOW);
      delay(20);
      digitalWrite(8,HIGH);
      delay(20);
      digitalWrite(8,LOW);
      delay(20);
      digitalWrite(8,HIGH);

}

void TransferOn() {
      digitalWrite(10, LOW);
      digitalWrite(9,HIGH);
     
}

void TransferOff() {
      digitalWrite(9,LOW);
      digitalWrite(10, HIGH);
      
     
}

void Control(){
      if( val == 0 )
      {
        mcp1.digitalWrite(0, HIGH);
        for (int x = 1; x < 16; x++)
        {
          mcp1.pinMode(x, OUTPUT);
          mcp1.digitalWrite(x, LOW);
        }
        
      }
      
      else if( val > 0 && val < 16){
        mcp1.digitalWrite(val, HIGH);
        for (int x = (val - (val -1) -1); x < val ; x++){
          mcp1.pinMode(x, OUTPUT);
          mcp1.digitalWrite(x, LOW);
           
        }
        for (int x = (val+1); x < 16; x++)
        {
          mcp1.pinMode(x, OUTPUT);
          mcp1.digitalWrite(x, LOW);
        }
      }
        
       else if ( val == 16.0 ) {
         for (int x = 0; x < 16; x++)
          {
            mcp1.pinMode(x, OUTPUT);
            mcp1.digitalWrite(x, HIGH);
          }
        
       }
      }
void Check(){
      int pinValue = digitalRead(13);
      Serial.println(pinValue);
}

      
void loop() {

  // put your main code here, to run repeatedly

  if (Serial.available()) {
    value = Serial.readStringUntil(' ');
//    value2 = Serial.readStringUntil(',');
    command = Serial.readStringUntil('\n');
    val = value.toFloat();
//    val2 = value2.toInt();
    vals = val * 1000;
//    val2 = val * 1000;

    if (command.equals("p")) {
      PowerOn();
    }
    else if (command.equals("o")) {
      PowerOff();
    }
    else if (command.equals("zi")) {
      ZoomIn();
    }
    else if (command.equals("zo")) {
      ZoomOut();
    }
    else if (command.equals("r")) {
      Record();
    }
    else if (command.equals("s")) {
      Stop();
    }
    
    else if (command.equals("c")) {
      Capture();
    }
    
    else if (command.equals("rc")) {
      Record();
//      Serial.println(val/val2);
      i = 0;
      while(i < 6){
        delay(6000/vals);
        Capture();
        i = i + 1;
      }
      Stop();
    }
    else if (command.equals("home")) {
      delay(2000);
      Ex();
      delay(2000);
      Ex();
      delay(2000);
      Ex();
      delay(2000);
      Move();
      delay(1000);
      Ex();
      delay(2000);
      Move();
      Ex();
      
    }
    else if (command.equals("format")) {
      delay(2000);
      Menu();
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); //In Settings
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); // In Format
      delay(1000);
      Move();
      delay(1000);
      Ex();
      delay(1000);
      Move();
      delay(1000);
      Ex();
      
    }
    
    else if (command.equals("ft")) {
      delay(2000);
      Ex();
      delay(2000);
      Ex();
      delay(2000);
      Ex();
      delay(2000);
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); //In Settings
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); // In Format
      delay(1000);
      Move();
      delay(1000);
      Ex();
      delay(1000);
      Move();
      delay(1000);
      Ex();
    }

    else if (command.equals("ton")) {
      TransferOn();
    }

    else if (command.equals("toff")) {
      TransferOff();
    }

    else if (command.equals("m")) {
      Menu();
    }
    else if (command.equals("e")) {
      Ex();
    }
    else if (command.equals("con")) {
      Control();
    }
    else if (command.equals("check")){
      Check();
    }
    else if (command.equals("mp")){
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex();
      while(i < val){
        delay(1000);
        Ex();
        delay(1000);
        i = i + 1;
      }
    }
    else if (command.equals("mn")){
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex();
      while(i < val){
        delay(1000);
        Ex();
        delay(1000);
        i = i + 1;
      }
    }
      else if (command.equals("steady")) {
      delay(2000);
      Menu();
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); //In Cam Settings
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); 
      delay(1000);
      Ex();
      delay(1000);
      Ex();
      delay(1000);
      Ex();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex();
      delay(1000);
      Move();
      delay(1000);
      Ex();
    }
     else if (command.equals("manex")) {
      delay(2000);
      Menu();
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); //In Cam Settings
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); 
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex();
      
    }
    
    else if (command.equals("autoex")) {
      delay(2000);
      Menu();
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); //In Cam Settings
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex(); 
      delay(2000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Move();
      delay(1000);
      Ex();
      delay(1000);
      Move();
      delay(1000);
      Ex();
      
    }
    
}
}

      
