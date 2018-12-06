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
    
    speed = kp * error
    
    if(speed > 1000):
      speed = 1000
    elif(speed < -1000):
      speed = -1000

    leftMotor.run_forever(speed_sp = speed)
    rightMotor.run_forever(speed_sp = speed)

  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')


def pd_control(kp,kd):
  prevEr = 0
  while not btn.any():
    distance = us.value()/10
    curEr = distance - DESIRED
    
    chEr = curEr - prevEr
    speed = (kp * curEr) + (kd * chEr)
    prevEr = curEr
    
    if(speed > 1000):
      speed = 1000
    elif(speed < -1000):
      speed = -1000

    leftMotor.run_forever(speed_sp = speed)
    rightMotor.run_forever(speed_sp = speed)
 
  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')

def pid_control(kp, kd, ki):
  erSum = 0
  prevEr = 0
  while not btn.any():
    distance = us.value()/10
    error = distance - DESIRED
    chEr = error - prevEr
    erSum = erSum + error
    prevEr = error

    integral = ki * erSum
    
    if(integral > 50):
      integral = 50
    if(integral < -50):
      integral = -50
  
    
    speed = (kp * error) + (kd * chEr) + integral
    
    if(speed > 1000):
      speed = 1000
    elif (speed < -1000):
      speed = -1000

    leftMotor.run_forever(speed_sp = speed)
    rightMotor.run_forever(speed_sp = speed)

  rightMotor.stop(stop_action = 'coast')
  leftMotor.stop(stop_action = 'coast')

