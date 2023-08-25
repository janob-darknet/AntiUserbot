from telethon import TelegramClient, sync, events
from telethon.sessions import StringSession
#
import getpass
#
from telethon.errors import SessionPasswordNeededError
#
from telethon.tl.functions.channels import JoinChannelRequest
#
from telethon.tl.functions.channels import LeaveChannelRequest
#
from telethon.tl.functions.messages import AddChatUserRequest
#
from telethon.tl.types import InputPhoneContact
#
from telethon.tl.functions.contacts import ImportContactsRequest
#
from telethon import functions, types
#
from telethon.tl.types import InputPhoneContact
#
from telethon.tl.functions.messages import SendReactionRequest
#
from telethon.tl.functions.users import GetFullUserRequest
#
import os, sys
#
from telethon.tl.functions.account import UpdateProfileRequest
#
from telethon.tl.functions.account import UpdateUsernameRequest
#
from telethon.tl.functions.photos import UploadProfilePhotoRequest
#
from telethon.tl.functions.messages import ImportChatInviteRequest
#
import asyncio, aiocron, datetime
#
import time
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
#
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
#
from telethon.tl.functions.channels import InviteToChannelRequest
#
import configparser
#
import csv
#
import traceback
#
import random
#
from time import sleep
#
from banners import terminal
from janob_darknet import code
from variables import numbers
#
os.system("clear")
#print(variables.words)
print(terminal.term_manager)
#
term_manager = input(">>> ")
#
if term_manager == numbers.num1:
		api_id = code.api_id
		api_hash = code.api_hash
		#os.system("clear")
		
		
		string = code.session
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
		    guruh = code.chat
		    
		    await client(JoinChannelRequest(guruh))
		    while True:
		    	await client.send_message(code.chat,  input('message: '))
		
		with client:
		    client.loop.run_until_complete(main())

elif term_manager == numbers.num2:
		api_id = code.api_id
		api_hash = code.api_hash
		
		
		
		string = code.session
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		
		    client.send_message("me", client.session.save())
		###########
		
		
		
		@client.on(events.NewMessage(pattern=".scan"))
		async def chatscan(event):
				async for dailog in client.iter_dialogs():
					print(dailog.name + " \033[1;32m id:\033[1;31m " + str(dailog.id))
		
				
		client.start()
		client.run_until_disconnected()
#
elif term_manager == numbers.num3:
		api_id = code.api_id
		api_hash = code.api_hash
		
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		async def main():
		
		    async for message in client.iter_messages(code.chat):
		        print(message.sender.username, message.text)
		        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
		with client:
			client.loop.run_until_complete(main())
#
elif term_manager == "4":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		string = code.session
		#
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
		    #reaksiya yuborish
		    
		    await client(SendReactionRequest(
		    peer=code.chat,
		    msg_id=code.msg_id,
		 
		    reaction='👍️'
		))
		
		
		with client:
		    client.loop.run_until_complete(main())
		    print("Succesfully")
	
elif term_manager == "6":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		@client.on(events.NewMessage)
		async def _(event):
			
			if '.first_name' in event.raw_text:
			   await client(UpdateProfileRequest(
		   	 first_name= code.first_name
			))
			   #username
			   #await client(UpdateUsernameRequest('fake_7719'))
			   #profile image
			  #
		#bio or name
			   #await client(UpdateProfileRequest(
		   	 #about='Umod va ftg userbotlari uchun AntiUserbot plugini'
			#))
		
		client.start()
		print("run")
		client.run_until_disconnected()
		
elif term_manager == "5":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		@client.on(events.NewMessage)
		async def _(event):
			
			if '.about' in event.raw_text:
			   await client(UpdateProfileRequest(
		   	 about= code.about
			))
			   #username
			   #await client(UpdateUsernameRequest('fake_7719'))
			   #profile image
			  #
		#bio or name
			   #await client(UpdateProfileRequest(
		   	 #about='Umod va ftg userbotlari uchun AntiUserbot plugini'
			#))
		
		client.start()
		print("run")
		client.run_until_disconnected()
elif term_manager == "7":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		@client.on(events.NewMessage)
		async def _(event):
			if '.image' in event.raw_text:
				
			
			#
			   #username
			   await client(UpdateUsernameRequest(code.username))
			   #profile image
			  #
		#bio or name
			   #await client(UpdateProfileRequest(
		   	 #about='Umod va ftg userbotlari uchun AntiUserbot plugini'
			#))
		
		client.start()
		print("run")
		client.run_until_disconnected()

elif term_manager == "8":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		string = code.session
		
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		@client.on(events.NewMessage)
		async def _(event):
			
			if '.test' in event.raw_text:
		#	   await client(UpdateProfileRequest(
		#   	 first_name='Account Hacked'
		#	))
			   #username
			   #await client(UpdateUsernameRequest('fake_7719'))
			   #profile image
			   await client(UploadProfilePhotoRequest(
    client.upload_file('test.jpg')
))
			  #
		#bio or name
			   #await client(UpdateProfileRequest(
		   	 #about='Umod va ftg userbotlari uchun AntiUserbot plugini'
			#))
		
		client.start()
		client.run_until_disconnected()
elif term_manager == "9":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		string = code.session
		#
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
			guruh = code.chat
			await client(JoinChannelRequest(guruh))
		
		
		with client:
		    client.loop.run_until_complete(main())
		
		
		
		
		client.start()
		client.run_until_disconnected()
	
elif term_manager == "10":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		
		string = code.session
		#
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
			await client(ImportChatInviteRequest(code.chat))
		
		
		with client:
		    client.loop.run_until_complete(main())
		
		
		
		
		client.start()
		client.run_until_disconnected()
	
elif term_manager == "11":
		api_id = 10953300
		api_hash = "9c24426e5d6fa1d441913e3906627f87"
		#os.system("clear")
		string = code.session
		#
		with TelegramClient(StringSession(string), api_id, api_hash) as client:
		    client.send_message("me", client.session.save())
		
		
		
		async def main():
			input_channel = code.chat
			await client(LeaveChannelRequest(input_channel))
		
		
		with client:
		    client.loop.run_until_complete(main())
		
		
		
		
		client.start()
		client.run_until_disconnected()
elif term_manager == '0':
	os.system("exit")
	os.system("python main.py")
else:
		print("\033[91mError")
