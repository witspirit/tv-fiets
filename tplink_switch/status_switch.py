from tplink_api import is_on, device_name

import asyncio
import sys
            
is_powered_on = asyncio.run(is_on(device_name))
print(is_powered_on)
