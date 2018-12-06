#!/usr/bin/env python3
import ev3dev.ev3 as ev3

rightMotor = ev3.LargeMotor('outC')  # The motor connected to the right wheel
leftMotor = ev3.LargeMotor('outB')   # The motor connected to the left wheel
button = ev3.Button()				 # Any button
camera = ev3.Sensor(address=ev3.INPUT_1)	 # The camera	
assert camera.connected, "Connect a color sensor to any sensor port"

CAMERA_WIDTH_PIXELS = 255
CAMERA_HEIGHT_PIXELS = 255

camera.mode = 'SIG1'

def follow_object(kp, kd): #P-control
  
  objCount = camera.value(0)
  prevEr = 0

  while(not button.any()):
    objCount = camera.value(0)      # get the number of objects seen by the camera
    
    if (objCount > 0):     # if we've seen at least one object
      # get the position and dimensions of the largest object seen 
      x = camera.value(1) # x coordinate of middle of largest object
      y = camera.value(2) # y coordinate of middle of largest object
      w = camera.value(3) # width of largest object
      h = camera.value(4) # height of largest object
    
      #speed = kp * (x/10) #where x is the error  ( from the origin - which is the center of the camera)
      
      chEr = x - prevEr
      speed = (kp * x) + (kd * chEr)
      prevEr = x

      if (speed > 1000):
        speed = 1000
      elif (speed < -1000):
        speed = -1000
 
      if (x < CAMERA_WIDTH_PIXELS/2 - w/2): #Object is to the left      
        rightMotor.run_forever( speed_sp = speed)
        leftMotor.run_forever(speed_sp = 0)
        
      elif (x > CAMERA_WIDTH_PIXELS/2 + w/2): #Object is to the right
        leftMotor.run_forever(speed_sp = speed)
        rightMotor.run_forever(speed_sp = 0)
        
      else:    
        leftMotor.run_forever(speed_sp = speed)
        rightMotor.run_forever(speed_sp = speed)
    
    else:
      print("No Object Has been identified")
      
  leftMotor.stop(stop_action = 'coast')
  rightMotor.stop(stop_action = 'coast')

follow_object(20, 20)  
