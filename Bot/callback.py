from pyrogram import Client, filters


@Client.on_callback_Query()
async def cb(bot, msg):
    if msg.data == "start":
     await msg.message_edit("hi")
