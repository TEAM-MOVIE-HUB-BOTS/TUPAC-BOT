import os
import shutil
from web_dl import urlDownloader
from pyrogram import Client, filters


@Client.on_message(filters.command("start"))
async def start_cmd(bot, message):
    await message.reply("Hi, {message.chat.first_name} iam Password Generator")


@Client.on_message(filters.private & filters.text & ~filters.regex('/start'))
async def webdl(_, m):

    if not m.text.startswith('http'):
        return await m.reply("the URL must start with 'http' or 'https'")

    msg = await m.reply('Processing..')
    url = m.text
    name = dir = str(m.chat.id)
    if not os.path.isdir(dir):
        os.makedirs(dir)

    obj = urlDownloader(imgFlg=True, linkFlg=True, scriptFlg=True)
    res = obj.savePage(url, dir)
    if not res:
        return await msg.edit('something went wrong!')

    shutil.make_archive(name, 'zip', base_dir=dir)
    await m.reply_document(name+'.zip')
    await msg.delete()

    shutil.rmtree(dir)
    os.remove(name+'.zip')
