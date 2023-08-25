import io
from io import BytesIO
import os
import requests
from telethon import events
from telethon.tl.types import DocumentAttributeFilename
import time 
import sys_os.client
client = sys_os.client.client
@events.register(events.NewMessage(pattern=r".webscreen (.*)", outgoing=True))
async def webscreen(event):
    await event.edit("📸 Screen qilinmoqda.")
    time.sleep(1)
    await event.edit("📸 Screen qilinmoqda..")
    time.sleep(1)
    await event.edit("📸 Screen qilinmoqda...")
    url = event.pattern_match.group(1)
    response = requests.get(f"https://api.apiflash.com/v1/urltoimage?access_key=3da31bb6a13047f0a2e4d2030a6c79ad&url={url}")
    if response.status_code == 200:
       image = io.BytesIO(response.content)
       image.name = "sys_ub.png"
       await event.delete()
       await client.send_file(event.chat_id,image, caption=f"🌐 Website {url}")
    else:
        await event.edit("man bu siteni screenshot qila olmadim 😔")