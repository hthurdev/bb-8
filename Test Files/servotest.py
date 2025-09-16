import time
from adafruit_servokit import ServoKit #needed for controlling the servo driver
import board
import adafruit_bno055 #gyro

import adafruit_motor
from gpiozero import PWMOutputDevice
from gpiozero import OutputDevice

import math

### DC Motors and Driver Relay ###
DCmotor1 = PWMOutputDevice(13, initial_value=0.5, frequency=10000)
DCmotor2 = PWMOutputDevice(18, initial_value=0.5, frequency=10000)
motorDriverRelay = OutputDevice(17, active_high=False)
##################################

### gyro related lines ###
i2c = board.I2C()  
sensor = adafruit_bno055.BNO055_I2C(i2c)
last_val = 0xFFFF
##########################

### Servo Driver ###
kit = ServoKit(channels=8)  
swingServo = kit.servo[0]
####################

print("Waiting 2 secs")
time.sleep(2)
motorDriverRelay.on()

# Quick Servo Test on the swinging arm
#swingServo.angle=100
#time.sleep(2)





# Testing is contained in a Try except loop to turn off the DC motor driver 
# when the program is cancelled with ctrl+C. This prevents the motors
# from spinning uncontrollably when the program is cancelled without ctrl+C

# 0 is full reverse
# 1 is full forward
# 0.5 is neutral
while True:
	try:
		time.sleep(2)
		print("reverse motors")
		DCmotor1.value = 0.6
		DCmotor2.value = 0.6
											
		time.sleep(2)
		
		DCmotor1.value = 0.5
		DCmotor2.value = 0.5
		
		time.sleep(2)
		
		DCmotor1.value = 0.4
		DCmotor2.value = 0.4
		
		time.sleep(2)
		
		DCmotor1.value = 0.5
		DCmotor2.value = 0.5
		
	except KeyboardInterrupt:
		
		#this sets the speed of the motors to 0 and turns off the relay.
		
		DCmotor2.value = 0.5
		DCmotor1.value = 0.5
		motorDriverRelay.off()
		print("Exiting")
		time.sleep(2)
		exit()


