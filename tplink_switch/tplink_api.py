import configparser
import asyncio
import json
import os

from tplinkcloud import TPLinkDeviceManager

config = configparser.ConfigParser(interpolation=None)
config.read(os.path.expanduser('~/.tplink_config.txt'))

username = config['kasa']['username']
password = config['kasa']['password']
device_name = config['device']['name']

device_manager = TPLinkDeviceManager(username, password)

async def list_devices():
    devices = await device_manager.get_devices()
    if devices:
        print(f'Found {len(devices)} devices')
        for device in devices:
            print(f'"{device.model_type.name}" device called "{device.get_alias()}"')
    else:
        print('Failed to fetch devices')

async def list_device(name):
    device = await device_manager.find_device(name)
    if device:
        print(f'"Found {device.model_type.name}" device called "{device.get_alias()}"')
        print(json.dumps(device.device_info, indent=2, default=lambda x: vars(x)
                        if hasattr(x, "__dict__") else x.name if hasattr(x, "name") else None))
    else:
        print(f'Device {name} was not found')
        
async def list_sys_info(name):
    device = await device_manager.find_device(name)
    if device:
        print(json.dumps(await device.get_sys_info(), indent=2, default=lambda x: vars(x)
                        if hasattr(x, "__dict__") else x.name if hasattr(x, "name") else None))
    else:
        print(f'Device {name} was not found')
        

async def is_on(name):
    device = await device_manager.find_device(name)
    if device:
        return device.device_info.status
    else:
        print(f'Device {name} was not found')
        return 0

async def switch_on(name):
    device = await device_manager.find_device(name)
    if device:
        await device.power_on()
    else:
        print(f'Device {name} was not found')
        
async def switch_off(name):
    device = await device_manager.find_device(name)
    if device:
        await device.power_off()
    else:
        print(f'Device {name} was not found')

