# %%
#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device

Arm = Arm_Device()
time.sleep(.1)

'''
def ctrl_all_servo(angle, s_time = 500):
    Arm.Arm_serial_servo_write6(angle, 180-angle, angle, angle, angle, angle, s_time)
    time.sleep(s_time/1000)
'''

def main():
    dir_state = 1
    angle = 90

    # 대기상태
    #Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 110, 2000)
    # 기본 세팅 각도
    '''
    # bus set
    Arm.Arm_serial_servo_write6(110, 40, 180, 170, 90, 145, 500)
    time.sleep(1)
    '''

    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 80, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(90, 108, 150, 162, 90, 80, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(90, 117, 150, 162, 90, 80, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(90, 117, 150, 162, 90, 145, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(90, 92, 150, 162, 90, 145, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(115, 92, 150, 162, 90, 145, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 145, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 80, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(118, 90, 150, 173, 113, 80, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(120, 115, 145, 170, 120, 80, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(120, 115, 145, 170, 120, 150, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(120, 106, 130, 173, 122, 150, 1000)
    time.sleep(2)
    Arm.Arm_serial_servo_write6(0, 106, 120, 173, 90, 150, 1000)
    time.sleep(2)
    Arm.Arm_serial_servo_write6(0, 105, 130, 180, 90, 150, 1000)
    time.sleep(2)
    Arm.Arm_serial_servo_write6(0, 105, 130, 180, 90, 80, 500)
    time.sleep(1)

try :
    main()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass


# %%
del Arm  # Release the Arm object

# %%
