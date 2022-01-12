# %%
#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device
import asyncio

Arm = Arm_Device()

time.sleep(.1)



#def ctrl_all_servo(angle):
    #Arm.Arm_PWM_servo_write(0, angle)

async def servo_activate(act_code):
    if(act_code == 1):
        Arm.Arm_PWM_servo_write(0, 110)
    else:
        await asyncio.sleep(.5)
        Arm.Arm_PWM_servo_write(0, 160)
        await asyncio.sleep(1)

# 110 ~ 160
'''
try :
    main()
except KeyboardInterrupt:
    print(" Program closed! ")
    pass


# %%
del Arm  # Release the Arm object

# %%
'''