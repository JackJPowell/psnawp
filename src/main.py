from psnawp_api import PSNAWP


psnawp = PSNAWP("")

# Your Personal Account Info
client = psnawp.me()
print(f"Online ID: {client.online_id}")
print(f"Account ID: {client.account_id}")
title = psnawp.game_title("PPSA21564_00", "me")
info = title.get_details()
#german = title.get_details("DE", "de")
print(info)