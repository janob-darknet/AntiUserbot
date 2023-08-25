import asyncio, aiocron, datetime
from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.functions.account import UpdateProfileRequest

api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"
client = TelegramClient("me", api_id, api_hash)
client.start()


@aiocron.crontab("*/1 * * * *")
async def set_clock():
    time = datetime.datetime.today().strftime("%H.%M")
    async with client:
        await client(UpdateProfileRequest(first_name=time))



client.start()
client.run_until_disconnected()