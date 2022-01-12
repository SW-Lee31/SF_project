#include <WiFiEsp.h>
#include <SoftwareSerial.h>

// Wifi 세팅
SoftwareSerial Serial1(7, 8);
IPAddress serverIP(192,168,0,32);
WiFiEspClient client;

char ssid[] = "iptime";
char pass[] = "asdf1234";
int status = WL_IDLE_STATUS;


void setup(void)
{
    Serial.begin(9600);
    Serial1.begin(9600);
    
    WiFi.init(&Serial1);
    Serial1.setTimeout(20);
    
      // 접속 시도
      while (status != WL_CONNECTED){
        Serial.print("Attempting to connect to WPA SSID: ");
        Serial.print(ssid);
        status = WiFi.begin(ssid, pass);
      }
    
      Serial.println("You're connected to the network");
      client.connect(serverIP,8787);
}
 
void loop(void)
{
    // 서버에서 데이터 송수신
    if (client.available()){
      String rcvmsg = client.readString();

      // 서버송신
      client.println(Serial.readStringUntil('\n'));
      // 서버수신
      if (rcvmsg){
      Serial.print("recv message : ");
      Serial.println(rcvmsg);
      }
    }
}
        
