#include <SoftwareSerial.h>
#include <WiFiEsp.h>
#include <Servo.h>

//Wifi 설정 및 Wifi pin 설정
char ssid[] = "iptime";
char pass[] = "asdf1234";
int status = WL_IDLE_STATUS;
//SoftwareSerial myserial(7, 8);
IPAddress serverIP(192,168,0,44);
WiFiEspClient client;
char strBuf[255];

void setup(){
  Serial.begin(115200);
  Serial.setTimeout(20);
  while(status != WL_CONNECTED){
    Serial.print("Attempting to connect to WPA SSID:");
    Serial.print(ssid);
    status = WiFi.begin(ssid, pass);
  }
  Serial.println("You're connected to the network");
  client.connect(serverIP, 8090);
}

void loop(){
  while (client.available()){
    client.println("hello from arduino");
    Serial.println("send success");
    delay(2000);
  }
  while (client.available()){
    String msg = client.readString();
    Serial.println(msg);
  }
}
