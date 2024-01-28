import asyncio
from psnawp_api import *


async def main() -> PSNAWP:
    #Get User
    psnawp = await PSNAWP.create('ajbE5UawaBoRLYDaU4YEm2edulnZNASZDQCCObnGyRCIa9vLECgxRkZwvnBYWA0G')
    me = await psnawp.user(online_id="me")
    client = await psnawp.me()
    
    #Get Presence and current play info
    presence = await me.get_presence()
    available = presence.get("basicPresence").get("availability") #availableToPlay, unavailable
    platform = presence.get("basicPresence").get("primaryPlatformInfo").get("platform") #PS5, PS4
    online = presence.get("basicPresence").get("primaryPlatformInfo").get("onlineStatus") #online, offline
    if online == 'availableToPlay':
        title_id = presence.get("basicPresence").get("gameTitleInfoList").get("npTitleId")
        title_name = presence.get("basicPresence").get("gameTitleInfoList").get("titleName")
        title_format = presence.get("basicPresence").get("gameTitleInfoList").get("format")
        title_art = presence.get("basicPresence").get("gameTitleInfoList").get("conceptIconUrl") #Only for PS5, ?ps4
    
    #Send a message
    steven = await psnawp.user(online_id="spesauce")
    group = await psnawp.group(users_list=[steven])
    #response = await group.send_message("Ignore this message. You're my api test at the moment.")
    
    #Chat Groups
    #client = await psnawp.me()
    #groups = await client.get_groups()
    #for group in groups:
    #    print(group.information)

    #Friends List
    print(await client.friends_list())

    #Users Online
    friends = await client.available_to_play()
    print(friends)

    #Trophy Summary
    trophy = await client.trophy_summary()

    #User Search
    search = psnawp.search()
    #user = await search.universal_search("Username")

    #Title Details
    title = psnawp.game_title("PPSA02432_00", "me", "PPSA02432_00") #np_comm is not really used but is supplied to skip code
    details = await title.get_details()

    #Trophies All
    trophy_title = psnawp.trophy_titles()
    titles = await trophy_title.get_trophy_titles(limit = 5)

    #Trophy by title
    test = await trophy_title.get_trophy_summary_for_title(title_ids=["PPSA02432_00"])

    # Get Play Times (PS4, PS5 above only)
    titles_with_stats = await client.title_stats()
    print(titles_with_stats)

    #np_id
    #np_id = await TrophyTitles.get_np_communication_id(client._request_builder, "PPSA02432_00", "me")

psn = asyncio.run(main())
#PPSA02432_00
