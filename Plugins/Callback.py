from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio




@Client.on_callback_query()
async def callback(bot, msg):
   if data == "help":
       await msg.message.edit(       
           text=f"""HEY {message.from_user.mention}
<b><u>MY COMMANDS</u></b>
◉ /start - Check Bot Alive 
◉ /id - your tg id
◉ /Song - Type Your Song Name 
 ∆ example : `/song Dear Mama`

Powered By  @Movie_Hub_Bots
""",                
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("🤖 ABOUT", callback_data="about")
                  ],[
                  InlineKeyboardButton("↩️ GO BACK", callback_data="start"),
                  InlineKeyboardButton("🔒 CLOSE", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
Nothing More""",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("↩️ GO BACK", callback_data="start"),
                  InlineKeyboardButton("🔒 CLOSE", callback_data="close")
                  ]]
                  )
         )    
   elif data == "start":
         await msg.message.edit(
         text=f"Hello {message.from_user.mention}👋🏻\nMy Name Is Tupac\nI Can Download Muisc From YouTube",
         reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton(text='🤔 Help', callback_data='help'), InlineKeyboardButton(text='🤖 About', callback_data='about')], [InlineKeyboardButton(text='Close 🔒', callback_data='close')]])
)
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass

