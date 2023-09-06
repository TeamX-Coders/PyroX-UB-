import sys
import io

from subprocess import getoutput as run
import traceback

import config, strings
import asyncio

from pyrogram import filters, enums
from Barath import bot, INFO , barath
from Barath.helpers.help_func import emoji_convert
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import MessageTooLong

SPAM = []

async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


@bot.on_message(filters.command("start") & filters.private)
async def start(_, message):
     user_id = message.from_user.id
     info = await INFO.barath()
     botlive = await emoji_convert(bot.is_connected)
     applive = await emoji_convert(barath.is_connected)
     name = info.first_name
     id = info.id
     if user_id in SPAM:
         return await message.reply("[`DON'T SPAM HERE`]")
     SPAM.append(user_id)
     await message.forward(config.GROUP_ID)
     mention = f"[{name}](tg://user?id={id})"
     BUTTON=InlineKeyboardMarkup([[
     InlineKeyboardButton("SOURCE 👾", url=config.SOURCE),]])
     await message.reply_text(text=strings.BOT_START.format(mention=mention, applive=applive, botlive=botlive),quote=True, reply_markup=BUTTON ,parse_mode=enums.ParseMode.MARKDOWN)
     await asyncio.sleep(20)
     SPAM.remove(user_id)
     return 

@bot.on_message(filters.command("e"))
async def eval(client, message):

    msg = await message.reply("Analyzing Code...")

    try:
        cmd = message.text.split(message.text.split()[0])[1]
    except:
         return await msg.reply("can you input the code to run my program?")

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr

    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success ✅"

    final_output = "<b>🖥️ Code</b>: "
    final_output += f"<code>{cmd}</code>\n\n"
    final_output += "<b>📝 Results</b>:\n"
    final_output += f"<code>{evaluation.strip()}</code>\n"

    if len(final_output) > 4096:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.txt"
            await reply_to_.reply_document(
                document=out_file, caption=f'<code>{cmd}</code>', parse_mode=enums.ParseMode.HTML)
            return await message.delete()
    else:
        await reply_to_.reply_text(final_output, parse_mode=enums.ParseMode.HTML)
        return await message.delete()


@bot.on_message(filters.command("sh"))
async def sh(_, message):

    await message.reply("Analyzing Code...")
    
    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    try:
        code = message.text.split(message.text.split()[0])[1]
    except:
        return await message.edit("can you input the code to run my program?")

    x = run(code)

    try:

       await reply_to_.reply_text(f"**🖥️ Code**: ```{code}```\n\n**📝 Results**:\n```{x}```")
       return await message.delete()

    except MessageTooLong:
         with io.BytesIO(str.encode(run_logs)) as logs:
               logs.name = "shell.txt"

               await reply_to_.reply_document(
                   document=logs, thumb=thumb_id)

               return await message.delete()
