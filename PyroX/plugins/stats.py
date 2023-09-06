from pyrogram import filters, enums
from PyroX import PyroX, MODULE
from pyrogram.types import Message
from pyrogram.enums import ChatType
import config

@PyroX.on_message(filters.command(["stats"], prefixes=config.HANDLER) & filters.me)
async def dialogstats_handler(_, m: Message):
    try:
        sent_message = await barath.send_message(m.chat.id, "Getting stats . . .", parse_mode=enums.ParseMode.MARKDOWN)

        bot = 0
        user = 0
        group = 0
        channel = 0
        stats_format = """
        • **STATS FOR:** {}
        🤖 • **BOTS:** {}
        👨 • **USERS:** {}
        🛡️ • **GROUPS:** {}
        ⚙️ • **CHANNELS:** {}
        **POWERED BY @sexy_dark**
        """

        async for x in barath.get_dialogs():
            if x.chat.type == ChatType.CHANNEL:
                channel += 1
            if x.chat.type == ChatType.BOT:
                bot += 1
            if x.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                group += 1
            if x.chat.type == ChatType.PRIVATE:
                user += 1

        await sent_message.edit_text(stats_format.format(me, bot, user, group, channel), parse_mode=enums.ParseMode.MARKDOWN)
    except Exception as e:
        print(e)
        await PyroX.send_message(m.chat.id, "Something went wrong in the stats command!")

__mod_name__ = "STATS"  
    
__help__ = """  
- stats: user stats
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
