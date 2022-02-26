from tplink_api import list_sys_info, device_name

import asyncio
            
asyncio.run(list_sys_info(device_name))