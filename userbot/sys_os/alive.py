from telethon import TelegramClient, events
import sys_os.client
import os
import time
client = sys_os.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(noob_py):
		client = noob_py.client
		me = await client.get_me()
		username = me.username
		os_sys = await client.download_profile_photo(username)
		await client.edit_message(noob_py.message, "Hayrli kun...")
		time.sleep(0.5)
		await noob_py.respond("""🥷 **Foydalanuvchi**: @{}

🥷 **Versia**: 1.0.1.3
├╴╴╴╴╴╴╴╴╴╴
└ 🧟‍♀️ **Sys Userbot**: @sys_ub

 👾 **2021yil 10oy 19kun dasturlangan**
 👾 **ajdodi**: magicbot-uz
 👾 **Dasturchi**: @janob_darknet

🥷 OʻRNATISH 
├╴╴╴╴╴╴╴╴╴╴
├ 👾 https://t.me/sys_ub
└ 👾 https://t.me/KaliNethunterUz,""".format(username, ' '), file=os_sys)
		await noob_py.message.delete()
		os.remove(os_sys)