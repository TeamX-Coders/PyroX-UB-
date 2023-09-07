import config 
import requests

from PyroX import PyroX 
from PyroX import MODULE, bot, INFO as GET_INFO
from PyroX.helpers.help_func import spacebin
from pyrogram import filters
from PyroX.plugins.alive import alive
from pyrogram.types import (
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultPhoto, 
)



@bot.on_inline_query(filters.regex("help"))
async def help_cmds(_, inline_query):
    user_id = (await GET_INFO.PyroX()).id
    if not inline_query.from_user.id == user_id:
        return

    buttons = []
    for x in MODULE:
        buttons.append(
            InlineKeyboardButton(x['module'], callback_data=f"help:{x['module']}")
        )

    # Organize buttons in two columns
    columns = 2
    buttons_in_columns = [buttons[i:i + columns] for i in range(0, len(buttons), columns)]

    keyboard = InlineKeyboardMarkup(buttons_in_columns)

    await bot.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            InlineQueryResultArticle(
                "🆘 HELP COMMANDS",
                InputTextMessageContent(message_text="[`HELP COMMANDS`]"),
                thumb_url="https://graph.org/file/b136511bda43b1d8db7d2.jpg",
                reply_markup=keyboard
            )
        ]
    )


@bot.on_inline_query(filters.regex("alive"))
async def alive_inline(_, inline_query):
    user_id = (await GET_INFO.PyroX()).id
    if not inline_query.from_user.id == user_id:
        return
     
    ALIVE_TEXT, photo_url = await alive()

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💫 𝗝𝗢𝗜𝗡 ✨", url="https://t.me/botupdatex"),
            ],
            [
                InlineKeyboardButton("🌝 𝗗𝗘𝗩'𝗦", url="https://t.me/Sexy_Dark"),
                InlineKeyboardButton("🌝 𝗗𝗘𝗩'𝗦", url="https://t.me/Siamkira"),
            ],
            [
                InlineKeyboardButton("❄️ 𝗢𝗪𝗡𝗘𝗥", url="https://t.me/tobiix"),
            ],
        ]
    )
 
    await bot.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            InlineQueryResultPhoto(  # Use InlineQueryResultPhoto
                title="🤖 Bot Status",
                caption=ALIVE_TEXT,  # Use caption for text content
                photo_url=photo_url,
                thumb_url="https://graph.org/file/b136511bda43b1d8db7d2.jpg",
                reply_markup=buttons,
            )
        ]
    )



@PyroX.on_message(filters.command("help", prefixes=".") & filters.me)
async def get_helpdex(_, message):
    user_id = (await GET_INFO.PyroX()).id
    if not message.from_user.id == user_id:
        return

    try:
        await message.edit("`. . .`",)
        result = await PyroX.get_inline_bot_results(
            PyroX.bot.username,
            "help"
        )

        if result:
            await message.delete()
            info = await PyroX.send_inline_bot_result(
                message.chat.id,
                query_id=result.query_id,
                result_id=result.results[0].id,
                disable_notification=True,
            )
    except Exception as e:
        print(f"Error: {e}")

@PyroX.on_message(filters.command("alive", prefixes=".") & filters.me)
async def alive_dex(_, message):
    user_id = (await GET_INFO.PyroX()).id
    if not message.from_user.id == user_id:
        return

    try:
        await message.edit("`. . .`")
        result = await PyroX.get_inline_bot_results(
            PyroX.bot.username,
            "alive"
        )

        if result:
            await message.delete()
            info = await PyroX.send_inline_bot_result(
                message.chat.id,
                query_id=result.query_id,
                result_id=result.results[0].id,
                disable_notification=True,
            )
    except Exception as e:
        print(f"Error: {e}")
