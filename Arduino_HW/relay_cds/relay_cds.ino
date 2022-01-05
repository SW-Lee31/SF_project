int cds = A0;
int relay = D1;

bool stop_flag = false;

void setup() {
  pinMode(relay, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int light = analogRead(cds);
  Serial.println(light);
  
  if (light > 150){
    if(stop_flag == false){
      delay(500);
      digitalWrite(relay, LOW);
      stop_flag = true;
    }
    if(stop_flag == true){
      digitalWrite(relay, LOW);
    }
    
  }
  else{
    stop_flag = false;
    digitalWrite(relay, HIGH);
  }  
}
