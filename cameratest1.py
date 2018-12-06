#!/usr/bin/env python3

import ev3dev.ev3 as ev3
import time

lcd = ev3.Screen()                   # The EV3 display
rightMotor = ev3.LargeMotor('outA')  # The motor connected to the right wheel
leftMotor = ev3.LargeMotor('outD')   # The motor connected to the left wheel
button = ev3.Button()				 # Any button
camera = ev3.Sensor(address=ev3.INPUT_1)	 # The camera
assert camera.connected, "Error while connecting Pixy camera to port 2"

CAMERA_WIDTH_PIXELS = 255
CAMERA_HEIGHT_PIXELS = 255

def setCameraMode(sigNum):
	camera.mode = 'SIG'+str(sigNum)
	
def readCameraAndPrintInfo():
  objCount = camera.value(0)	# get the number of objects seen by the camera
	
  if (objCount > 0):     # if we've seen at least one object
    # get the position and dimensions of the largest object seen
    x = camera.value(1)	# x coordinate of middle of largest object
    y = camera.value(2)	# y coordinate of middle of largest object
    w = camera.value(3)	# width of largest object
    h = camera.value(4)	# height of largest object
        
    print("Found " + str(objCount) + " objects.")
    print("  Largest is at (" + str(x) + "," + str(y) + ")" +
  		    " with width " + str(w) + " pixels" +
    		  " and height " + str(h) + " pixels")
    if (x < CAMERA_WIDTH_PIXELS/2 - w/2):
   	  print("  Object is to my left.")
    elif (x > CAMERA_WIDTH_PIXELS/2 + w/2):
   	  print("  Object is to my right.")
    else:
      print("  Object is approximatley in front of me.")
      ev3.Sound.beep()	# demonstrating how to make a sound
  		
  else:
 	  print("No objects with the chosen signature.")
    	        

# Test the camera by searching for items 
def main():
  setCameraMode(1)
  while (not button.any()):
    readCameraAndPrintInfo()
    # Add a delay to reduce frequency of printing info to screen
    time.sleep(2)
    
  print("Done")
	
	
main()

