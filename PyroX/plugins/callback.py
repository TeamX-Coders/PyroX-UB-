import strings

from PyroX import bot, MODULE, INFO as GET_INFO
from pyrogram import filters, enums 
from PyroX import PyroX 
from pyrogram.types import ( 
InlineKeyboardMarkup, InlineKeyboardButton )


@bot.on_callback_query(filters.regex("help_back"))
async def help_back(_, query):
    user_id = (await GET_INFO.PyroX()).id
    if not query.from_user.id == int(user_id):
        return await query.answer("😤 You aren't my master")
    
    buttons = []
    for x in MODULE:
        buttons.append(
            InlineKeyboardButton(x['module'], callback_data=f"help:{x['module']}")
        )

    # Organize buttons in two columns
    columns = 2
    buttons_in_columns = [buttons[i:i + columns] for i in range(0, len(buttons), columns)]

    keyboard = InlineKeyboardMarkup(buttons_in_columns)

    return await bot.edit_inline_text(
        inline_message_id=query.inline_message_id, 
        text="[`HELP COMMANDS`]", 
        reply_markup=InlineKeyboardMarkup(keyboard), 
        parse_mode=enums.ParseMode.MARKDOWN
    )

     

@bot.on_callback_query(filters.regex('^help'))
async def help_commnds(_, query):
   user_id = (await GET_INFO.PyroX()).id
   if not query.from_user.id == int(user_id):
       return await query.answer("😤 You aren't my master")
   CB_NAME = query.data.split(':')[1].casefold()
   data = [x for x in MODULE if x['module'].casefold() == CB_NAME]
   if len(data) == 0:
       return await query.answer("🤔 somthing wrong.")
   module = data[0]['module']
   help = data[0]['help']
   button = InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ BACK",callback_data="help_back")]])
   return await bot.edit_inline_text(inline_message_id=query.inline_message_id, text=strings.HELP_CMD.format(module=module, help=help), parse_mode=enums.ParseMode.MARKDOWN, reply_markup=button)
       
            
