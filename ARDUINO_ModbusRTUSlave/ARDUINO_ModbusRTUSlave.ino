#include <ModbusRtu.h>

// data array for modbus network sharing
int modbus_table[16] = {
  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };


/**
 *  Modbus object declaration
 *  u8id : node id = 0 for master, = 1..247 for slave
 *  port : serial port
 *  u8txenpin : 0 for RS-232 and USB-FTDI 
 *               or any pin number > 1 for RS-485
 */
Modbus slave(1,Serial,0); // this is slave @1 and RS-485

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  
  Serial.begin( 19200 ); // baud-rate at 19200
  slave.start();
}

void loop() {
  //모드버스의 40001 주소
  bool data =  modbus_table[0];
  if(data == LOW)
    digitalWrite(LED_BUILTIN, LOW);
  else if(data == HIGH)
    digitalWrite(LED_BUILTIN, HIGH);

  slave.poll( modbus_table, 16 );
}
