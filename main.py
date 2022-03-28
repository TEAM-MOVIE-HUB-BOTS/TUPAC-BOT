from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Supermart=Client(
    "Supermart",
    bot_token="5001347153:AAHepqJMqzLySGbrfSYeUj2oHVp5fv6sfhw",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611"
)

@Supermart.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("Hi Man 😁")


Supermart.run()
