# Ā© Credit By VETRI Thanks You Bro š

from pyrogram import Client, filters
import youtube_dl
from youtube_search import YoutubeSearch
import requests
import os




@Client.on_message(filters.command(['song']))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('š šššš«šš”š¢š§š  š­š”š š¬šØš§š ...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            views = results[0]["views"]
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('ššØš®š§š ššØš­š”š¢š§š . šš«š² šš”šš§š š¢š§š  šš”š šš©šš„š„š¢š§š  š šš¢š­š­š„š š')
            return
    except Exception as e:
        m.edit(
            "āļø ššØš®š§š ššØš­š”š¢š§š . ššØš«š«š².\n\nšš«š² šš§šØš­š”šš« ššš²š°šØš«š¤ šš« ššš²šš šš©šš„š„ šš­ šš«šØš©šš«š„š².\n\nEg.`/song Look At Me`"
        )
        print(str(e))
        return
    m.edit("š šš¢š§šš¢š§š  š ššØš§š  š¶ šš„ššš¬š ššš¢š­ ā³ļø ššØš« ššš° ššššØš§šš¬ [š](https://telegra.ph/file/4c9d9362acd7ce6df0dc5.mp4)")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'š§ šš¢š­š„š : [{title[:35]}]({link})\nā³ šš®š«šš­š¢šØš§ : `{duration}`\nš¬ ššØš®š«šš : [Youtube]({link})\nšāšØ šš¢šš°š¬ : {views}\n\nPowered šš² : @Movie_Hub_Bots'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='md',quote=False, title=title, duration=dur, thumb=thumb_name)
        m.delete()
    except Exception as e:
        m.edit('ā šš«š«šØš«\n\n Report This Erorr To Fix @MoViE_HuB_BoTs ā¤ļø')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
