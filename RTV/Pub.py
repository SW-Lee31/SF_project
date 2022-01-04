import threading
import sys
import time
import paho.mqtt.client as mqtt_client

BORKER_ADDR = '192.168.0.32'
PORT_RPI = 1883
TOPIC = 'test/test1'
PUB_ID = 'py_pub'


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
def publish(client):
    while True:
        time.sleep(1)
        msg = f"messages : 안녕하세여 from Pub"
        # msg = rcv_msg
        result = client.publish(TOPIC, msg)
        status = result[0]

        if status == 0:
            if msg != '':
                print(f"send '{msg}' to topic '{TOPIC}'")
        else:
            print(f"failed to send message")


def run():
    pub = connect_mqtt()
    pub.loop_start()
    # cntData = '/'.join(str(_) for _ in msg)
    publish(pub)