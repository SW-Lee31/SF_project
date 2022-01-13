import socket
import threading

#TCP/IP 서버 생성
HOST_AD = ''
PORT_AD = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST_AD, PORT_AD))
sock.listen(5)

BUF_SIZE = 1024
rcv_msg = ''

def acceptClient(msg):
    while True:
        try:
            cli_sock, cli_addr = sock.accept()
            # print('클라이언트 접속: ', cli_sock)
            print("connected successs! (AD_Client) : ", cli_addr)
            thread_client = threading.Thread(target=broadcastUser, args=[cli_sock, msg])
            thread_client.start()
        except Exception as x:
            print('accept 에러: ', x)
            break

def broadcastUser(cli_sock, msg):
    if msg == 1:
        try:
           cli_sock.send(bytes([msg]))
           print('send success!')
        except Exception as x:
            print('send 에러: ', x)
            pass
    else:
        pass

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