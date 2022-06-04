from pyrogram import Client


PasswordBOT = Client(
    "Password BOT",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611",
    bot_token="5496896007:AAEQUBtUDtp5A_XTiPnloiceVRPBGVZ8smQ",
    plugins=dict(root="PasswordBot")
)


PasswordPDFBOT.run()
