import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
SIMPLE_REED = 4
GPIO.setup(SIMPLE_REED, GPIO.IN)

selectedDetector = SIMPLE_REED

cycleCredits = 0

# A detection should be a HIGH, LOW, HIGH sequence
# So basically whenever we see a LOW -> HIGH transition we can count


lastDetection = not GPIO.input(selectedDetector)
lastCycle = time.time()
while True:
    currentDetection = GPIO.input(selectedDetector)
    if lastDetection == False and currentDetection == True:
        cycleCredits+=1
        currentTime = time.time()
        cycleTime = currentTime - lastCycle
        lastCycle = currentTime
        print('Credits = ', cycleCredits, ' Revolution Duration = ', cycleTime)
    
    if currentDetection != lastDetection:
    #    print(round(time.time(),0),' Change detected: ', currentDetection)
        lastDetection = currentDetection    
    time.sleep(0.01)

