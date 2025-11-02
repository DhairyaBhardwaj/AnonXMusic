# Copyright (c) 2025 AnonymousX1025
# Licensed under the MIT License.
# This file is part of AnonXMusic

from dotenv import load_dotenv
load_dotenv()
import os

needed = ["API_ID", "API_HASH", "BOT_TOKEN", "LOGGER_ID", "MONGO_URL", "OWNER_ID", "SESSION"]
for n in needed:
    if not os.getenv(n):
        print(f"❌ Missing variable: {n}")
    else:
        print(f"✅ Loaded: {n}")

import time
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s: %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=10485760, backupCount=5),
        logging.StreamHandler(),
    ],
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("ntgcalls").setLevel(logging.CRITICAL)
logging.getLogger("pymongo").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)


__version__ = "3.0.1"

from config import Config

config = Config()
config.check()
tasks = []
boot = time.time()

from anony.core.bot import Bot
app = Bot()

from anony.core.dir import ensure_dirs
ensure_dirs()

from anony.core.userbot import Userbot
userbot = Userbot()

from anony.core.mongo import MongoDB
db = MongoDB()

from anony.core.lang import Language
lang = Language()

from anony.core.telegram import Telegram
from anony.core.youtube import YouTube
tg = Telegram()
yt = YouTube()

from anony.helpers import Queue
queue = Queue()

from anony.core.calls import TgCall
anon = TgCall()
