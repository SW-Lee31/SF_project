/*
    This sketch establishes a TCP connection to a "quote of the day" service.
    It sends a "hello" message, and then prints received data.
*/

#include <ESP8266WiFi.h>

#ifndef STASSID
#define STASSID "iptime"
#define STAPSK  "asdf1234"
#endif

const char* ssid     = STASSID;
const char* password = STAPSK;

const char* host = "192.168.0.135";
const uint16_t port = 8090;
String stopSign = "";

void setup() {
  Serial.begin(115200);

  // We start by connecting to a WiFi network

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  /* Explicitly set the ESP8266 to be a WiFi-client, otherwise, it by default,
     would try to act as both a client and an access-point and could cause
     network-issues with your other WiFi-devices on your WiFi-network. */
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  static bool wait = false;
  
  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  // TCP 연결시도
  WiFiClient client;
  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    delay(5000);
    return;
  }

  // 데이터 송신
  Serial.println("sending data to server");
  if (client.connected()) {
    while (true){
      client.print("hello from ESP8266 : ");
      delay(300);
    }
  }

  // 연결 및 데이터 송신 확인(Time Out)
  unsigned long timeout = millis();
  while (client.available() == 0) {
    if (millis() - timeout > 5000) {
      Serial.println(">>> Client Timeout !");
      client.stop();
      delay(60000);
      return;
    }
  }
/*
  // Read all the lines of the reply from server and print them to Serial
  Serial.println("receiving from remote server");
  // not testing 'client.connected()' since we do not need to send data here
  while (client.available()) {
    char ch = static_cast<char>(client.read());
    Serial.print(ch);
  }
*/
  if (wait) {
    delay(300000); // execute once every 5 minutes, don't flood remote service
  }
  wait = true;
  
  // 연결 종료 (작동 X)
  stopSign = Serial.readStringUntil('\n');
  if (stopSign == "fEnd"){
    Serial.println();
    Serial.println("closing connection");
    client.stop();
  }
}
