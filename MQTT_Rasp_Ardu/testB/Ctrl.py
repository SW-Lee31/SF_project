# %%
#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device
import asyncio

Arm = Arm_Device()
time.sleep(.1)

async def work_blue():
    await asyncio.sleep(4)
    Arm.Arm_serial_servo_write6(86, 108, 150, 162, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(86, 117, 150, 162, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(86, 117, 150, 162, 90, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(86, 92, 150, 162, 90, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(115, 92, 150, 162, 90, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(115, 92, 150, 162, 120, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150, 173, 113, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 102, 150 ,173, 113 ,90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 90, 150, 173, 113, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 125, 135, 173, 122, 84, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 125, 135, 173, 122, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 106, 111, 173, 122, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 106, 111, 173, 122, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 106, 111, 173, 90, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 177, 180, 90, 160, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 177, 180, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 150, 180, 90, 90, 500)
    await asyncio.sleep(1)

async def work_red():
    await asyncio.sleep(4)
    Arm.Arm_serial_servo_write6(90, 90, 150, 180, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(50, 90, 150, 150, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(52, 145, 93, 180, 70, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(54, 150, 93, 180, 50, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(54, 157, 90, 180, 75, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(54, 157, 90, 180, 75, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(53, 151, 93, 180, 70, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(53, 98, 145, 180, 70, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(122, 98, 145, 180, 70, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(113, 98, 145, 180, 134, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 110, 137 ,180, 111, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 110, 137 ,180, 111, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 90, 137 ,180, 111, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 128, 128, 180, 111, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 128, 128, 180, 111, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(118, 90, 128, 180, 134, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 90, 137, 174, 114, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 177, 180, 90, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 177, 180, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 150, 180, 90, 90, 500)
    await asyncio.sleep(1)

async def work_green():
    await asyncio.sleep(4)
    Arm.Arm_serial_servo_write6(90, 90, 150, 180, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(64, 90, 150, 150, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(68, 124, 119, 180, 67, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(68, 137, 113, 180, 67, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(68, 137, 113, 180, 67, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(68, 124, 119, 180, 67, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(68, 72, 163, 180, 67, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(127, 72, 163, 180, 67, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(127, 72, 163, 180, 136, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(113, 86, 147, 180, 112, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(119, 113, 137, 180, 112, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(119, 113, 137, 180, 112, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(119, 88, 137, 180, 112, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(119, 131, 127, 180, 112, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(119, 131, 127, 180, 112, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(119, 113, 151 ,170, 120, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(119, 74, 160 ,170, 120, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 74, 160 ,170, 120, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 177, 180, 90, 150, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 177, 180, 90, 90, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 53, 150, 180, 90, 90, 500)
    await asyncio.sleep(1)




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