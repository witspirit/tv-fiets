import paho.mqtt.publish as publish
publish.single('fiets/automation-debug', 'Fake Switch Off', hostname='127.0.0.1')