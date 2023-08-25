from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession

from time import sleep

import sys_os.animation, sys_os.client, sys_os.alive, sys_os.help, sys_os.mute, sys_os.userinfo, sys_os.iptrace, sys_os.webscreen, sys_os.gitsave, sys_os.chatinfo, sys_os.rcddcr, sys_os.tts

client = sys_os.client.client



with client as darknet:
	darknet.add_event_handler(sys_os.animation.lul)

with client as darknet:
	darknet.add_event_handler(sys_os.animation.snake)

with client as darknet:
	darknet.add_event_handler(sys_os.animation.nothappy)

with client as darknet:
	darknet.add_event_handler(sys_os.animation.heart)

with client as darknet:
	darknet.add_event_handler(sys_os.alive.alive)

with client as darknet:
	darknet.add_event_handler(sys_os.help.help)	

with client as darknet:
	darknet.add_event_handler(sys_os.mute.mute)

with client as darknet:
	darknet.add_event_handler(sys_os.animation.clown)	

with client as darknet:
	darknet.add_event_handler(sys_os.userinfo.userinfo)	

with client as darknet:
	darknet.add_event_handler(sys_os.iptrace.iptrace)	

with client as darknet:
	darknet.add_event_handler(sys_os.webscreen.webscreen)

with client as darknet:
	darknet.add_event_handler(sys_os.gitsave.gitsave)

with client as darknet:
	darknet.add_event_handler(sys_os.chatinfo.chatinfo)

with client as darknet:
	darknet.add_event_handler(sys_os.rcddcr.rundrc)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
client.start()
client.run_until_disconnected()