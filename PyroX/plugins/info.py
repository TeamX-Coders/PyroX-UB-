from pyrogram import filters
from pyrogram.types import Message
from config import HANDLER
from PyroX import PyroX



no_reply_user = """ ╒═══「 Appraisal results:」

**ɪᴅ**: `{}`
**ᴅᴄ**: `{}`
**ғɪʀsᴛ ɴᴀᴍᴇ**: {}
**ᴜsᴇʀɴᴀᴍᴇ**: @{}
**ᴘᴇʀᴍᴀʟɪɴᴋ**: {}
**ᴜsᴇʀʙɪᴏ**: {}

**Meet Me Here🙈 @sexy_dark ✨🥀**
"""


@PyroX.on_message(filters.command("info", prefixes=HANDLER) & (filters.me | filters.reply), group=1)
async def info(_, m: Message):
    if m.reply_to_message:
        user_id = m.reply_to_message.from_user.id
    elif len(m.command) >= 2:
        user_id = m.text.split(" ")[1]
    else:
        await m.reply_text("ɢɪᴠᴇ ᴍᴇ ɪᴅ")
        return
    
    msg = await m.reply_text("ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀɪɴɢ!")
    info = await PyroX.get_chat(user_id)
    
    if info.photo:
        file_id = info.photo.big_file_id
        photo = await PyroX.download_media(file_id)
        user_id = info.id
        first_name = info.first_name
        username = info.username
        user_bio = info.bio
        dc_id = info.dc_id
        user_link = f"[link](tg://user?id={user_id})"
        await m.reply_photo(
            photo=photo,
            caption=no_reply_user.format(
                user_id, dc_id, first_name, username, user_link, user_bio
            ),
        )
    elif not info.photo:
        user_id = info.id
        first_name = info.first_name
        username = info.username
        user_bio = info.bio
        dc_id = info.dc_id
        user_link = f"[link](tg://user?id={user_id})"
        await m.reply_text(
            text=no_reply_user.format(
                user_id, dc_id, first_name, username, user_link, user_bio
            )
        )
    await msg.delete()
