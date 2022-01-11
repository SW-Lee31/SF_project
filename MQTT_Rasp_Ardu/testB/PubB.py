import threading
import sys
import time
import paho.mqtt.client as mqtt_client


BORKER_ADDR = '192.168.0.32'
PORT_RPI = 1883
TOPIC_CON = 'ToC/conn'
TOPIC = 'ToC/productB'
TOPIC_R = 'ToC/productB/r'
TOPIC_B = 'ToC/productB/b'
TOPIC_G = 'ToC/productB/g'
PUB_ID = 'B_pub'

## MQTT Publisher
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("connected successs! (RPI_Broker)")
        else:
            print("failed connect, return code %d\n", rc)

    pub = mqtt_client.Client(PUB_ID)
    pub.on_connect = on_connect
    pub.connect(BORKER_ADDR, PORT_RPI)
    return pub


# Publish(send) 데이터 송신 함수(Call back)
def publish(client, msg, red, blue, green):
    # msg = f"messages : 안녕하세여 from Pub"
    # msg = rcv_msg
    result = client.publish(TOPIC, msg)
    result_r = client.publish(TOPIC_R, red)
    result_b = client.publish(TOPIC_B, blue)
    result_g = client.publish(TOPIC_G, green)
    status = result[0]
    status_r = result_r[0]
    status_b = result_b[0]
    status_g = result_g[0]

    if status == 0 and status_r == 0 and status_b == 0 and status_g == 0:
        if msg != '':
            print(f'send success {red}, {blue}, {green}')
    else:
        print(f"failed to send message")

def conn_pub(client, msg):
    result = client.publish(TOPIC_CON, msg)
    status = result[0]

    if status == 0:
        if msg != '':
            print('conn Publish success!')
    else:
        print(f"failed to send conn message")

def run(client, msg):
    # pub = connect_mqtt()
    # pub.loop_start()
    cntData = '/'.join(str(_) for _ in msg)
    # print('Pub val', cntData)
    publish(client, cntData, msg[0], msg[1], msg[2])

def conn_run(client, msg):
    conn_pub(client, msg)