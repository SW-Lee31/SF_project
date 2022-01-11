import socket
import threading
import sys
import time
import PubA as Pub
import SubA_flag as Sub
import Vision as Vi
import Ctrl as Rc
from multiprocessing import Process

# 제품 A에 대한 저장 리스트 초기화
PAData = [1, 0, 0, 0]
# PB에서 받은 데이터 저장 global 변수 초기화
PBData = 'null'
# Vision - blue를 2번 씩 읽음(예외처리 -> 내부 cnt{2})
cnt = [0, 0, 0, 0]

# Publisher객체 생성 및 브로커 연결
publisher = Pub.connect_mqtt()

# Subscriber객체 생성 및 브로커 연결
sub = Sub.connect_mqtt()
# Subscribe의 구독
Sub.subscribe(sub)

# 동작 플래그
Flag = False
Flagtemp = False

def read_Vision():
    global PAData
    global cnt
    vision_data = threading.Timer(1, read_Vision)

    if Vi.processCam() == 'red':
        cnt[0] += 1
        print(cnt)
        if cnt[0] >= 1:
            print('call red')
            PAData[0] += 1
            Robot_P = Process(target=Rc.work_red)
            Robot_P.start()
            Robot_P.join()
            cnt[0] = 0
        print(cnt)
    elif Vi.processCam() == 'blue':
        # blue 예외처리 (두개 씩 잡힘)
        cnt[1] += 0.5
        print(cnt)
        if cnt[1] >= 1:
            print('call blue')
            PAData[1] += 1
            Robot_P = Process(target=Rc.work_blue)
            Robot_P.start()
            Robot_P.join()
            cnt[1] = 0
        print(cnt)
    elif Vi.processCam() == 'green':
        cnt[2] += 1
        print(cnt)
        if cnt[2] >= 1:
            print('call green')
            PAData[2] += 1
            Robot_P = Process(target=Rc.work_green)
            Robot_P.start()
            Robot_P.join()
            cnt[2] = 0
        print(cnt)
    elif Vi.processCam() == 'yellow':
        cnt[3] += 1
        print(cnt)
        if cnt[3] >= 1:
            print('call yellow')
            PAData[3] += 1
            Robot_P = Process(target=Rc.work_yellow)
            Robot_P.start()
            Robot_P.join()
            cnt[3] = 0
        print(cnt)

    Pub.run(publisher, PAData)
    vision_data.start()

def read_flag():
    sub_act = threading.Timer(.3, read_flag)

    global Flag
    ### !!!!python에서는 loop 내 global 변수를 holding 하는 문제 발생
    ### MQTT 내 loop시작, 끝 지정 loop에서 global 갱신
    ### loop를 끝내고 난 후 갱신된 global 변수 call
    sub.loop_start()
    Sub.run(sub)
    sub.loop_stop()

    #if Sub.return_data() == '1':
        #Vision_P = Process(target=read_Vision)
        #Vision_P.start()
    # print('debug', Sub.return_data())


    sub_act.start()

if __name__ == '__main__':
    try:
        Vision_P = Process(target=read_Vision)
        Vision_P.start()
        ReadB_P = Process(target=read_flag)
        ReadB_P.start()
        # Pub.run()
    except KeyboardInterrupt:
        print('키보드 인터럽트 발생')
        sock.close()
        print('서버 강제 종료')
        sys.exit()