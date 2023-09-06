import asyncio
import re
import random
import requests
from Barath import barath, MODULE
from pyrogram import filters          
from config import OWNER_ID, HANDLER

@barath.on_message(filters.command("cat", prefixes=HANDLER) & filters.user(OWNER_ID))
async def cat(_, message):
    api = requests.get("https://api.thecatapi.com/v1/images/search").json()
    url = api[0]["url"]
    if url.endswith(".gif"):
        await message.reply_animation(url)
    else:
        await message.reply_photo(url)

@barath.on_message(filters.regex("baka") & filters.user(OWNER_ID))
async def baka(_, message):
    reply = message.reply_to_message
    api = requests.get("https://nekos.best/api/v2/baka").json()
    url = api["results"][0]['url']
    anime = api["results"][0]["anime_name"]     
    if reply:
        user = reply.from_user
        name = user.first_name
        username = user.username
        user_profile_link = f"https://t.me/{username}" if username else ""
        user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
        await reply.reply_animation(url, caption="**• {}**\n**Baka! {}**".format(anime, user_hyperlink))
    else:
        await message.reply_animation(url, caption="**• {}**\n**Baka!**".format(anime))

@barath.on_message(filters.regex("hug") & filters.user(OWNER_ID))
async def hug(_, message):
    reply = message.reply_to_message
    api = requests.get("https://nekos.best/api/v2/hug").json()
    url = api["results"][0]['url']
    anime = api["results"][0]["anime_name"]     
    if reply:
        user = reply.from_user
        name = user.first_name
        username = user.username
        user_profile_link = f"https://t.me/{username}" if username else ""
        user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
        await reply.reply_animation(url, caption="**• {}**\n**Hugs! {}**".format(anime, user_hyperlink))
    else:
        await message.reply_animation(url, caption="**• {}**\n**Hugs!**".format(anime))

@barath.on_message(filters.command("in", prefixes=HANDLER) & filters.user(OWNER_ID))
async def insult(_, message):
    reply = message.reply_to_message
    try:
        insult = requests.get("https://insult.mattbas.org/api/insult").text
        if reply:
            user = reply.from_user
            name = user.first_name
            username = user.username
            user_profile_link = f"https://t.me/{username}" if username else ""
            user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
            string = insult.replace("You are", user_hyperlink)
            await message.reply(string)
        else:
            await message.reply(insult)
    except Exception as e:
        await message.reply(f"Error: {e}")

@barath.on_message(filters.command("ri", prefixes=HANDLER) & filters.user(OWNER_ID))
async def riddle(_, message):
    riddle = requests.get("https://riddles-api.vercel.app/random").json()
    question = riddle["riddle"]
    answer = riddle["answer"]
    msg = await message.reply(f"**• Riddle**:\n[ `{question}` ]\n\n[ `The Answer will show automatically 20 seconds after tell me your guess's!` ]")
    await asyncio.sleep(20)
    await msg.edit(f"**• Riddle**:\n[ `{question}` ]\n\n• **Answer**: [ `{answer}` ]")

@barath.on_message(filters.command("qu", prefixes=HANDLER) & filters.user(OWNER_ID))
async def quote(_, m):
    api = random.choice(requests.get("https://type.fit/api/quotes").json())
    string = api["text"]
    author = api["author"]
    await m.reply(
        f"**Quotes**:\n`{string}`\n\n"
        f"   ~ **{author}**")

@barath.on_message(filters.command("gt", prefixes=HANDLER) & filters.user(OWNER_ID))
async def google_it(_, message):
    file_id = "CAACAgUAAx0CXss_8QABB0iVY2ZDrB4YHzW6u1xRqKLuUX7b6sEAAhUAA-VDzTc4Ts7oOpk4nx4E"
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(sticker=file_id, reply_markup=None)
        await message.reply_to_message.reply_text("🔎 [Google](https://www.google.com/search?)", disable_web_page_preview=True)
    else:
        await message.reply_sticker(sticker=file_id, reply_markup=None)
        await message.reply_text("🔎 [Google](https://www.google.com/search?)", disable_web_page_preview=True)


__mod_name__ = "FUN"  
    
__help__ = """  
- gt: ggl search
- in: insult someone
- hug: try self
- baka: try self
- cat: rndm cat img
- ri: rndm riddle
- qu: rndm quotes eng
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
