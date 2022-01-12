int cdsA = A0;
int cdsB = A1;
int relayA = 7;
int relayB = 6;

bool stop_flagA = false;
bool stop_flagB = false;

void setup() {
  pinMode(relayA, OUTPUT);
  pinMode(relayB, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int lightA = analogRead(cdsA);
  int lightB = analogRead(cdsB);
  Serial.print('A');
  Serial.print(lightA);
  Serial.print('B');
  Serial.println(lightB);
  
  
  if (lightA > 150){
    if(stop_flagA == false){
      delay(300);
      digitalWrite(relayA, LOW);
      stop_flagA = true;
    }
    if(stop_flagA == true){
      digitalWrite(relayA, LOW);
    }
    
  }
  else{
    stop_flagA = false;
    digitalWrite(relayA, HIGH);
  }  

  if (lightB > 150){
    if(stop_flagB == false){
      delay(300);
      digitalWrite(relayB, LOW);
      stop_flagB = true;
    }
    if(stop_flagB == true){
      digitalWrite(relayB, LOW);
    }
    
  }
  else{
    stop_flagB = false;
    digitalWrite(relayB, HIGH);
  }  
}
