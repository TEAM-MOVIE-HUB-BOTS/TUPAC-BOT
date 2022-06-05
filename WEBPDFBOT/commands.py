from pyrogram import Client, filters
import os, re
import pyppdf
from pyppeteer.errors import PageError, NetworkError, TimeoutError


@Client.on_message(filters.command("start"))
async def start_cmd(bot, message):
    await message.reply("Hi, {message.chat.first_name} iam Password Generator")


@Client.on_message(filters.private & filters.text)
async def webtopdf(_, m):
    url = m.text
    name = re.sub(r'^\w+://', '', url.lower())
    name = name.replace('/', '-') + '.pdf'
    msg = await m.reply("Processing..")
    try:
        await pyppdf.save_pdf(name, url)
    except PageError:
        return await msg.edit('URL could not be resolved.')
    except TimeoutError:
        return await msg.edit('Timeout.')
    except NetworkError:
        return await msg.edit('No access to the network.')
    await m.reply_document(name)
    await msg.delete()
    os.remove(name)
