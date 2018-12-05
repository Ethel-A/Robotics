#!/usr/bin/env python3

from ev3dev.ev3 import *
from movement.ev3movement.movement import *

cl = ColorSensor()
assert cl.connected, "Connect a single EV3 color sensor to any sensor port"
cl.mode = "COL-COLOR"

while cl.value() != 1:
    if cl.value() == 5:
        if turned_red == False:
            turned_red = True
            stop()
            turn_left_by_angle(90, 450)
            run_forever(450)
        else:
            run_forever(450)
    elif cl.value() == 3:
        if turned_green == False:
            turned_green = True
            stop()
            turn_right_by_angle(90, 450)
            run_forever(450)
        else: 
            run_forever(450)
    else:
        turned_green = False
        turned_red = False
        run_forever(450)
else:
    print('Done!!')
    stop()
    Sound.beep()       
    Leds.set_color(Leds.LEFT, Leds.GREEN)  #set left led green before exiting
