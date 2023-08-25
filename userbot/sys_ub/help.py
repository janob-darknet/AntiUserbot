from telethon import TelegramClient, events
import sys_os.client
import os
import time
client = sys_os.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.help'))
async def help(noob_py):
		client = noob_py.client
		me = await client.get_me()
		username = me.username
		os_sys = await client.download_profile_photo(username)
		await client.edit_message(noob_py.message, "Hayrli kun...")
		time.sleep(0.5)
		await noob_py.respond("""Sys_Ub Animation menu commands

**.snake**  **.nothappy**  **.heart**  **.lul**  **.clown**

Functions command 
**.alive**  **.mute <m h d>**  **.userinfo <reply> **  **.iptrace <ip>**  **.webscreen <url>**  **.gitsave <url>**  **.rcd <replay>**
""".format(username, ' '), file=os_sys)
		await noob_py.message.delete()
		os.remove(os_sys)