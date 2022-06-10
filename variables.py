import re
import os
from os import environ


id_pattern = re.compile(r'^.\d+$')

PICS = os.environ.get("PICS", "https://telegra.ph/file/78e7dd10ae3006381c951.jpg").split()
