from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.error import UserNotParticipant

force_channel = "Bookanu"

Supermart=Client(
    "Supermart",
    bot_token="5001347153:AAHepqJMqzLySGbrfSYeUj2oHVp5fv6sfhw",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611"
)

@Supermart.on_message(filters.command("start"))
async def start_message(bot, message):
    if force_channel:
        try:
            user = await bot.get_chat_member(force_channel, message.from_user.id)
            if user.status == "kicked out":
                await message.reply_text("I'm sorry ☹️ , you banned")
                return
         expect UserNotParticipant:
             await message.reply_text(
                  text="Your not Subscribe My Channel ✨",
                  reply_markup=InlineKeyboardMarkup( [[
                   InlineKeyboardBotton("💖 SUBSCRIBE NOW 💖", url=f"t.me/{force_channel}")
                   ]]
                  )
             )





    await message.reply_text("Hi Man 😁")


Supermart.run()
