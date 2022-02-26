import paho.mqtt.publish as publish

publish.single('fiets/credits', 0, hostname='127.0.0.1')
publish.single('fiets/tv', 'off', hostname='127.0.0.1')
publish.single('fiets/automation-debug', 'Fiets - CLI Init', hostname='127.0.0.1')

