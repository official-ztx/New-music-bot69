import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", 23028479))
API_HASH = getenv("API_HASH", "c1e6a93b04c0810a5c282d8d8d44ea6f")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6981997419:AAErPDMGUxxcXbiHkmBjw98X15NThOTK0Wg")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://GOKU:MISSBHOPALI@goku.pzzsl8d.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 777777))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002186923374))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 7089408502))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/arindam69x/New-music-bot69",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ztx_org")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Anime_Chat_Group_International")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "df4340d7535741cf945b1848c20c2fd8")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "5bec438b8cb4495dac757db614c51494")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFfYv8AD2eqkTo8RlXMZiJ3Bet0JcugOeiGSVQePJCqPNbw4zbXeASKv0saZ6RnQ79m8jRAd-A5yi4IdZBRYJ96_MMnyH9uWObH4kVyQnyVxwgQMPr30UerPVS-NjfoNhweie3g-qXkPThfSlnzyJHDRwvWyZje6kQB_kDn4c24ZGOXeVSSBjV_R6GBeIm1yqeSELJx-OiA0bL4su8BZD8P8nxWDvnTGEkHcicX1RdNYGwl5ifKcEoOOXiQd6tw6XT1sbARes19YAnkKUDRDDwfHoMN8faJg98JwbDAZ0RDnDCDL0H6kKnspH3hlMevf4nlPW-5N2ncaRun2gi22lPwbWVDBgAAAAG2CnSXAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/233a442487ff4b2e6df0e.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/a7d42ce0f4aeb2449b2ca.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph//file/77ba78d195c2e26de2d32.jpg"
STATS_IMG_URL = "https://telegra.ph/file/8fcc411b17f865d183267.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph//file/a64b601cce0f45a192ce1.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph//file/37f24422832e727ebf478.jpg"
STREAM_IMG_URL = "https://telegra.ph//file/7c896988bd3d0b91b8e46.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph//file/1df85370be3f13663a2d9.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph//file/38124ca6dea236fb7e4ef.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph//file/adf5178b6e62a11b2c402.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph//file/9a258a9e3c9c3b6f61169.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph//file/b3b2e9a46166f3ee1a5cf.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
