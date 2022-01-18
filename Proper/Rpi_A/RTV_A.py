import asyncio
import threading
import PubA as Pub
import Ctrl as Rc
import Vision as Vi
import SubA_flag as Flag
import Tcpip as Ti

# Mqtt Publiser object created
publiser = Pub.connect_mqtt()

vision_value = []

def vision_flag():
    global Flag
    if Flag:
        Pub.

def read_vision():
    global Flag
    while Flag == True:
        vision_value.append(await Vi.processCam())

    # need to change amount of count
        if vision_value.count('red') >= 1:
            asyncio.run(Rc_work('red'))
        elif vision_value.count('blue') >= 1:
            asyncio.run(Rc_work('blue'))
        elif vision_value.count('green') >= 1:
            asyncio.run(Rc_work('green'))
        elif vision_value.count('yellow') >= 1:
            asyncio.run(Rc_work('yellow'))

async def Rc_work(color_value):
    if color_value == 'red':
        # send robot_flag(activated/deactivated)
        Pub.ro_run(publiser, True)
        # robot action (color_value depends)
        await Rc.work_red()
        Pub.ro_run(publiser, False)
    if color_value == 'blue':
        Pub.ro_run(publiser, True)
        await Rc.work_blue()
        Pub.ro_run(publiser, False)
    if color_value == 'green':
        Pub.ro_run(publiser, True)
        await Rc.work_green()
        Pub.ro_run(publiser, False)
    if color_value == 'yellow':
        Pub.ro_run(publiser, True)
        await Rc.work_yellow()
        Pub.ro_run(publiser, False)


if __name__ == '__main__':
    try:

    except:
