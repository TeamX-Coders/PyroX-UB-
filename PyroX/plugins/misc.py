import asyncio 

from PyroX import PyroX, MODULE
from config import HANDLER
from pyrogram import filters
from gpytranslate import Translator

import requests


@PyroX.on_message(filters.command(["ud","define"],prefixes=HANDLER) & filters.me)
async def ud(_, message):
        if len(message.command) < 2:
             return await message.edit("where you input the text?")         
        text = message.text.split(None, 1)[1]
        try:
          results = requests.get(
            f'https://api.urbandictionary.com/v0/define?term={text}').json()
          reply_text = f'**results: {text}**\n\n{results["list"][0]["definition"]}\n\n_{results["list"][0]["example"]}_'
        except Exception as e: 
              return await message.edit_text(f"Somthing wrong Happens:\n`{e}`")
        ud = await message.edit_text("Exploring....")
        await ud.edit_text(reply_text)
        
        
trans = Translator()
@PyroX.on_message(filters.command("tr",prefixes=HANDLER) & filters.me)
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("[Reply To The Message Using The Translation Code Provided!](https://telegra.ph/Lang-Codes-03-19-3)")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"**Translated from {source} to {dest}**:\n"
        f"`{translation.text}`"
    )
    await message.delete()
    await reply_msg.reply_text(reply)
    return 

@PyroX.on_message(filters.command("webss", prefix) & filters.me)
async def webshot(_, message):
    try:
        user_link = message.command[1]
        await message.delete()
        full_link = f"https://webshot.deam.io/{user_link}/?delay=2000"
        await PyroX.send_document(message.chat.id, full_link, caption=f"{user_link}")
    except Exception as e:
        await message.edit(format_exc(e))

            

__mod_name__ = "MISC"  
    
__help__ = """  
- tr: translate any text 
- ud: find wrd in disctinory
- webshot: webss url
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
