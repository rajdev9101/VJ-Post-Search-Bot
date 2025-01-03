# Don't Remove Credit Tg - @Rajdev21_bot
# Subscribe YouTube Channel For Amazing Bot https://youtub.com
# Ask Doubt on telegram @raj_dev21

from info import *
from pyrogram import Client

class Bot(Client):   
    def __init__(self):
        super().__init__(   
           "raj-post-search-bot",
            api_id=API_ID,
            api_hash=API_HASH,           
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})
    async def start(self):                        
        await super().start()  
        print("Bot Started 🔧 Powered By @raj_dev21")   
    async def stop(self, *args):
        await super().stop()
