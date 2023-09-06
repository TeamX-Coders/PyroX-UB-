from Barath import barath, MODULE
from config import OWNER_ID, HANDLER
import os
from pyrogram import filters


async def FileType(message):
    if message.document:
        type = message.document.mime_type
        return ["txt" if type == "text/plain" else type.split("/")[1]][0]
    elif message.photo:
          return "jpg"
    elif message.animation:
          return message.animation.mime_type.split("/")[1]
    elif message.video:
         return message.video.mime_type.split("/")[1]
    else:
         return False

@barath.on_message(filters.command("rename",prefixes=HANDLER) & filters.user(OWNER_ID))
async def rename(_, message):
    try:
       filename = message.text.split(None,1)[1]
    except:
        name = "Barath"
        try:
          if (await FileType(message=message.reply_to_message)) != False:
               filetype = await FileType(message=message.reply_to_message)
        except Exception as e:
               return await message.reply_text(f"Error: `{e}`")
        filename = "{name}.{filetype}".format(name=name, filetype=filetype)
    msg = await message.reply_text("⬇️ File has downloading...")
    path = await message.reply_to_message.download(file_name=filename)
    thumb_id = "./Barath/barath_img/IMG_20230503_093609_915.jpg"
    await msg.edit_text("⬆️ File has uplaoding")
    await message.reply_document(document=path, thumb=thumb_id)
    await msg.delete()
    os.remove(path)
    return 
    
    
    
__mod_name__ = "RENAME"  
    
__help__ = """  
- rename: rename any file 
- note: upload speed may be slow
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
