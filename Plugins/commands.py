from pyrogram import Client, filters



@Client.on_message(filters.command("start"))
async def start_cmd(bot, message):
    await message.reply(f""Hi, {message.chat.first_name}")

