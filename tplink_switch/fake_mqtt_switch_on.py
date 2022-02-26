import paho.mqtt.publish as publish
publish.single('fiets/automation-debug', 'Fake Switch On', hostname='127.0.0.1')
