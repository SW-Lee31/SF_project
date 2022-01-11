import socket
import threading
import sys
import time
import PubA as Pub
import SubA_flag as Sub
import Vision as Vi
import Ctrl as Rc
from multiprocessing import Process
import asyncio

# 제품 A에 대한 저장 리스트 초기화
PAData = [0, 0, 0, 0]

# PB에서 받은 데이터 저장 global 변수 초기화
PBData = 'null'
# Vision - Buffer
Vbuffer = []
# 예외처리 두번 이상 읽히는 경우
buff_cnt = 0

# Publisher객체 생성 및 브로커 연결
publisher = Pub.connect_mqtt()
#Pub.conn_run(publisher, 'Activated')

# Subscriber객체 생성 및 브로커 연결
sub = Sub.connect_mqtt()
# Subscribe의 구독
Sub.subscribe(sub)

# 동작 플래그
Flag = False
Flagtemp = False

def read_Vision():
    global PAData
    global Vbuffer
    global buff_cnt
    vision_data = threading.Timer(1, read_Vision)

    if Vi.processCam() == 'red':
        buff_cnt += 1
        if buff_cnt >= 1:
            Vbuffer.append('red')
            buff_cnt = 0
    elif Vi.processCam() == 'blue':
        buff_cnt += 0.5
        if buff_cnt >= 1:
            Vbuffer.append('blue')
            buff_cnt = 0
    elif Vi.processCam() == 'green':
        buff_cnt += 1
        if buff_cnt >= 1:
            Vbuffer.append('green')
            buff_cnt = 0
    elif Vi.processCam() == 'yellow':
        buff_cnt += 0.5
        if buff_cnt >= 1 or buff_cnt >= 0.5:
            Vbuffer.append('yellow')
            buff_cnt = 0

    if Vbuffer != []:
        if Vbuffer[0] == 'red':
            print(Vbuffer)
            asyncio.run(robot_action(Vbuffer[0]))
            PAData[0] += 1
            del Vbuffer[0]
            Pub.run(publisher, PAData)
            print(Vbuffer)
            # Rc_red_task = asyncio.create_task(robot_action(Vi.processCam()))
        elif Vbuffer[0] == 'blue':
            #print(Vbuffer)
            asyncio.run(robot_action(Vbuffer[0]))
            PAData[1] += 1
            del Vbuffer[0]
            Pub.run(publisher, PAData)
            #print(Vbuffer)
        elif Vbuffer[0] == 'green':
            #print(Vbuffer)
            asyncio.run(robot_action(Vbuffer[0]))
            PAData[2] += 1
            del Vbuffer[0]
            Pub.run(publisher, PAData)
            #print(Vbuffer)
        elif Vbuffer[0] == 'yellow':
            #print(Vbuffer)
            asyncio.run(robot_action(Vbuffer[0]))
            PAData[3] += 1
            del Vbuffer[0]
            Pub.run(publisher, PAData)
            #print(Vbuffer)
        else:
            pass


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

async def robot_action(color_value):
    if color_value == 'red':
        await Rc.work_red()
    elif color_value == 'blue':
        await Rc.work_blue()
    elif color_value == 'green':
        await Rc.work_green()
    elif color_value == 'yellow':
        await Rc.work_yellow()

if __name__ == '__main__':
    try:
        Vision_P = Process(target=read_Vision)
        Vision_P.start()
        ReadB_P = Process(target=read_flag)
        ReadB_P.start()
        #asyncio.run(Rt())
        # Pub.run()
    except KeyboardInterrupt:
        Pub.conn_run(publisher, 'Deactivated')
        Vision_P.join()
        ReadB_P.join()
        print('키보드 인터럽트 발생')
        sock.close()
        print('서버 강제 종료')
        sys.exit()