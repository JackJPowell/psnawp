import asyncio
from psnawp_api import *

psnawp = PSNAWP('ajbE5UawaBoRLYDaU4YEm2edulnZNASZDQCCObnGyRCIa9vLECgxRkZwvnBYWA0G')
example_user_1 = psnawp.user(online_id="JackPowell")
print(example_user_1.get_presence())

# async def main():
#     psnawp = await PSNAWP.create('ajbE5UawaBoRLYDaU4YEm2edulnZNASZDQCCObnGyRCIa9vLECgxRkZwvnBYWA0G')
#     example_user_1 = await psnawp.user(online_id="JackPowell")
#     example_user_1.get_presence()
#     print(example_user_1)
# asyncio.run(main())
