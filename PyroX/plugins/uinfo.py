from config import HANDLER, OWNER_ID
from Barath import barath as app, MODULE
from config import HANDLER, OWNER_ID
from Barath import barath as app, MODULE
import os
from pyrogram import filters
from pyrogram.types import User, Message
from pyrogram.raw import functions
from pyrogram.errors import PeerIdInvalid

def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id

infotext = (
    "**[{full_name}](tg://user?id={user_id})**\n"
    " > UserID: `{user_id}`\n"
    " > First Name: `{first_name}`\n"
    " > Last Name: `{last_name}`\n"
    " > Username: {username}\n"
    " > DC: {dc_id}\n"
    " > Status: {status}\n"
    " > Is Scam: {scam}\n"
    " > Is Bot: {bot}\n"
    " > Is Verified: {verifies}\n"
    " > Is Contact: {contact}\n"
    " > Total Groups In Common: {common}"
)

def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name

@app.on_message(filters.command("whois", HANDLER) & filters.me)
async def whois(client, message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.reply("I don't know that User.")
        return
    common = await app.get_common_chats(user.id)

    # Get user profile picture
    pfp = None
    if user.photo:
        pfp = await user.download_profile_photo()

    await message.delete()
    await app.send_photo(
        message.chat.id,
        photo=pfp,
        caption=infotext.format(
            full_name=FullName(user),
            user_id=user.id,
            first_name=user.first_name,
            last_name=user.last_name or "",
            username=user.username or "",
            dc_id=user.dc_id or "1",
            status=user.status or "None",
            scam=user.is_scam,
            bot=user.is_bot,
            verifies=user.is_verified,
            contact=user.is_contact,
            common=len(common),
        ),
        reply_to_message_id=message.reply_to_message.message_id if message.reply_to_message else None,
    )

    # Clean up profile picture file if downloaded
    if pfp:
        os.remove(pfp)


@app.on_message(filters.command("id", HANDLER) & filters.me)
async def id(client, message):
    cmd = message.command
    chat_id = message.chat.id
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.edit("I don't know that User.")
        return
    text = "**User ID**: `{}`\n**Chat ID**: `{}`".format(user.id, chat_id)
    await message.edit(text)


__mod_name__ = "INFO"  
    
__help__ = """  
- info: user info
- id: get ids
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
