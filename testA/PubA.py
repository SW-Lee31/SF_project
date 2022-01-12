import threading
import sys
import time
import paho.mqtt.client as mqtt_client


BORKER_ADDR = '192.168.0.32'
PORT_RPI = 1883

# 장치 정보(conveyor)
TOPIC_CON = 'FromA/con/conn'
TOPIC_ROB = 'FromA/rob/conn'

# vision 정보
TOPIC_VI_R = 'FromA/vi/r'
TOPIC_VI_G = 'FromA/vi/g'
TOPIC_VI_B = 'FromA/vi/b'
TOPIC_VI_Y = 'FromA/vi/y'

# 로봇 시작 정보
TOPIC_ROB_R = 'FromA/rob/r'
TOPIC_ROB_B = 'FromA/rob/b'
TOPIC_ROB_G = 'FromA/rob/g'
TOPIC_ROB_Y = 'FromA/rob/y'

# increase vision value
vi_red_cnt = 1
vi_blue_cnt = 1
vi_green_cnt = 1
vi_yellow_cnt = 1

# increase robot value
ro_red_cnt = 1
ro_blue_cnt = 1
ro_green_cnt = 1
ro_yellow_cnt = 1

# A공정 이후 value 전달
TOPIC = 'ToB/productA'
TOPIC_R = 'ToB/productA/R'
TOPIC_B = 'ToB/productA/B'
TOPIC_G = 'ToB/productA/G'
TOPIC_Y = 'ToB/productA/Y'

# Publisher ID
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


# conveyor 정보 송신 (아두이노 TCP/IP 통신으로 데이터 조회 이후)
def conn_pub(client, msg):
    result = client.publish(TOPIC_CON, msg)
    status = result[0]

    if status == 0:
        if msg != '':
            print('conn Publish success!')
    else:
        print(f"failed to send conn message")

# vision 데이터 송신 (값 증가 -> 아날로그)
def vi_pub(client, msg):
    if msg == 'vred':
        global vi_red_cnt
        result = client.publish(TOPIC_VI_R, vi_red_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                print('vi Publish success!')
                vi_red_cnt += 1
        else:
            print("failed to send vi message")
    elif msg == 'vblue':
        global vi_blue_cnt
        result = client.publish(TOPIC_VI_B, vi_blue_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                print('vi Publish success!')
                vi_blue_cnt += 1
        else:
            print("failed to send vi message")
    elif msg == 'vgreen':
        global vi_green_cnt
        result = client.publish(TOPIC_VI_G, vi_green_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                print('vi Publish success!')
                vi_green_cnt += 1
        else:
            print("failed to send vi message")
    elif msg == 'vdetected':
        global vi_yellow_cnt
        result = client.publish(TOPIC_VI_Y, vi_yellow_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                print('vi Publish success!')
                vi_yellow_cnt += 1
        else:
            print("failed to send vi message")
    else:
        pass

def ro_pub(msg):
    if msg == 'rred':
        global ro_red_cnt
        result = client.publish(TOPIC_VI_R, ro_red_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                print('ro Publish success!')
                ro_red_cnt += 1
        else:
            print("failed to send ro message")
    elif msg == 'rblue':
        global ro_blue_cnt
        result = client.publish(TOPIC_VI_R, ro_blue_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                print('ro Publish success!')
                ro_blue_cnt += 1
        else:
            print("failed to send ro message")
    elif msg == 'rgreen':
        global ro_green_cnt
        result = client.publish(TOPIC_VI_R, ro_green_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                print('ro Publish success!')
                ro_green_cnt += 1
        else:
            print("failed to send ro message")
    elif msg == 'ryellow':
        global ro_yellow_cnt
        result = client.publish(TOPIC_VI_R, ro_yellow_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                print('ro Publish success!')
                ro_yellow_cnt += 1
        else:
            print("failed to send ro message")

def run(client, PAData, PATotal):
    # pub = connect_mqtt()
    # pub.loop_start()

    ### MQTT 클라이언트는 str, int 등의 데이터타입만 송신 가능(배열 X) -> 문자열 치환작업
    cntData = '/'.join(str(_) for _ in PAData)

    # print('Pub val', cntData)
    publish(client, cntData, PATotal[0], PATotal[1], PATotal[2], PATotal[3])

def con_run(client, msg):
    conn_pub(client, msg)

def vi_run(client, msg):
    vi_pub(client, msg)

def ro_run(client, msg):
    ro_pub(client, msg)