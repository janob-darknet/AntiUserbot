import os
import shutil
import time
import requests
from telethon import events
import sys_os.client
client = sys_os.client.client
PATH = "./repo/"


async def download_repo(repo_url: str):
    
    repo_name = repo_url.split("/")[-1]
    
    repo_path = f"{PATH}/{repo_name}"
    
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)  
    os.makedirs(repo_path)  

    
    zip_url = f"{repo_url}/archive/master.zip"
    response = requests.get(zip_url)

    
    zip_path = f"{PATH}/{repo_name}.zip"
    with open(zip_path, 'wb') as f:
        f.write(response.content)

    return repo_path



@events.register(events.NewMessage(pattern=r".gitsave (.*)", outgoing=True))
async def gitsave(event):
    try:
        
        repo_url = event.pattern_match.group(1)
        await event.edit('📂 yuklanmoqda.')
        time.sleep(1)
        await event.edit('📂 yuklanmoqda..')
        time.sleep(1)
        await event.edit('📂 yuklanmoqda...')
        repo_path = await download_repo(repo_url)
        f = open(f"{repo_path}.zip", "rb")
        await event.delete()
        await client.send_file(event.chat_id, f, caption='💻 Downloaded from Github ☑️\n\n🧑‍💻 Sys_ub')
        shutil.rmtree(PATH)
    except:
        await event.edit("There was an error downloading the repo 😔")