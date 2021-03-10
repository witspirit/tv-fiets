import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LINEAR_HALL = 23
GPIO.setup(LINEAR_HALL, GPIO.IN)

selectedDetector = LINEAR_HALL

cycleCredits = 0

# Using the linear hall sensor, we get a pulsed signal when nothing
# detected and a low signal when the field is there. So whenever the
# pulsing stops, we have a detection.
# Not sure how to properly model that

def t():
    return time.time() * 1000 # [ms]
    

def sonic():
    pulse_start = t()
    pulse_end = t()
    while True:
        # Wait until we see the first 1
        pulse_start = t()
        while GPIO.input(selectedDetector) == 0:
            pulse_start = t()
        # pulse_start now contains the moment we saw the line high
        
        pulse_end = t()
        while GPIO.input(selectedDetector) == 1:
            pulse_end = t()
        # pulse_end now contains the moment we saw the line go down again
        
        pulse_duration = pulse_end - pulse_start # [ms]
        print(time.time(),' | pulse_duration = ', pulse_duration)
    
        time.sleep(0.01)
        
def iteration():
    while True:
        lastPulse = t()
        # Wait until we see 1
        while GPIO.input(selectedDetector) == 0:
            continue
        # Wait until we see 0
        while GPIO.input(selectedDetector) == 1:
            continue
    
        iteration_duration = round(t() - lastPulse, 2)
        # print(round(time.time(), 6),' | iteration_duration = ', iteration_duration, ' [ms]')
        if iteration_duration > 0.1 :
            print(round(time.time(), 6), ' | INTERRUPTION DETECTED')                    


iteration()
