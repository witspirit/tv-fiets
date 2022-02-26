import paho.mqtt.publish as publish
import random

is_on = random.choice([True, False])
publish.single('fiets/automation-debug', f'Fake Switch State={is_on}', hostname='127.0.0.1')
if (is_on):
    print('1')
else:
    print('0')

