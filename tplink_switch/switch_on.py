from tplink_api import switch_on, device_name

import asyncio
            
asyncio.run(switch_on(device_name))
