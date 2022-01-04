import socket
import threading
import sys
import time
import Pub
import Sub
import Vision as Vi
import Ctrl as Rc
from multiprocessing import Process

def Vision_read():
    vision_data = threading.Timer(.1, Vision_read)

    if Vi.processCam() == 'red':
        Rc.ctrl_all_servo(70)
    elif Vi.processCam() == 'blue':
        Rc.ctrl_all_servo(120)
    elif Vi.processCam() == 'green':
        Rc.ctrl_all_servo(50)
    elif Vi.processCam() == 'yellow':
        Rc.ctrl_all_servo(130)
    else:
        Rc.ctrl_all_servo(90)

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