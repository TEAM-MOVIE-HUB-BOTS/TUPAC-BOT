from pyrogram import Client, filters



@Huzain.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(
        f"Hi, {message.chat.first_name} !!\n\n"
        "My Name Is .Maude Apatow  🤗,  My Work Not Completed ❌ \n Owner By © @Movie_Hub_Lite 😅")
