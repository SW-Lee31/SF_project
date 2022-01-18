import socket
import threading
import PubA as Pub

#TCP/IP 서버 생성
HOST_AD = ''
PORT_AD = 8585

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST_AD, PORT_AD))
sock.listen(5)

BUF_SIZE = 1024
rcv_msg = ''

def acceptClient(pub_client):
    connList = []
    while True:
        try:
            cli_sock, cli_addr = sock.accept()
            # print('클라이언트 접속: ', cli_sock)
            print("connected successs! (AD_Client) : ", cli_addr)
            connList.append(cli_sock)
            connList.append(pub_client)
            thread_client = threading.Thread(target=broadcastUser, args=[cli_sock, pub_client])
            thread_client.start()
        except Exception as x:
            print('accept 에러: ', x)
            break

def broadcastUser(cli_sock, pub_client):
    while 1:
        try:
            data = cli_sock.recv(BUF_SIZE)
            if data:
                #print(data)
                if data.decode() == 'Conv_A Act':
                    Pub.conA_run(pub_client, True)
                    #print('send1')
                elif data.decode() == 'Conv_A Dead':
                    Pub.conA_run(pub_client, False)
                    #print('send0')
                elif data.decode() == 'Conv_B Act':
                    Pub.conB_run(pub_client, False)
                elif data.decode() == 'Conv_B Dead':
                    Pub.conB_run(pub_client, False)
                #bUser(cli_sock, data)
        except Exception as x:
            print('recv 에러: ', x)
            break

'''
def bUser(cs_sock, msg):
    for client in connList:
        try:
            if (msg.decode() == 'fEnd'):
                print('fEnd: ', client)
                connList.remove(client)
                continue
            """if client != cs_sock:
                rcv_msg = msg
                client.send(msg)"""
        except Exception as x:
            print('send 에러: ', x)
            break
'''