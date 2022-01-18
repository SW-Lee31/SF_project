import threading
import sys
import time
import paho.mqtt.client as mqtt_client


BORKER_ADDR = '192.168.0.32'
PORT_RPI = 1883

# 장치 정보(conveyorAB)
TOPIC_CON_A = 'FromA/conA/conn'
TOPIC_CON_B = 'FromA/conB/conn'

# 장치 정보(Robot)
TOPIC_ROB = 'FromA/rob/conn'

# 장치 정보(vision)
TOPIC_VI_R = 'FromA/vi/r'
TOPIC_VI_G = 'FromA/vi/g'
TOPIC_VI_B = 'FromA/vi/b'
TOPIC_VI_Y = 'FromA/vi/y'

# increase vision value
vi_red_cnt = 0
vi_blue_cnt = 0
vi_green_cnt = 0
vi_yellow_cnt = 0

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


# conveyorA 정보 송신 (아두이노 TCP/IP 통신으로 데이터 조회 이후)
def connA_pub(client, msg):
    result = client.publish(TOPIC_CON_A, msg)
    status = result[0]

    if status == 0:
        pass
        #if msg != '':
            #print('conn Publish success!')
    else:
        print(f"failed to send conn message")

# conveyorB 정보 송신 (아두이노 TCP/IP 통신으로 데이터 조회 이후)
def connB_pub(client, msg):
    result = client.publish(TOPIC_CON_B, msg)
    status = result[0]

    if status == 0:
        pass
        #if msg != '':
            #print('conn Publish success!')
    else:
        print(f"failed to send conn message")

# vision 데이터 송신 (값 증가 -> 아날로그)
def vi_pub(client, msg):
    if msg == 'vred':
        global vi_red_cnt
        vi_red_cnt += 1
        result = client.publish(TOPIC_VI_R, vi_red_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                #print('vi Publish success!')
                pass
        else:
            print("failed to send vi message")
    elif msg == 'vblue':
        global vi_blue_cnt
        vi_blue_cnt += 1
        result = client.publish(TOPIC_VI_B, vi_blue_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                #print('vi Publish success!')
                pass
        else:
            print("failed to send vi message")
    elif msg == 'vgreen':
        global vi_green_cnt
        vi_green_cnt += 1
        result = client.publish(TOPIC_VI_G, vi_green_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                #print('vi Publish success!')
                pass
        else:
            print("failed to send vi message")
    elif msg == 'vdetected':
        global vi_yellow_cnt
        vi_yellow_cnt += 1
        result = client.publish(TOPIC_VI_Y, vi_yellow_cnt)
        status = result[0]

        if status == 0:
            if msg != '':
                #print('vi Publish success!')
                pass
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

def run(client, PAData, PATotal):
    # pub = connect_mqtt()
    # pub.loop_start()

    ### MQTT 클라이언트는 str, int 등의 데이터타입만 송신 가능(배열 X) -> 문자열 치환작업
    cntData = '/'.join(str(_) for _ in PAData)

    # print('Pub val', cntData)
    publish(client, cntData, PATotal[0], PATotal[1], PATotal[2], PATotal[3])

def conA_run(client, msg):
    connA_pub(client, msg)

def conB_run(client, msg):
    connB_pub(client, msg)

def vi_run(client, msg):
    vi_pub(client, msg)

def ro_run(client, msg):
    ro_pub(client, msg)