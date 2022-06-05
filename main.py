from pyrogram import Client


PasswordBOT = Client(
    "Password BOT",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611",
    bot_token="5594929276:AAF6fGIGHNPZNBghjf_ABVxoVS4W1oFDYJg",
    plugins=dict(root="WEBPDFBOT")
)


PasswordBOT.run()
