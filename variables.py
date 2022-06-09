import re
import os
from os import environ


id_pattern = re.compile(r'^.\d+$')

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '1467649219').split()]

PICS = os.environ.get("PICS", "https://telegra.ph/file/f1e190cc3cf92409ecefb.jpg").split()
