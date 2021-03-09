import paho.mqtt.publish as publish
import time

for i in range(100):
    publish.single("home/living/fiets/credits", i, hostname="127.0.0.1")
    time.sleep(0.1)
    
for i in range(100,0, -1):
    publish.single("home/living/fiets/credits", i, hostname="127.0.0.1")
    time.sleep(0.1)
    


