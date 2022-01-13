import threading
import sys
import time
import paho.mqtt.client as mqtt_client


BORKER_ADDR = '192.168.0.32'
PORT_RPI = 1883
PUB_ID = 'B_pub'

TOPIC = 'ToC/productB'
TOPIC_R = 'ToC/productB/R'
TOPIC_B = 'ToC/productB/B'
TOPIC_G = 'ToC/productB/G'


# 장치 정보(Robot)
TOPIC_ROB = 'FromB/rob/conn'

# 장치 정보(vision)
TOPIC_VI_T = 'FromB/vi/true'
TOPIC_VI_F = 'FromB/vi/false'

# increase vision value
vi_true_cnt = 1
vi_false_cnt = 1

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

def vi_pub(client, msg):
    if msg == 'vTrue':
        global vi_true_cnt
        result = client.publish(TOPIC_VI_T, vi_true_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                #print('vi Publish success!')
                vi_true_cnt += 1
        else:
            print("failed to send vi message")
    elif msg == 'vFalse':
        global vi_false_cnt
        result = client.publish(TOPIC_VI_F, vi_false_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                #print('vi Publish success!')
                vi_false_cnt += 1
        else:
            print("failed to send vi message")
    else:
        pass

def ro_pub(client, msg):
    result = client.publish(TOPIC_ROB, msg)
    status = result[0]

    if status == 0:
        pass
    else:
        print("failed to send ro message")

def run(client, msg):
    # pub = connect_mqtt()
    # pub.loop_start()
    cntData = '/'.join(str(_) for _ in msg)
    # print('Pub val', cntData)
    publish(client, cntData, msg[0], msg[1], msg[2])

def vi_run(client, msg):
    vi_pub(client, msg)

def ro_run(client, msg):
    ro_pub(client, msg)

