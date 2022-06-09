import re
import os
from os import environ

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMIN', '1467649219').split()]
