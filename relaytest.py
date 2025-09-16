#relay test
from gpiozero import OutputDevice
import time


relay = OutputDevice(17)
while True:
	
	# This tests the relay that controls the DC motor driver. I deemed a relay 
	# to be necessary after having a recurring issue of the motor driver allowing
	# the motors to run away.
	
	# I'm sure there was a better fix than adding hardware, but a relay is a fix
	# nonetheless.
	
	relay.on()
	print("Relay on")
	time.sleep(5)
	relay.on()
	print("Relay off")
	time.sleep(5)
	

