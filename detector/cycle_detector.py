import RPi.GPIO as GPIO
import time
import paho.mqtt.publish as publish

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
HALL_SWITCH = 23
GPIO.setup(HALL_SWITCH, GPIO.IN)

selectedDetector = HALL_SWITCH

cycleCredits = 0

# A detection should be a HIGH, LOW, HIGH sequence
# So basically whenever we see a LOW -> HIGH transition we can count


lastDetection = not GPIO.input(selectedDetector)
lastCycle = time.time()
lastDepreciation = time.time();
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
        print(round(time.time(),0),' Change detected: ', currentDetection)
        lastDetection = currentDetection
        
    if currentTime - lastDepreciation > 3 and cycleCredits > 0:        
        cycleCredits+=-1
        print('Idling...losing credits. Credits = ', cycleCredits)
        lastDepreciation = time.time()
        publish.single("home/living/fiets/credits", cycleCredits, hostname="127.0.0.1")
    
    time.sleep(0.01)

