from time import sleep, time
import math
from threading import *


def limit_length(variable, desired_length, padding_char=' '):
    if len(variable) < desired_length:
        variable = variable + (padding_char * (desired_length - len(variable)))
    elif len(variable) > desired_length:
        variable = variable[:desired_length]

    return variable


def dist():
    global pos

    starttime = time()
    t = 0.2
    while True:
        temp = pos

        vx = temp["vx"]
        vy = temp["vy"]
        vr = temp["vr"]

        x = temp["x"]
        y = temp["y"]
        r = temp["r"]


        pos["x"] = x + vx * t
        pos["y"] = y + vy * t
        pos["r"] = r + vr * t

        sleep((t / 2) - ((time() - starttime) % (t / 2)))  # run every second


def main():
    global ep_chassis, ep_start, pos, delay

    pos = {"x": 0, "y": 0, "r": 0, "vx": 0, "vy": 0, "vr": 0}
    while True:
        sleep(delay)

        x = limit_length(str(pos["x"]), 8)
        y = limit_length(str(pos["y"]), 8)
        r = limit_length(str(pos["r"]), 8)
        vx = limit_length(str(pos["vx"]), 8)
        vy = limit_length(str(pos["vy"]), 8)
        vr = limit_length(str(pos["vr"]), 8)

        print("| x: " + x + " | y: " + y + " | r: " + r + " | vx: " + vx + " | vy: " + vy + " | vr: " + vr + " |")


def start(dela):
    global ep_chassis, ep_start, pos, delay

    if dela < 0.5:
        delay = 0.5
    else:
        delay = dela

    ep_chassis = "started"
    ep_start = 1

    t1 = Thread(target=main)
    t1.start()
    t2 = Thread(target=dist)
    t2.start()


def driveWheels(frWheel, flWheel, blWheel, brWheel):
    global pos

    min_limit = -200
    max_limit = 200

    fr = max(min(frWheel, max_limit), min_limit)
    fl = max(min(flWheel, max_limit), min_limit)
    bl = max(min(blWheel, max_limit), min_limit)
    br = max(min(brWheel, max_limit), min_limit)


    y = (fr + fl + bl + br) / 4
    x = (-fr + fl + bl - br) / 4
    rx = (-fr + fl - bl + br) / 4

    pos["vx"] = x
    pos["vy"] = y
    pos["vr"] = rx
