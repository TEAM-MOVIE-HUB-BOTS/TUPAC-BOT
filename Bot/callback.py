from pyrogram import Client, filters
from pyrogram.types import CallbackQuery

@Bot.on_Callback_Query()
async def cb(bot, msg):
    if msg.data == "start":
     await msg.message_edit("hi")
