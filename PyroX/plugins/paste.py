import requests 
import config, os
import datetime

from PyroX import PyroX, MODULE
from pyrogram import filters

async def convert_to_datetime(timestamp): # Unix timestamp
    try:
        date = datetime.datetime.fromtimestamp(timestamp)
        return date
    except Exception as e:
        print(f"Error converting timestamp: {e}")
        return ""

async def spacebin(text: str):
    url = "https://spaceb.in/api/v1/documents/"
    response = requests.post(url, data={"content": text, "extension": "txt"})
    id = response.json().get('payload').get('id')
    res = requests.get(f"https://spaceb.in/api/v1/documents/{id}").json()
    created_at = res.get("payload").get("created_at")
    link = f"https://spaceb.in/{id}"
    raw = f"https://spaceb.in/api/v1/documents/{id}/raw"
    timedate = await convert_to_datetime(created_at)
    string = f"""\u0020
**Here's the link**: **[Paste link]({link})**
**Here's the link**: **[Raw View]({raw})**
**Created datetime**: {timedate}
"""
    return string

@PyroX.on_message(filters.command("paste", config.HANDLER) & filters.me)
async def paste(_, message):
    # share your codes on https://spacebin.in
    if not message.reply_to_message:
        try:
            text = message.text.split(None, 1)[1]
        except IndexError:
            await message.edit("=> Input text to paste else reply.")
            return 

        link = await spacebin(text)
        await message.edit(link, disable_web_page_preview=True)
        return

    elif bool(message.reply_to_message.text or message.reply_to_message.caption):
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        elif message.reply_to_message.caption:
            text = message.reply_to_message.caption

        link = await spacebin(text)
        await message.edit(link, disable_web_page_preview=True)
        return

    elif (message.reply_to_message.document and bool(message.reply_to_message.document.mime_type.startswith("text/"))):
        try:
            path = await PyroX.download_media(message.reply_to_message)
            with open(path, "r") as file:
                text = file.read()
            os.remove(path)
            link = await spacebin(text)
            await message.edit(link, disable_web_page_preview=True)
        except Exception as e:
            print(f"Error processing document: {e}")
            await message.edit("=> Error processing the document.")
    else:
        await message.edit("=> I am unable to paste this.")


__mod_name__ = "PASTE"  
    
__help__ = """  
- paste: paste txt to nekobin
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
