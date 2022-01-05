# %%
#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device

Arm = Arm_Device()
time.sleep(.1)


def ctrl_all_servo(angle, s_time = 500):
    Arm.Arm_serial_servo_write6(angle, 180-angle, angle, angle, angle, angle, s_time)
    time.sleep(s_time/1000)

def ctrl_servo(angle1, angle2, angle3, angle4, angle5, angle6, s_time = 700):
    Arm.Arm_serial_servo_write6(angle1, angle2, angle3, angle4, angle5, angle6, s_time)
    time.sleep(s_time/1000)

def action():
    dir_state = 1
    angle = 90
    

    Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 500)
    time.sleep(1)

    """
    while True:
        if dir_state == 1:
            angle += 1
            if angle >= 180:
                dir_state = 0
        else:
            angle -= 1
            if angle <= 0:
                dir_state = 1
        
        ctrl_all_servo(angle, 10)
        time.sleep(10/1000)
    """
#         print(angle)
'''
try :
    action()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass

# %%
del Arm  # Release the Arm object

# %%
'''