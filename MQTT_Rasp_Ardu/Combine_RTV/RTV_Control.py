import socket
import threading
import sys
import time
import paho.mqtt.client as mqtt_client
import Vision as Vi
import Ctrl as Rc
from multiprocessing import Process
import os

BORKER_ADDR = '192.168.0.32'
PORT_RPI = 1883
TOPIC = 'test/test1'
PUB_ID = 'py_pub'
HOST_AD = ''
PORT_AD = 8090

# Vision에서 작성한 파일 주소
bin_path = 'data.bin'
# Vision bin파일 인코딩
encoding_data = 'utf-8'
# Vision data
vision_data = ''

# TCP/IP 수신 메시지 저장공간
BUF_SIZE = 1024
rcv_msg = ''


def Vision_read():
    Vision_data = threading.Timer(0.3, Vision_read)

    if Vi.processCam() == 'red':
        Rc.
        
    
## TCP/IP Server
def acceptClient():
    while True:
        try:
            cli_sock, cli_addr = sock.accept()
            # print('클라이언트 접속: ', cli_sock)
            print("connected successs! (AD_Client) : ", cli_addr)
            connList.append(cli_sock)
            thread_client = threading.Thread(target=broadcastUser, args=[cli_sock])
            thread_client.start()
        except Exception as x:
            print('accept 에러: ', x)
            break

def broadcastUser(cli_sock):
    while True:
        try:
            data = cli_sock.recv(BUF_SIZE)
            if data:
                print('recv: ', data)
                global rcv_msg
                rcv_msg = data
                bUser(cli_sock, rcv_msg)
        except Exception as x:
            print('recv 에러: ', x)
            break

# TCP/IP  server 송신 함수 (송신은 X cs_sock 파라미터 사용X)
def bUser(cs_sock, msg):
    for client in connList:
        try:
            if (msg.decode() == 'fEnd'):
                print('fEnd: ', client);
                connList.remove(client)
                continue
            """if client != cs_sock:
                rcv_msg = msg
                client.send(msg)"""
        except Exception as x:
            print('send 에러: ', x)
            break

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
        time.sleep(5)
        msg = f"messages : 안녕하세여 from Pub"
        # msg = rcv_msg
        result = client.publish(TOPIC, msg)
        status = result[0]

        if status == 0:
            if rcv_msg != '':
                print(f"send '{msg}' to topic '{TOPIC}'")
        else:
            print(f"failed to send message")

def run():
    pub = connect_mqtt()
    pub.loop_start()
    publish(pub)

if __name__ == '__main__':
    Vision_P = Process(target=Vision_activate)
    Vision_P.start()
    
    try:
        connList = []  # 비어있는 리스트 생성 TCP/IP Client 담는 공간

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST_AD, PORT_AD))
        sock.listen(5)
        print('Server in waiting..(AD_CONN)')
        threadServ = threading.Thread(target=acceptClient)
        threadServ.start()
        
        
        

        run()
    except KeyboardInterrupt:
        print('키보드 인터럽트 발생')
        sock.close()
        print('서버 강제 종료')
        sys.exit()