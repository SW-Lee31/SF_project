#include <WiFiEsp.h>
#include <SoftwareSerial.h>

int cdsA = A0;
int cdsB = A1;
int relayA = 7;
int relayB = 6;
bool stop_flagA = false;
bool stop_flagB = false;

// Wifi 세팅
SoftwareSerial Serial1(5, 4);
IPAddress serverIP(192,168,0,32);
WiFiEspClient client;

char ssid[] = "iptime";
char pass[] = "asdf1234";
int status = WL_IDLE_STATUS;


void setup(void)
{
    Serial.begin(9600);
    Serial1.begin(9600);
    pinMode(relayA, OUTPUT);
    pinMode(relayB, OUTPUT);
  
    WiFi.init(&Serial1);
    Serial1.setTimeout(20);
    
      // 접속 시도
      while (status != WL_CONNECTED){
        Serial.print("Attempting to connect to WPA SSID: ");
        Serial.print(ssid);
        status = WiFi.begin(ssid, pass);
      }
    
      Serial.println("You're connected to the network");
      client.connect(serverIP, 8585);

      
      client.print("Conv_A Act");
      client.print("Conv_B Act");
      
}
 
void loop(void)
{
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
      client.write("Conv_A Dead");
    }
  }
  else{
    stop_flagA = false;
    digitalWrite(relayA, HIGH);
    client.write("Conv_A Act");
  }  

  if (lightB > 150){
    if(stop_flagB == false){
      delay(300);
      digitalWrite(relayB, LOW);
      stop_flagB = true;
    }
    if(stop_flagB == true){
      digitalWrite(relayB, LOW);
      client.write("Conv_B Dead");
    }
  }
  else{
    stop_flagB = false;
    digitalWrite(relayB, HIGH);
    client.write("Conv_B Act");
  }
}
        
