int cds = A0;
int relay = D1;

void setup() {
  pinMode(relay, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int light = analogRead(cds);

  if (light < 100){
    digitalWrite(relay, LOW);
  }
  else{
    digitalWrite(relay, HIGH);
  }  
}
