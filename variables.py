import re
import os
from os import environ


id_pattern = re.compile(r'^.\d+$')

PICS = os.environ.get("PICS", "https://telegra.ph/file/f1e190cc3cf92409ecefb.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '900873119').split()]

FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001675753014"))
