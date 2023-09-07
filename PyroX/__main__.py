import pyrogram
import strings
import config

from PyroX import bot , PyroX
from PyroX.helpers.help_func import get_datetime 

async def run_clients():
      await bot.start()
      await PyroX.start()
      await pyrogram.idle()
      zone = await get_datetime()
      await bot.send_message(
           chat_id=config.GROUP_ID,
           text=strings.RESTART_TEXT1.format(date=zone["date"], time=zone["time"]))
      await PyroX.send_message(
           chat_id=config.GROUP_ID,
           text=strings.RESTART_TEXT2.format(date=zone["date"], time=zone["time"]))


if __name__ == "__main__":
    PyroX.loop.run_until_complete(run_clients())
