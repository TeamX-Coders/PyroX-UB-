from PyroX import PyroX, MODULE
from pyrogram import filters
from PyroX.PyroX_db.clone_db import store_profile, get_profile

import config

@PyroX.on_message(filters.command("cpfp",config.HANDLER) & filters.me)
async def clone(_, message):
    if not message.reply_to_message:
         try:
            clone_id = message.text.split(None,1)[1]
         except:
              return await message.edit("=> reply to the user either give a user id")
    else:
         clone_id = message.reply_to_message.from_user.id

    user_id = message.from_user.id
    
    if (await get_profile(user_id)) == False:
          return await message.edit_text("You didn't Saved Any Profile. Send ```.savepfp``` and try again.") 
           
          
    await message.edit('Collecting Information from Client')

    user = await PyroX.get_chat(clone_id)
    bio = user.bio if user.bio else None
    first_name = user.first_name
    photo_id = user.photo.big_file_id if user.photo else None

    try:
       profile = await PyroX.download_media(photo_id)
       await PyroX.set_profile_photo(photo=profile)
    except:
        pass
   
    await PyroX.update_profile(first_name=first_name, bio=bio)
    return await message.edit("✅ Successfully Implemented!")
    
    
    
@PyroX.on_message(filters.command("savepfp", config.HANDLER) & filters.me)
async def save_pfp(_, message):
      user_id = message.from_user.id
      await message.edit('Saving your information into DB')      
      user = await PyroX.get_chat(user_id)
      bio = user.bio if user.bio else None
      first_name = user.first_name 
      async for file in PyroX.get_chat_photos(user_id, limit=1):
             photo_id = file.file_id if user.photo else None
      await store_profile(user_id=user_id, profile=photo_id, first_name=first_name, bio=bio)
      return await message.edit("Successfully Saved!")
          
@PyroX.on_message(filters.command("rnpfp", config.HANDLER) & filters.me)
async def return_profile(_, message):
     user_id = message.from_user.id
     if (await get_profile(user_id)) == False:
         return await message.edit("Use ```.savepfp``` save your information and try again.")      
     user = await get_profile(user_id)
     bio = user.get("bio")
     first_name = user.get("first_name")
     photo_id = user.get("profile")
     try:
        profile = await PyroX.download_media(photo_id)
        await PyroX.set_profile_photo(photo=profile)
     except:
         pass

     await PyroX.update_profile(first_name=first_name, bio=bio)
     return await message.edit("Successfully Reseted Info!")


__mod_name__ = "CLONE"  
    
__help__ = """  
- savepfp: save profile to db
- cpfp: kang someone
- rnpfp: back to orginal
- note: do savepfp always when kanging
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)


