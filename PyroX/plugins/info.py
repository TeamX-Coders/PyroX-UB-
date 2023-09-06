from pyrogram import filters

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


@PyroX.on_message(filters.command("info", prefixes=HANDLER) & filters.me)
async def info(_, m):
    m.reply_to_message
    if len(m.command) < 2:
        await m.reply_text("ɢɪᴠᴇ ᴍᴇ ɪᴅ")
        return
    id_user = m.text.split(" ")[1]
    msg = await m.reply_text("ɪɴғᴏʀᴍᴀᴛɪᴏɴ ɢᴀᴛʜᴇʀɪɴɢ!")
    info = await PyroX.get_chat(id_user)
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
