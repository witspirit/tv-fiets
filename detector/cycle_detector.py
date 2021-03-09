import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish

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
    currentTime = time.time()
    
    if lastDetection == False and currentDetection == True:
        cycleCredits+=1    
        cycleTime = currentTime - lastCycle
        lastCycle = currentTime
        print('Credits = ', cycleCredits, ' Revolution Duration = ', cycleTime)
        publish.single("home/living/fiets/credits", cycleCredits, hostname="127.0.0.1")
    
    if currentDetection != lastDetection:
        # print(round(time.time(),0),' Change detected: ', currentDetection)
        lastDetection = currentDetection
        
    if currentTime - lastCycle > 3 and cycleCredits > 1:        
        cycleCredits+=-1
        print('Idling...losing credits. Credits = ', cycleCredits)
        publish.single("home/living/fiets/credits", cycleCredits, hostname="127.0.0.1")
    
    time.sleep(0.01)

