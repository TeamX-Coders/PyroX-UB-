import asyncio
import requests
import wget
import yt_dlp
import config
import os

from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from pyrogram import filters
from pyrogram.types import *

from Barath import barath, MODULE
from config import HANDLER, OWNER_ID, BARATH

@barath.on_message(filters.command("video",prefixes=HANDLER) & filters.user(OWNER_ID))
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        me = await barath.get_me()
        msg = await message.reply("**wait sor 👌 processing**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **Error:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("**Process Complete.\n Now Uploading 🌝**")
    title = ytdl_data["title"]
    await message.reply_video(file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=f"{title}\n**Uploaded by {message.from_user.mention}**")
     
    await msg.delete()
    try:
        os.remove(file_name)
    except Exception as e:
        print(e)                                  

flex = {}
chat_watcher_group = 3

                       
ydl_opts = {
    "format": "best",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}        

@barath.on_message(filters.command("song",prefixes=HANDLER) & filters.user(OWNER_ID))
def download_song(_, message):
    query = " ".join(message.command[1:])  
    print(query)
    m = message.reply("**🔍**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("**⚠️ No results were found. Make sure you typed the information correctly**")
        print(str(e))
        return
    m.edit("**🧐 Downloading .. Your Request song sor w8**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**💀 Uploading .. For You sor w8**")

        message.reply_audio(
            audio_file,
            thumb=thumb_name,
            title=title,
            caption=f"{title}\n**Uploaded by {message.from_user.mention}**",
            duration=dur
        )
        m.delete()
    except Exception as e:
        m.edit(" - An error check logs again sor!!")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


__mod_name__ = "UTHOOB"  
    
__help__ = """  
- song: get a song from yt
- video: get video from yt
"""  
    
    
string = {"module": __mod_name__, "help": __help__}   
MODULE.append(string)
