import asyncio
from psnawp_api import *

psnawp = PSNAWP('zJNnVd8rvBkf0Y6Gv9Z9Lj3PcAZWq63KwJ8DuvVp2sfFpdSvyVuZwVHeg2hmaZ3Z')
example_user_1 = psnawp.user(online_id="JackPowell")
client = psnawp.me()
devices = client.get_account_devices()
friends_list = client.friends_list()

titles_with_stats = client.title_stats(limit=10)
for title in titles_with_stats:
    print(
        f" \
        Game: {title.name} - \
        Play Count: {title.play_count} - \
        Play Duration: {title.play_duration} \n"
    )

print(example_user_1.get_presence())

# async def main():
#     psnawp = await PSNAWP.create('ajbE5UawaBoRLYDaU4YEm2edulnZNASZDQCCObnGyRCIa9vLECgxRkZwvnBYWA0G')
#     example_user_1 = await psnawp.user(online_id="JackPowell")
#     example_user_1.get_presence()
#     print(example_user_1)
# asyncio.run(main())
