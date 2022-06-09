import re
import os
from os import environ


id_pattern = re.compile(r'^.\d+$')

PICS = os.environ.get("PICS", "https://telegra.ph/file/f1e190cc3cf92409ecefb.jpg").split()
