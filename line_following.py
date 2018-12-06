#!/usr/bin/env python3

import ev3dev.ev3 as ev3

lcd = ev3.Screen()                   # The EV3 display
rightMotor = ev3.LargeMotor('outA')  # The motor connected to the right wheel
leftMotor = ev3.LargeMotor('outD')   # The motor connected to the left wheel
button = ev3.Button()				 # Any button
cs = ev3.ColorSensor()				 # The color sensor
assert cs.connected, "Connect a color sensor to any sensor port"

# A basic test to follow the left edge of a line
def followLineTillButtonPress(threshold):
	cs.mode = 'COL-REFLECT'
    
	# Follow the left edge of the line until a button is pressed
	while (not button.any()):
	
		if (cs.value() < threshold): # sees dark line, must turn left
			leftMotor.run_forever(speed_sp=400)
			rightMotor.run_forever(speed_sp=0)
    	
		else:                 # sees light surface, must turn right
			leftMotor.run_forever(speed_sp=0)
			rightMotor.run_forever(speed_sp=400)
       
    # stop moving   
	leftMotor.stop(stop_action='coast')
	rightMotor.stop(stop_action='coast')
	
	
followLineTillButtonPress(40)

  