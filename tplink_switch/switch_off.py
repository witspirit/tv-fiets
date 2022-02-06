from tplink_api import switch_off, device_name

import asyncio
            
asyncio.run(switch_off(device_name))
