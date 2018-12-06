#!/usr/bin/env python3
from ev3dev.ev3 import *

leftMotor = LargeMotor('outB')
rightMotor = LargeMotor('outC')

btn = Button()
us = UltrasonicSensor()
assert us.connected, " Error while connecting Ultrasonic Sensor"
us.mode='US-DIST-CM'

camera = Sensor(address=INPUT_1)	 # The camera
assert camera.connected, "Error while connecting Pixy camera to Input1"
camera.mode = 'SIG2'
DESIRED = 15

from threading import Thread

CAMERA_WIDTH_PIXELS = 255
CAMERA_HEIGHT_PIXELS = 255


global approach
global wander
global avoid

approach = False
wander = False
avoid = False

def look_for_object():
  global wander
  global approach
  while not btn.any():
    if(camera.value(0)== 0):
      leftMotor.run_forever(speed_sp = 450)
      rightMotor.run_forever(speed_sp = -450)
    else:
      leftMotor.stop(stop_action = 'hold')
      rightMotor.stop(stop_action = 'hold')
        
  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')
    
look_for_object()

def approach_object():
  global approach
  global wander
  while not btn.any():
    if(camera.value(0) != 0):
      distance = us.value()/10
      error = distance - DESIRED
      
      speed = 40 * error
      
      if(speed > 1000):
        speed = 1000
      elif(speed < -1000):
        speed = -1000
      
      leftMotor.run_forever(speed_sp = speed)
      rightMotor.run_forever(speed_sp = speed)
      
      if(distance == DESIRED):
        Sound.tone(1000, 200).wait()
      
    else:
      leftMotor.stop(stop_action = 'hold')
      rightMotor.stop(stop_action = 'hold')

  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')

approach_object()
  
def avoid_obstacles():
  #global avoid
  while not btn.any():
    if(camera.value(0) == 0):
      distance = (us.value()/10)
      if(distance <= 50):
        leftMotor.run_forever(speed_sp = 450)
        rightMotor.run_forever(speed_sp = 0)
    else:
      leftMotor.stop()
      rightMotor.stop()
        
  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')
    
avoid_obstacles()

t1 = Thread(target = look_for_object)
t1.start()
t2 = Thread(target = approach_object)
t2.start()
#t3 = Thread(target = avoid_obstacles)
#t3.start()


def main():
  global approach
  global wander
  #global avoid
  while not btn.any():
    #avoid = True
    if (camera.value(0) == 0):
      approach = False
      #avoid = False
      wander = True
    else:
      wander = False
      #avoid = False
      approach = True
      
  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')
  
main()
