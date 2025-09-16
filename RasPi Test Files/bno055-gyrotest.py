import time

import board

import adafruit_bno055

i2c = board.I2C()  
sensor = adafruit_bno055.BNO055_I2C(i2c)
last_val = 0xFFFF


def temperature():
    global last_val  # noqa: PLW0603
    result = sensor.temperature
    if abs(result - last_val) == 128:
        result = sensor.temperature
        if abs(result - last_val) == 128:
            return 0b00111111 & result
    last_val = result
    return result


while True:
    
    #print(
    #    "Temperature: {} degrees C".format(temperature())
    #)  # Uncomment if using a Raspberry Pi
    
    #print(f"Accelerometer (m/s^2): {sensor.acceleration}")
    #print(f"Magnetometer (microteslas): {sensor.magnetic}")
    #print(f"Gyroscope (rad/sec): {sensor.gyro}")
    
    #### I only left the Euler Angle uncommented to find position info
    #### all of the other data works
    print(f"Euler angle: {sensor.euler}")
    
    
    #print(f"Quaternion: {sensor.quaternion}")
    #print(f"Linear acceleration (m/s^2): {sensor.linear_acceleration}")
    #print(f"Gravity (m/s^2): {sensor.gravity}")
    #print()

    time.sleep(1)
