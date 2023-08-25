from telethon import TelegramClient, sync
from telethon.sessions import StringSession
import getpass
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from time import sleep
import os, sys
api_id = 10953300
api_hash = "9c24426e5d6fa1d441913e3906627f87"

string = "1ApWapzMBuylkPPxV08SS1AU3nOONRzSUbqJLht2gju_djYjhR3tGbz-jXCnUI61WUPg6G4ckXysqgeIcBfiHEjWzwTF6cfphpd7btRfCNZO3se6awwQxFVQuXUdLDc3WJZOdXcQ1eVFvNlyMVSVgFGNVGYcHR3XZZynGTVhvyfFtZrJatT5OphlUC4cqDCeFALoakdZnDg4z7YqG6pw32LbM0_VUxukw8GAsSVVqgbJ4dNLAwGdyoNQQavsM_mNFvuMwo2xUnt_BF3R60crO1Jmu0RteT2aaq-AcSWMLzGLl7K_jguiO9LlOZexmNsXv8hXjcRp56SvoN3I1gPL_r8EgZnqOiMI="

with TelegramClient(StringSession(string), api_id, api_hash) as client:
    #print(client.session.save())
    client.send_message("me", client.session.save())

