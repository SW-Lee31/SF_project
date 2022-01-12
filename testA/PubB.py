import threading
import sys
import time
import paho.mqtt.client as mqtt_client


BORKER_ADDR = '192.168.0.32'
PORT_RPI = 1883
TOPIC = 'ToA/productA-'
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
def publish(client, rval, bval, gval, yval):
    # msg = f"messages : 안녕하세여 from Pub"
    # msg = rcv_msg
    result_rval = client.publish(TOPIC, rval)
    result_bval = client.publish(TOPIC, bval)
    result_gal = client.publish(TOPIC, gval)
    result_yval = client.publish(TOPIC, yval)
    status = result_rval[0]

    if status == 0:
        if msg != '':
            print(f"send '{msg}' to topic '{TOPIC}'")
    else:
        print(f"failed to send message")


def run(client, PAdata):
    # pub = connect_mqtt()
    # pub.loop_start()
    # cntData = '/'.join(str(_) for _ in msg)
    # print('Pub val', cntData)
    publish(client, PAdata[0], PAdata[1], PAdata[2], PAdata[3])