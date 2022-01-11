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
    
    # red set
    '''
    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 90, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(53, 40, 180, 170, 90, 90, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(53, 75, 180, 125, 90, 90, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(53, 115, 170, 125, 80, 90, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(53, 115, 170, 125, 80, 145, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(53, 75, 180, 125, 90, 145, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(53, 75, 180, 125, 90, 90, 500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(0, 40, 180, 170, 90, 90, 500)
    time.sleep(1)
    '''
    
try :
    main()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass


# %%
del Arm  # Release the Arm object

# %%

