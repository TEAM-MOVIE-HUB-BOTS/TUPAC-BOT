from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import PICS
import random



@Client.on_message(filters.command('start') & filters.private)
async def start_cmd(bot, message):
    await message.reply_chat_action("typing")
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻 My Name Is TuPc \nI Can Download Muisc From YouTube",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("🍁Group🍁", url="https://t.me/"),
            InlineKeyboardButton("🍀Updates🍀", url="https://t.me/Movie_Hub_Bots")
            ]]
            )
