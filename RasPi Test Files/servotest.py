import time
from adafruit_servokit import ServoKit #needed for controlling the servo driver
import adafruit_bno055 #gyro
import math

from gpiozero import PWMOutputDevice
from gpiozero import OutputDevice

import adafruit_motor
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import busio, board

i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50  # 50Hz for servos

### Testing Control Area ###
#enable ONLY ONE boolean for what you want to test
DCdrivemotorsTest=False
SwingServoTest=False
HeadServoTest=True
RestAllServos=False
############################

### DC Motors and Driver Relay Definitions ###
DCmotor1 = PWMOutputDevice(13, initial_value=0.5, frequency=10000)
DCmotor2 = PWMOutputDevice(18, initial_value=0.5, frequency=10000)
motorDriverRelay = OutputDevice(17, active_high=False)
##################################

### Gyro Definitions ###
sensor = adafruit_bno055.BNO055_I2C(i2c)
last_val = 0xFFFF
########################

### Servo Definitions ###
#!!USE setSwing!! instead of setting the angle of individual swingServo motors#
swingServo = servo.Servo(pca.channels[0]) #use setSwing to not break the opposite servo!!
headFB = servo.Servo(pca.channels[2]) #front to back CENTER: 105
headS2S = servo.Servo(pca.channels[1]) #side to side CENTER: 95
headRotate = servo.ContinuousServo(pca.channels[3], min_pulse=810, max_pulse=2300) #self explanatory
swingServo2 = servo.Servo(pca.channels[4]) #other swing servo. It swings opposite to the first one. USE SETSWING
#########################




print("TO CANCEL, USE CTRL+C, DONT CLOSE THE TAB")
print("Waiting 2 secs")
time.sleep(2)
motorDriverRelay.on()

### quality of life servo functions ###
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
	#max 125 
	#min 70
	if 125>=degrees>=70:
		difference=degrees-90
		swingServo.angle = 90 + difference
		swingServo2.angle = 90 - difference
	else:
		print("swing out of range: max 115 minimum 70")
#used for testing to "disable" servos who may be retaining their previous position

def setHeadFB(degrees):
	#center: 105
	if 65<degrees+15<150:
		headFB.angle = degrees+15;
	else:
		print("headFB can't go out of range")

def setHeadS2S(degrees):
	#center: 95
	if 45<degrees+5<145:
		headS2S.angle = degrees+5;
	else:
		print("headS2S can't go out of range")


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

def rest_all_servos():
	set_servo_floppy(0)
	set_servo_floppy(1)
	set_servo_floppy(2)
	set_servo_floppy(3)
	set_servo_floppy(4)

#unused for more traditional "servo.angle = degree" usage
def set_servo_angle(channel, angle):
    """Safely move servo unless it's in floppy mode."""
    if not servo_floppy[channel]:
        s = servo.Servo(pca.channels[channel])
        s.angle = angle
    else:
        print(f"Channel {channel} is in floppy mode; ignoring command.")
#######################################	

def headTurn(degrees):
	#2.65 seconds per turn at speed 1     22.64rpm
	#2.65 seconds per turn at speed -0.92 22.64rpm
	turnseconds=abs(degrees*(2.5/360))
	if degrees>0:
		headRotate.throttle=1
		time.sleep(turnseconds)
		headRotate.throttle=0
	if degrees<0:
		headRotate.throttle=-0.92
		time.sleep(turnseconds)
		headRotate.throttle=0
	

# Testing is contained in a Try except loop to turn off the DC motor driver 
# when the program is cancelled with ctrl+C. This prevents the motors
# from spinning uncontrollably when the program is cancelled without ctrl+C

# instructions for the DC drive motors
# 0 is full reverse
# 1 is full forward
# 0.5 is neutral
while True:
	try:
		if DCdrivemotorsTest:
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
			
		if SwingServoTest:
			# Quick Servo Test swings it back and forth


			setSwing(70)
			time.sleep(2)
			setSwing(117)
			time.sleep(2)
			
		if HeadServoTest:
			# Test Head Servos
			
			setHeadFB(90)
			setHeadS2S(90)
			headTurn(180)
			time.sleep(1)
			headTurn(180)
			
			time.sleep(2)
			
		
			
		
	except KeyboardInterrupt:
		
		#this sets the speed of the motors to 0 and turns off the relay.
		DCmotor2.value = 0.5
		DCmotor1.value = 0.5
		
		motorDriverRelay.off()
		rest_all_servos()
		print("Exiting")
		time.sleep(2)
		exit()


