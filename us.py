#!/usr/bin/env python3
from ev3dev.ev3 import *
from movement.ev3movement.movement import *
import random

us = UltrasonicSensor() 
assert us.connected, "Connect a single US sensor to any sensor port"

us.mode='US-DIST-CM'
btn = ev3.Button()
units = us.units


while not btn.any():    # Stop program by pressing touch sensor button
    # US sensor will measure distance to the closest
    # object in front of it.
    #run_forever(450)

    distance = us.value()/10  # convert mm to cm
    print(str(distance) + " " + units)

    if distance <= 100:  #This is an inconveniently large distance
        Leds.set_color(Leds.LEFT, Leds.RED)
        value = random.choice([1, 2, 3])
        
        if value == 1:
            turn_right_by_angle(90, 450)
        elif value == 2:
            turn_left_by_angle(90, 450)
        else:
            spin_right_by_angle(90, 450)
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)
        run_forever(450)
        #Robot should do nothing
else:
    print('Done!!')
    stop()
    Sound.beep()       
    Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting
