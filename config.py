import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

PICS = environ.get("PICS", "https://telegra.ph/file/78e7dd10ae3006381c951.jpg").split()

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '1467649219').split()]
       
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Tupac:Tupac@cluster19.plwjb.mongodb.net/?retryWrites=true&w=majority")
