import asyncio
from pyrogram.types import Message
from pyrogram import filters
from PyroX import PyroX, MODULE
import config

@PyroX.on_message(filters.command(["ds"], prefixes=config.HANDLER) & filters.me)
async def delay_handler(_, m: Message):
    try:
        reply = m.reply_to_message
        cmd = m.command

        if len(m.command) < 3:
            await PyroX.send_message(m.chat.id, f"Use like this: `.dspam [count spam] [delay time in seconds] [text messages]`")

        elif len(m.command) > 2 and not reply:
            await m.delete()
            msg = m.text.split(None, 3)
            times = int(msg[1]) if msg[1].isdigit() else None
            sec = int(msg[2]) if msg[2].isdigit() else None
            text = msg[3]
            for x in range(times):
                await barath.send_message(
                    m.chat.id,
                    text
                )
                await asyncio.sleep(sec)
        else:
            await PyroX.send_message(m.chat.id, "Something wrong in spam command !")
    except Exception as e:
        print(e)  # Print the error to the console for debugging purposes


# For spam command Made by @daanav_asura

@PyroX.on_message(filters.command(["spam"], prefixes=config.HANDLER) & filters.me)
async def spam_handler(_, m: Message):
    try:
        reply = m.reply_to_message
        reply_to_id = reply.message_id if reply else None
        cmd = m.command

        if not reply and len(cmd) < 2:
            await PyroX.send_message(m.chat.id, f"Use like this: .spam [count spam] [text messages]")
            return

        if not reply and len(cmd) > 1:
            await m.delete()
            times = int(cmd[1]) if cmd[1].isdigit() else None
            text = " ".join(cmd[2:]).strip()
            if not text:
                await PyroX.send_message(m.chat.id, "The spam text cannot be empty.")
                return

            for x in range(times):
                await PyroX.send_message(
                    m.chat.id,
                    text
                )
                await asyncio.sleep(0.10)

        elif reply:
            await m.delete()
            times = int(cmd[1]) if cmd[1].isdigit() else None
            for x in range(times):
                await PyroX.copy_message(
                    m.chat.id,
                    m.chat.id,
                    reply.message_id
                )
    except Exception as e:
        print(e)  # Print the error to the console for debugging purposes

__mod_name__ = "SPAM"  
    
__help__ = """  
- spam: spam message
- ds: spam with time
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
