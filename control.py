#!/usr/bin/env python3
from ev3dev.ev3 import *

leftMotor = LargeMotor('outB')
rightMotor = LargeMotor('outC')

us = UltrasonicSensor() 
assert us.connected, "Connect a single US sensor to any sensor port"

us.mode='US-DIST-CM'
btn = Button()
DESIRED = 15

def bangBang(kp):
  while not btn.any():
    distance = us.value()/10  # convert mm to cm
    error = distance - DESIRED
    if (error > 0):
      esign = 1
    else:
      esign = -1
    
    speed = kp * esign
    
    leftMotor.run_forever(speed_sp = speed)
    rightMotor.run_forever(speed_sp = speed)

  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')

def p_control(kp):
  while not btn.any():
    distance = us.value()/10
    error = distance - DESIRED
    
    if(error > 0): #When error is positive
      if(kp > (1000/error)):
        kp = 1000/error
    elif(error < 0): #When error is negative
      if(kp < (-1000/error)):
        kp = -1000/error
    
    speed = kp * error

    leftMotor.run_forever(speed_sp = speed)
    rightMotor.run_forever(speed_sp = speed)

  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')

p_control(40)


