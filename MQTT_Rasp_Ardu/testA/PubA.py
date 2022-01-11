import threading
import sys
import time
import paho.mqtt.client as mqtt_client


BORKER_ADDR = '192.168.0.32'
PORT_RPI = 1883
TOPIC_CON = 'ToB/conn'
TOPIC = 'ToB/productA'
TOPIC_R = 'ToB/productA/R'
TOPIC_B = 'ToB/productA/B'
TOPIC_G = 'ToB/productA/G'
TOPIC_Y = 'ToB/productA/Y'
PUB_ID = 'A_pub'

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
def publish(client, msg, Rval, Bval, Gval, Yval):
    # msg = f"messages : 안녕하세여 from Pub"
    # msg = rcv_msg
    result_R = client.publish(TOPIC_R, Rval)
    result_B = client.publish(TOPIC_B, Bval)
    result_G = client.publish(TOPIC_G, Gval)
    result_Y = client.publish(TOPIC_Y, Yval)
    result = client.publish(TOPIC, msg)
    status_r = result_R[0]
    status_b = result_B[0]
    status_g = result_G[0]
    status_y = result_Y[0]
    status = result[0]

    if status == 0 and status_r == 0 and status_b == 0 \
            and status_g == 0 and status_y == 0:
        if Rval != '' and Bval != '' and Gval != '' and Yval != '':
            print(f"success send messege {Rval}, {Bval}, {Gval}, {Yval}")
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

def run(client, PAData):
    # pub = connect_mqtt()
    # pub.loop_start()

    ### MQTT 클라이언트는 str, int 등의 데이터타입만 송신 가능(배열 X) -> 문자열 치환작업
    cntData = '/'.join(str(_) for _ in PAData)

    # print('Pub val', cntData)
    publish(client, cntData, PAData[0], PAData[1], PAData[2], PAData[3])

def conn_run(client, msg):
    conn_pub(client, msg)