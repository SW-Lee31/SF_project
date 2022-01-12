import socket
import threading
import sys
import time
import SubB as Sub
import PubB as Pub
# from SubB import rcv_msg
import Vision as Vi
import Ctrl as Rc
from multiprocessing import Process


PB_value = 'null'


# Publisher객체 생성 및 브로커 연결
publisher = Pub.connect_mqtt()

# Subscriber객체 생성 및 브로커 연결
sub = Sub.connect_mqtt()
# Subscribe의 구독
Sub.subscribe(sub)

'''
def Adata_read():
    global PAData
    read_dataA = threading.Timer(1, Adata_read)
    print(Sub.return_data())
    read_dataA.start()
'''
def read_fromPA():
    sub_act = threading.Timer(.3, read_fromPA)

    ### !!!!python에서는 loop 내 global 변수를 holding 하는 문제 발생
    ### MQTT 내 loop시작, 끝 지정 loop에서 global 갱신
    ### loop를 끝내고 난 후 갱신된 global 변수 call
    sub.loop_start()
    Sub.run(sub)
    sub.loop_stop()
    global PAData
    PAData = parse_Adata(Sub.return_data())
    print(PAData)
    # print(Sub.return_data())

    sub_act.start()

def parse_Adata(data):
    PAdata = data.split(sep='/')
    return PAdata

def read_Vision():
    update_val = threading.Timer(.5, read_Vision)
    
    ### Vision B 코드 입력
    print(Vi.processCam())
    ### Vision B 값을 토대로 연산 
    
    ### PubB를 통해 완성 직후 A로 송신
    Pub.run(publisher, 'null')
    time.sleep(2)
    Pub.run(publisher, 'red')
    time.sleep(2)
    Pub.run(publisher, 'blue')
    time.sleep(2)

    update_val.start()

if __name__ == '__main__':
    try:
        ReadA_P = Process(target=read_fromPA)
        Vision_P = Process(target=read_Vision)
        ReadA_P.start()
        Vision_P.start()
        # Pub.run()
    except KeyboardInterrupt:
        print('키보드 인터럽트 발생')
        print('서버 강제 종료')
        sys.exit()