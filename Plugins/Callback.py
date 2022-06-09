from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio




@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""HEY {message.from_user.mention}
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
             disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("↩️ GO BACK", callback_data="start"),
                  InlineKeyboardButton("🔒 CLOSE", callback_data="close")
                  ]]
                  )
         )        
