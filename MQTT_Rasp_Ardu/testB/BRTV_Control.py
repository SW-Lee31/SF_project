import asyncio
import socket
import threading
import sys
import time
import SubB as Sub
import PubB as Pub
from SubB import rcv_msg
import Vision as Vi
import Ctrl as Rc
from multiprocessing import Process
import ctrl_PWM_servo as Servo
import signal


#PAData = []

# Publisher객체 생성 및 브로커 연결
publisher = Pub.connect_mqtt()
Pub.conn_run(publisher, 'Activated')

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
    sub_act = threading.Timer(2, read_fromPA)

    ### !!!!python에서는 loop 내 global 변수를 holding 하는 문제 발생
    ### MQTT 내 loop시작, 끝 지정 loop에서 global 갱신
    ### loop를 끝내고 난 후 갱신된 global 변수 call
    sub.loop_start()
    Sub.run(sub)
    sub.loop_stop()
    global PAData
    PAData = parse_Adata(Sub.return_data())
    #print('temp received', rcv_msg)

    if PAData[0] != '':
        sendmsg = [0, 0, 0]
        red = PAData[0]
        blue = PAData[1]
        green = PAData[2]
        print(f'received {PAData[0]}, {PAData[1]}, {PAData[2]}')

        if int(red) >= 1:
            asyncio.run(robot_control('red'))
            PAData[0] = int(PAData[0]) - 1
            sendmsg[0] += 1
            Pub.run(publisher, sendmsg)
        elif int(blue) >= 1:
            asyncio.run(robot_control('blue'))
            PAData[1] = int(PAData[1]) - 1
            sendmsg[1] += 1
            Pub.run(publisher, sendmsg)
        elif int(green) >= 1:
            asyncio.run(robot_control('green'))
            PAData[2] = int(PAData[2]) - 1
            sendmsg[2] += 1
            Pub.run(publisher, sendmsg)

        print(f'updated {PAData[0]}, {PAData[1]}, {PAData[2]}')



    sub_act.start()


def parse_Adata(data):
    PAdata = data.split('/')
    return PAdata

async def robot_control(color_value):
    if color_value == 'red':
        await Rc.work_red()
    elif color_value == 'blue':
        await Rc.work_blue()
    elif color_value == 'green':
        await Rc.work_green()

def read_Vision():
    update_val = threading.Timer(.5, read_Vision)
    ### Vision B 코드 입력
    # 서보 동작
    # print(Vi.cheakArea())
    if Vi.cheakArea() == False:
        asyncio.run(Servo.servo_activate(0))
    else:
        asyncio.run(Servo.servo_activate(1))


    ### PubB를 통해 완성 직후 A로 송신

    update_val.start()

if __name__ == '__main__':
    try:
        ReadA_P = Process(target=read_fromPA)
        Vision_P = Process(target=read_Vision)
        ReadA_P.start()
        Vision_P.start()
        # Pub.run()
        signal.pause()
    except (KeyboardInterrupt, SystemExit):
        Pub.conn_run(publisher, 'Deactivated')
        print('키보드 인터럽트 발생')
        print('서버 강제 종료')
        Vi.end()
        sys.exit()