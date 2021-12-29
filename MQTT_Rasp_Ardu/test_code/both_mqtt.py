import socket
import threading
import sys
import threading
import time
import paho.mqtt.client as mqtt_client

BORKER_ADDR = '192.168.0.135'
PORT_RPI = 1883
TOPIC = 'test/test1'
PUB_ID = 'py_pub'
HOST_AD = ''
PORT_AD = 8090

# 수신 메시지 저장공간
BUF_SIZE = 1024
rcv_msg = ''

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

"""
def acceptClient():
    while Ture:
        try:
            servSocket = socket(AF_INET, SOCK_STREAM)
            servSocket.bind((HOST_AD, PORT_AD))
            servSocket.listen(5)
            print("서버 대기 중..")

            conn, addr = servSocket.accept()
            print("connected successs! (AD_Client) : " + addr)
            thread_rcv_data = threading.Thread(target=rcv_data, args=conn)
        except Exception as e:
            print("accept 에러 : ", e)
            break

def rcv_data(client):
    while True:
        try:
            data = client.recv(BUF_SIZE)
            if not data:
                break
            # conn.sendall(data)
            rcv_msg = data
            #client.close()
        except Exception as e:
            print("rcv 에러 : ", e)
            break;
"""

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
    msg_cnt = 0

    while True:
        time.sleep(5)
        # msg = f"messages : 안녕하세여 from Pub{msg_cnt}"
        msg = rcv_msg
        result = client.publish(TOPIC, msg)
        status = result[0]

        if status == 0:
            print(f"send '{msg}' to topic '{TOPIC}'")
        else:
            print(f"failed to send message")

def run():
    pub = connect_mqtt()
    pub.loop_start()
    publish(pub)

if __name__ == '__main__':
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