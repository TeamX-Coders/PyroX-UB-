
from Barath import barath as app
from config import HANDLER

from pyrogram import filters, errors

from Barath.barath_db.gmutedb import get_gmuted_users, gmute_user, ungmute_user
from Barath.helpers.help_func import get_arg
from Barath.helpers.utils import CheckAdmin


@app.on_message(filters.command("gmute", HANDLER) & filters.me)
async def gmute(_, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user.id
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I gmute?**")
            return
    get_user = await app.get_users(user)
    await gmute_user(get_user.id)
    await message.edit(f"**Gmuted {get_user.first_name}, LOL!**")


@app.on_message(filters.command("ungmute", HANDLER) & filters.me)
async def gmute(_, message):
    reply = message.reply_to_message
    if reply:
        user = reply.from_user.id
    else:
        user = get_arg(message)
        if not user:
            await message.edit("**Whome should I ungmute?**")
            return
    get_user = await app.get_users(user)
    await ungmute_user(get_user.id)
    await message.edit(f"**Unmuted {get_user.first_name}, enjoy!**")


@app.on_message(filters.group & filters.incoming)
async def check_and_del(client, message):
    if not message:
        return
    try:
        if not message.from_user.id in (await get_gmuted_users()):
            return
    except AttributeError:
        return
    message_id = message.message_id
    try:
        await app.delete_messages(message.chat.id, message_id)
    except errors.RPCError:
            pass  # you don't have 
