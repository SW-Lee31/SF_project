import socket
import threading
import sys
import time
import Sub
from Sub import rcv_msg
# import Sub
# import Vision as Vi
import Ctrl as Rc
from multiprocessing import Process


PBData = [0, 0, 0, 0]
PAData = [0, 0, 0, 0]

sub = Sub.connect_mqtt()
Sub.subscribe(sub)

def Adata_read():
    global PAData
    read_dataA = threading.Timer(1, Adata_read)
    print(Sub.return_data())
    read_dataA.start()

def sub_activate():
    sub_act = threading.Timer(.3, sub_activate)

    ### !!!!python에서는 loop 내 global 변수를 holding 하는 문제 발생
    ### MQTT 내 loop시작, 끝 지정 loop에서 global 갱신
    ### loop를 끝내고 난 후 갱신된 global 변수 call
    sub.loop_start()
    Sub.run(sub)
    sub.loop_stop()
    print(Sub.return_data())
    sub_act.start()

if __name__ == '__main__':
    try:
        SubActP = Process(target=sub_activate)
        SubReadP = Process(target=Adata_read)
        SubActP.start()
        SubReadP.start()
        # Pub.run()

    except KeyboardInterrupt:
        print('키보드 인터럽트 발생')
        print('서버 강제 종료')
        sys.exit()