from pyrogram import Client


BOT = Client(
    "BOT",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611",
    bot_token="5430545854:AAGBLsx58DvJ2kvnQed3cAp0aoO12E5adw0",
    plugins=dict(root="Plugins")
)


BOT.run()
