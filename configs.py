import os


class Config(object):
    SESSION_NAME = os.environ.get("SESSION_NAME")
    API_ID = os.environ.get("8406611",)
    API_HASH = os.environ.get("5820bc246505e0ff60af5391d649f9a6")
    BOT_TOKEN = os.environ.get("5471316306:AAF3-xjAAwxGnx34YBDI7mniE01Qe7CbcUI")
    MAX_INLINE_RESULTS = os.environ.get("50",)
