import socket
import threading
import sys
import time
import Pub
# import Sub
import Vision as Vi
import Ctrl as Rc
from multiprocessing import Process

PAData = [0, 0, 0, 0]
publisher = Pub.connect_mqtt()
cnt = 0

def Vision_read():
    global PAData
    global cnt
    vision_data = threading.Timer(.6, Vision_read)

    if Vi.processCam() == 'red':
        print('call red')
        Rc.ctrl_all_servo(70)
        PAData[0] += 1
    elif Vi.processCam() == 'blue':
        cnt += 1
        if cnt == 2:
            print('call blue')
            Rc.ctrl_all_servo(120)
            PAData[1] += 1
            cnt = 0
    elif Vi.processCam() == 'green':
        print('call green')
        Rc.ctrl_all_servo(50)
        PAData[2] += 1
    elif Vi.processCam() == 'yellow':
        print('call yellow')
        Rc.ctrl_all_servo(130)
        PAData[3] += 1
    else:
        Rc.ctrl_all_servo(90)

    Pub.run(publisher, PAData)
    vision_data.start()

if __name__ == '__main__':
    try:
        Vision_P = Process(target=Vision_read)
        Vision_P.start()
        # Pub.run()
    except KeyboardInterrupt:
        print('키보드 인터럽트 발생')
        sock.close()
        print('서버 강제 종료')
        sys.exit()