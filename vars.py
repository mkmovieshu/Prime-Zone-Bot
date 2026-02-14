import os
from typing import List

API_ID = int(os.getenv("API_ID", "20990520"))
API_HASH = os.getenv("API_HASH", "714a70d62fc73bf8ec1a5d38adf8f198")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8097946087:AAEfpDuN-N58XpSX-5diHKaqlnlfwM7zi_g")
MONGO_URI = os.getenv("MONGO_URI", "")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", ""))
ADMIN_ID = int(os.getenv("ADMIN_ID", ""))
PICS = (os.environ.get("PICS", "")).split()
LOG_CHNL = int(os.getenv("LOG_CHNL", ""))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "TechifyBots") # Without @
IS_FSUB = bool(os.environ.get("FSUB", False))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_LOG", ""))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "240"))
