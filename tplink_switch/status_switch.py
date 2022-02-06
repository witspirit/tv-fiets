from tplink_api import is_on, device_name

import asyncio
import sys
            
is_powered_on = asyncio.run(is_on(device_name))

# The contract of the CLI integraiton on Home Assistant is a bit unexpected
# It expects 0 for Switch On and anything else for Off
exit_code = 0 if is_powered_on else 1
print(exit_code)
sys.exit(exit_code)
