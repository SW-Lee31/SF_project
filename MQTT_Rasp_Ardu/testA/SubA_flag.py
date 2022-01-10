import functools

import paho.mqtt.client as mqtt_client
from multiprocessing import Queue
import time
import asyncio

broker_addr = '192.168.0.32'
port = 1883
from_topic = 'Das/flag'
sub_id = f'A_sub'
rcv_msg = ''

# MQTT 연결 콜백함수
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('connected Successful')
        else:
            print('failed connect, return code %d\n', rc)

    sub = mqtt_client.Client(sub_id)
    sub.on_connect = on_connect
    sub.connect(broker_addr, port)
    return sub

### Plan-B 파일 쓰고 읽기(failed -> sync 문제{많이 느림})
def fwrite(rcv_msg):
    with open("Adata.txt", "w") as f:
        f.write(rcv_msg)

### Pub으로부터의 message 수신 부
def on_message(client, userdata, msg):
    # print(f"Received '{msg.payload.decode()}' from '{msg.topic}' topic")
    global rcv_msg
    # rcv_msg = f"Received '{msg.payload.decode()}' from '{msg.topic}' topic"
    print('scada_val : ', rcv_msg)
    rcv_msg = msg.payload.decode()
    # client.loop_stop()

### 전역변수 call  함수 -> on_message는 Call back함수(return 불가)
def return_data():
    return rcv_msg


# 구독 연결 콜백함수
def subscribe(client: mqtt_client):
    client.subscribe(from_topic)

def run(client):
    # client.loop_start()
    client.on_message = on_message
    # client.loop_stop()
    # Loop (내장 스레드)
    #sub.loop_forever()


