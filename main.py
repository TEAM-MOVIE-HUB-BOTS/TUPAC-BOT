from pyrogram import Client


BOT = Client(
    "BOT",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611",
    bot_token="5471316306:AAF3-xjAAwxGnx34YBDI7mniE01Qe7CbcUI",
    plugins=dict(root="Plugins")
)


BOT.run()
