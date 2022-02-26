from tplink_api import is_on, switch_on, switch_off, device_name

import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

import asyncio
import sys

on = "POWER_ON"
off = "POWER_OFF"

def power_status() :
    is_powered_on = asyncio.run(is_on(device_name))
    if (is_powered_on):
        return on
    else :
        return off
    
def report_status(status):
    print(f'Reporting power Status = {status}')
    publish.single('living/tv_switch/status', status, retain=True, hostname='127.0.0.1')
      
report_status(power_status())

def handle_request(client, userdata, message):
    print("Received request@%s=%s" % (message.topic, message.payload))
    request = message.payload.decode('UTF-8')
    if (request == on):
        print('Requested to switch on')
        if (power_status() == on):
            print('Already on... so nothing to do')
        else:
            print('Currently off... so switching on...')
            asyncio.run(switch_on(device_name))        
    elif (request == off):
        print('Requested to switch off')
        if (power_status() == off):
            print('Already off... so nothing to do')
        else:
            print('Currently on... so switching off...')
            asyncio.run(switch_off(device_name))        
    else:
        print(f'Unexpected request: {message.payload}')
    report_status(power_status())

subscribe.callback(handle_request, "living/tv_switch/set", hostname="127.0.0.1")
