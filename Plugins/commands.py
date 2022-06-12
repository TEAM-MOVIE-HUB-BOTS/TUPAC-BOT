from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import PICS, ADMIN
import random
from DB.db import insert, getid
import pymongo 

@Client.on_message(filters.command('start') & filters.private)
async def start_cmd(bot, message):
    insert(int(message.chat.id))
    await message.reply_chat_action("typing")
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻 My Name Is TuPc \nI Can Download Muisc From YouTube",
        reply_markup = InlineKeyboardMarkup( [[
            InlineKeyboardButton(text='🌼 Owner 🌼' url='github.com/Tupac-Owners')
            InlineKeyboardButton(text='🍀 Updates 🍀', url='t.me/Movie_Hub_Bots')
            ],[
            InlineKeyboardButton(text='👀 Help', callback_data='help'),
            InlinekeyboardButton(text='🤖 About', callback_data='about')  
            ]]
            )
        )


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(client, message):    
    msg = await client.send_message(chat_id=message.chat.id, text="weit.....")
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")
