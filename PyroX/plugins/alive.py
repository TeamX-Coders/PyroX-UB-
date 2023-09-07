import time 
import random 
import asyncio
from config import HANDLER
from pyrogram import filters, __version__ as pyrover, enums
from PyroX import PyroX, get_readable_time, StartTime
from PyroX import bot, MODULE

async def alive():
    katsuki = "3.01"
    user = await PyroX.get_me()
    name = user.first_name
    username = user.username
    user_profile_link = f"https://t.me/{username}" if username else ""
    user_hyperlink = f"[{name}]({user_profile_link})" if user_profile_link else name
    dbhealth = "ᴡᴏʀᴋɪɴɢ"
    uptime = get_readable_time((time.time() - StartTime))
    start_time = time.time()
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    
    ALIVE_TEX = " 𝙷𝙴𝚈 , 𝙱𝙰𝙱𝙴 😍 𝙸 𝙰𝙼 𝙰𝙻𝙸𝚅𝙴"
    EMOTES = ["😍", "💀", "😊", "👋", "🎉", "🔥", "🌟", "💫", "🚀", "🤖", "👻", "👾", "🧡"]

    photo_url = "https://te.legra.ph/file/4489fb9f5bccfe210def1.jpg"
    
    ALIVE_TEXT = f"""{ALIVE_TEX}

ㅤ╔══════💫✨💫═════╗
¹┃ㅤ{random.choice(EMOTES)} s ᴛ ᴀ ᴛ ᴜ s ➫ {dbhealth}
²┃ㅤ{random.choice(EMOTES)} ᴋᴀᴛsᴜᴋɪ   ʙ ᴏ ᴛ ➫ {katsuki}
³┃ㅤ{random.choice(EMOTES)} ᴜ ᴘ ᴛ ɪ ᴍ ᴇ ➫ {uptime}
⁴┃ㅤ{random.choice(EMOTES)} ᴘ ɪ ɴ ɢ ➫ {ping_time} ms
⁵┃ㅤ{random.choice(EMOTES)} ᴘ ʏ ᴛ ʜ ᴏ ɴ ➫ {pyrover}
ㅤ╚══════💫✨💫═════╝
ㅤ╔═════🇮🇳🇮🇳🇮🇳🇮🇳═════╗
⁶┃ {random.choice(EMOTES)} s ᴇ ɴ s ᴇ ɪ ➫ {user_hyperlink}
ㅤ╚═════🇮🇳🇮🇳🇮🇳🇮🇳═════╝"""

    return ALIVE_TEXT, photo_url
    

@PyroX.on_message(filters.command("ping", prefixes=HANDLER) & filters.me)
async def ping(_, message):
    start_time = time.time()
    await message.edit("✮ᑭｴƝG...✮")
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 3)
    uptime = get_readable_time((time.time() - StartTime))
    await message.edit(f"\ (•◡•) / **ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ**\n⋙ 🔔 **ᑭｴƝG**: {ping_time}\n⋙ ⬆️ **ⴑⲢⲦⲒⲘⲈ**: {uptime}")

__mod_name__ = "STATUS"  
    
__help__ = """  
- alive: to check bot on/off
- ping: check response of server
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
