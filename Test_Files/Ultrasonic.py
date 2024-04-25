# The purpose of this file is to see if an ultrasonic senor is functional
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#Change this pin numbers based on which pins you use
TRIG = 23
ECHO = 25

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

try:
    while True:
        
        GPIO.output(TRIG, False)
        time.sleep(2)
        
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
            
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
            
        pulse_duration = pulse_end - pulse_start
        
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print("Distance: ", distance, "cm")
        
except KeyboardInterrupt:
    print("Clean up")
    gpio.cleanup()
        