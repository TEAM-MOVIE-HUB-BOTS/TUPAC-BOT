import os
import io
from pyrogram import Client, filters
from pyromod import listen
from PIL import Image
from music_tag import load_file



@Client.on_message(filters.command("start"))
async def start_cmd(bot, message):
    await message.reply("Hi, {message.chat.first_name} iam Password Generator")




@Client.on_message(filters.private & filters.audio)
async def tag(bot, m):
    mes = await m.reply("`Downloading...`", parse_mode='md')
    await m.download(f"temp/{m.audio.file_name}.mp3")
    music = load_file(f"temp/{m.audio.file_name}.mp3")

    try:
        artwork = music['artwork']
        image_data = artwork.value.data
        img = Image.open(io.BytesIO(image_data))
        img.save("temp/artwork.jpg")
    except ValueError:
        image_data = None

    await mes.delete()
    fname = await bot.ask(m.chat.id,'`Send the Filename`', filters=filters.text, parse_mode='Markdown')
    title = await bot.ask(m.chat.id,'`Send the Title name`', filters=filters.text, parse_mode='Markdown')
    artist = await bot.ask(m.chat.id,'`Send the Artist(s) name`', filters=filters.text, parse_mode='Markdown')
    answer = await bot.ask(m.chat.id,'`Send the Artwork or` /skip', filters=filters.photo | filters.text, parse_mode='Markdown')
    music.remove_tag('artist')
    music.remove_tag('title')
    music['artist'] = artist.text
    music['title'] = title.text

    if answer.photo:
        await bot.download_media(message=answer.photo, file_name="temp/artwork.jpg")
        music.remove_tag('artwork')
        with open('temp/artwork.jpg', 'rb') as img_in:
            music['artwork'] = img_in.read()
    music.save()

    try:
        await bot.send_audio(chat_id=m.chat.id, file_name=fname.text, performer=artist.text, title=title.text, duration=m.audio.duration, audio=f"temp/{m.audio.file_name}.mp3", thumb='temp/artwork.jpg' if answer.photo or image_data else None)
    except Exception as e:
        print(e)
        return
    os.remove(f"temp/{m.audio.file_name}.mp3")
