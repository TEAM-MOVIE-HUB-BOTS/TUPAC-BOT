from pyrogram import Client, filters
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import QueryIdInvalid, FloodWait
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, InlineQuery, InlineQueryResultArticle, \
    InputTextMessageContent

from configs import Config
from tool import API_ANIME , API_PIRATEBAY, API_YTS , API_1337x 



TorrentBot = Client(session_name=Config.SESSION_NAME, api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)
DEFAULT_SEARCH_MARKUP = [
                    [InlineKeyboardButton("Search YTS", switch_inline_query_current_chat="!yts "),
                     InlineKeyboardButton("Go Inline", switch_inline_query="!yts ")],
                    [InlineKeyboardButton("Search ThePirateBay", switch_inline_query_current_chat="!pb "),
                     InlineKeyboardButton("Go Inline", switch_inline_query="!pb ")],
                    [InlineKeyboardButton("Search 1337x", switch_inline_query_current_chat=""),
                     InlineKeyboardButton("Go Inline", switch_inline_query="")],
                    [InlineKeyboardButton("Search Anime", switch_inline_query_current_chat="!a "),
                     InlineKeyboardButton("GO Inline", switch_inline_query_current_chat="!a ")],
                    [InlineKeyboardButton("Developer: @AbirHasan2005", url="https://t.me/AbirHasan2005")]
                ]

@Client.on_message(filters.command("search"))
async def start_handler(_, message: Message):
    try:
        await message.reply_text(
            text="Hello, I am Torrent Search Bot!\n"
                 "I can search Torrent Magnetic Links from Inline.\n\n"
                 "Made by @AbirHasan2005",
            disable_web_page_preview=True,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(DEFAULT_SEARCH_MARKUP)
        )
    except FloodWait as e:
        print(f"[{Config.SESSION_NAME}] - Sleeping for {e.x}s")
        await asyncio.sleep(e.x)
        await start_handler(_, message)



@Client.on_message(filters.command("start"))
async def start_cmd(bot, message):
    await message.reply("Hi")

