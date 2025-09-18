import time
from adafruit_servokit import ServoKit #needed for controlling the servo driver
import adafruit_bno055 #gyro

import adafruit_motor
from gpiozero import PWMOutputDevice
from gpiozero import OutputDevice

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import busio, board

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50  # 50Hz for servos

import math

### DC Motors and Driver Relay ###
DCmotor1 = PWMOutputDevice(13, initial_value=0.5, frequency=10000)
DCmotor2 = PWMOutputDevice(18, initial_value=0.5, frequency=10000)
motorDriverRelay = OutputDevice(17, active_high=False)
##################################

### gyro related lines ###
sensor = adafruit_bno055.BNO055_I2C(i2c)
last_val = 0xFFFF
##########################

### Servo Driver ###

swingServo = servo.Servo(pca.channels[0]) #Middle position 100
headSidetoSide = servo.Servo(pca.channels[1])
headFB = servo.Servo(pca.channels[2])
headRotate = servo.Servo(pca.channels[3])
swingServo2 = servo.Servo(pca.channels[4]) #Middle position 90
####################

servo_floppy = [False] * 16  # up to 16 channels

def set_servo_floppy(channel, floppy=True):
    """Enable or disable floppy mode for a servo channel."""
    global servo_floppy
    if floppy:
        pca.channels[channel].duty_cycle = 0  # stop sending PWM
        servo_floppy[channel] = True
    else:
        # Re-enable by creating a Servo object again
        # (or just keep your old one around)
        servo_floppy[channel] = False

def set_servo_angle(channel, angle):
    """Safely move servo unless it's in floppy mode."""
    if not servo_floppy[channel]:
        s = servo.Servo(pca.channels[channel])
        s.angle = angle
    else:
        print(f"Channel {channel} is in floppy mode; ignoring command.")



print("TO CANCEL, USE CTRL+C, DONT CLOSE THE TAB")
print("Waiting 2 secs")
time.sleep(2)
motorDriverRelay.on()

def easyTurn(servo, angle, timeperdegree):
	#This function allows to fine tune the turn rate of a servo
	if angle>int(servo.angle):
		for angle in range(int(servo.angle),angle,1):
			servo.angle=angle
			time.sleep(timeperdegree)
	else:
		for angle in range(int(servo.angle),angle,-1):
			servo.angle=angle
			time.sleep(timeperdegree)
			
def setSwing(degrees): #rolling straight is 90
	#max 115 
	#min 70
	if 115>=degrees>=70:
		difference=degrees-90
		swingServo.angle = 90 + difference
		swingServo2.angle = 90 - difference
	else:
		print("swing out of range: max 115 minimum 70")
		


#swingServo2.angle=120
#print("Going 120")
#easyTurn(swingServo, 160, 0.02)
#time.sleep(2)
#easyTurn(swingServo, 70, 0.02)

#swingServo.angle = 130
#time.sleep(1)
#swingServo.angle = 100
#time.sleep(1)
#swingServo.angle = 

time.sleep(10)



# Testing is contained in a Try except loop to turn off the DC motor driver 
# when the program is cancelled with ctrl+C. This prevents the motors
# from spinning uncontrollably when the program is cancelled without ctrl+C

# 0 is full reverse
# 1 is full forward
# 0.5 is neutral
while True:
	try:
		if False:
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
		if True:
			# Quick Servo Test

			#set_servo_floppy(1)
			set_servo_floppy(2)
			set_servo_floppy(3)
			set_servo_floppy(4)

			setSwing(69)
			print("Going 90")
			time.sleep(10)
		
	except KeyboardInterrupt:
		
		#this sets the speed of the motors to 0 and turns off the relay.
		setSwing(90)
		DCmotor2.value = 0.5
		DCmotor1.value = 0.5
		
		motorDriverRelay.off()
		print("Exiting")
		time.sleep(2)
		exit()


