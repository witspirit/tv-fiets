from tplink_api import list_device, device_name

import asyncio
            
asyncio.run(list_device(device_name))