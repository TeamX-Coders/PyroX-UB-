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


@PyroX.on_message(filters.command("id", prefixes=HANDLER) & filters.me)
async def id(_, m):
    reply = m.reply_to_message
    _reply = ""
    if not reply:
        no_reply = f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
        no_reply += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
        no_reply += f"**ᴍsɢ ɪᴅ**: `{m.id}`"
        await m.reply_text(text=(no_reply))
    if reply.from_user:
        _reply += f"**ʏᴏᴜʀ ɪᴅ**: `{m.from_user.id}`\n\n"
        _reply += f"**ʀᴇᴘʟɪᴇᴅ ɪᴅ**: `{reply.from_user.id}`\n\n"
        _reply += f"**ᴄʜᴀᴛ ɪᴅ**: `{m.chat.id}`\n\n"
        _reply += f"**ʀᴇᴘʟɪᴇᴅ ᴍsɢ ɪᴅ**: `{reply.id}`\n\n"
    if reply.sender_chat:
        _reply += f"\n\n**ᴄʜᴀɴɴᴇʟ  ɪᴅ**: `{reply.sender_chat.id}`\n\n"
    if reply.sticker:
        _reply += f"**sᴛɪᴄᴋᴇʀ ɪᴅ**: `{reply.sticker.file_id}`"
    elif reply.animation:
        _reply += f"**ᴀɴɪᴍᴀᴛɪᴏɴ ɪᴅ**: `{reply.animation.file_id}`"
    elif reply.document:
        _reply += f"**ᴅᴏᴄᴜᴍᴇɴᴛ ɪᴅ**: `{reply.document.file_id}`"
    elif reply.audio:
        _reply += f"**ᴀᴜᴅɪᴏ ɪᴅ**: `{reply.audio.file_id}`"
    elif reply.video:
        _reply += f"**ᴠɪᴅᴇᴏ ɪᴅ**: `{reply.video.file_id}`"
    elif reply.photo:
        _reply += f"**ᴘʜᴏᴛᴏ ɪᴅ**: `{reply.photo.file_id}`"
    await reply.reply_text(_reply)
    await m.delete()
