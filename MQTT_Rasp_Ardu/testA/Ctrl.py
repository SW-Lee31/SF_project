# %%
#!/usr/bin/env python3
#coding=utf-8
import time
import asyncio
from Arm_Lib import Arm_Device

Arm = Arm_Device()
time.sleep(.1)

'''
def ctrl_all_servo(angle, s_time = 500):
    Arm.Arm_serial_servo_write6(angle, 180-angle, angle, angle, angle, angle, s_time)
    time.sleep(s_time/1000)
'''
async def work_red():
    await asyncio.sleep(4)
    Arm.Arm_serial_servo_write6(180, 40, 180, 170, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 75, 175, 162, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 75, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    # red
    Arm.Arm_serial_servo_write6(127, 60, 175, 162, 90, 145, 1000)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(127, 100, 175, 145, 115, 145, 1000)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(127, 100, 175, 145, 115, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(127, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 40, 180, 170, 90, 110, 500)

async def work_blue():
    await asyncio.sleep(4)
    Arm.Arm_serial_servo_write6(180, 40, 180, 170, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 75, 175, 162, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 75, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    # blue 위치 각도
    Arm.Arm_serial_servo_write6(85, 60, 175, 162, 90, 145, 1000)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(85, 95, 175, 162, 90, 145, 1000)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(85, 95, 175, 162, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(125, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 40, 180, 170, 90, 110, 500)

async def work_green():
    await asyncio.sleep(4)
    Arm.Arm_serial_servo_write6(180, 40, 180, 170, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 75, 175, 162, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 75, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    # green
    Arm.Arm_serial_servo_write6(110, 60, 175, 162, 90, 145, 1000)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(110, 90, 175, 162, 100, 145, 1000)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(110, 90, 175, 162, 100, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(125, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 40, 180, 170, 90, 110, 500)

async def work_yellow():
    await asyncio.sleep(4)
    Arm.Arm_serial_servo_write6(180, 40, 180, 170, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 75, 175, 162, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 75, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    # yellow
    Arm.Arm_serial_servo_write6(0, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(0, 60, 175, 162, 90, 110, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(125, 60, 175, 162, 90, 145, 500)
    await asyncio.sleep(1)
    Arm.Arm_serial_servo_write6(180, 40, 180, 170, 90, 110, 500)

