from os import remove
from telethon import TelegramClient, events

@events.register(events.NewMessage(outgoing=True, pattern=r'\.rcd'))
async def rundrc(event):
    await event.delete()
    try:
        getrestrictedcontent = await event.get_reply_message()
        downloadrestrictedcontent = await getrestrictedcontent.download_media()
        await event.client.send_file("me", downloadrestrictedcontent)
        remove(downloadrestrictedcontent)
    except:
        pass