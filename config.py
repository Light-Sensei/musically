import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
if str(getenv("SESSION_NAME")).strip() == "1BVtsOKQBu7vtptuduE7330MVpF4A_C6hBRQK-DQvhR-Engb6aK0lUmIu-KBpXQaIEg2yf6ecNPGLWIlYU7ch6NxuRVzPER0-_GaRfFZ8vD0QtRYme6k8Ag4Gj-G7G7XQ93ZRM05tZDce67d20fAu_X8WY41OdzDlk6XmiSP2QkP_2xq9qFqI5TCxpc35z8TXT9il5nDjVicQYzP8YkMZzQu_CfN9GZljO3PprWWu2x_jd8d3t3iMsMsfzi-KJVQfxONW-VMK4oY60TyIHZPZPxoE9HfGLeRprz6Ob1BR-83JVn_2nm3QGGpnbtKoUxULcc9zc4R-Sfklw_2rOf2To0LSalNJkHA=":
    SESSION_NAME = str(None)
else:
    SESSION_NAME = str(getenv("SESSION_NAME"))

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5130078117:AAFHcD-KPRaupc4iWil9L6ulP6cuco0qfgw")
BOT_NAME = getenv("BOT_NAME", "@ShikimoriXrobot")

API_ID = int(getenv("API_ID", "10501678"))
API_HASH = getenv("API_HASH", "c28923c93d9f26ad3fa920972f3a989f")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Light Yagami")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@Yagami_Roito")
ALIVE_NAME = getenv("ALIVE_NAME", "Shikimori")
BOT_USERNAME = getenv("BOT_USERNAME", "ShikimoriXrobot")
OWNER_ID = getenv("OWNER_ID", "5330764294")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ShikimoriAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "ShikimoriXsupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ShikimoriXupdates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5132611794").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/b4990dc110e4b1565f4a6.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/b4990dc110e4b1565f4a6.jpg"")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/13e6b986e95d613905b42.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/3b626f0a8f33937378a14.jpg")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/3b626f0a8f33937378a14.jpg")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/086dceeee5388e37384a0.jpg")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/086dceeee5388e37384a0.jpg")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/562b4951e8f1d45e6e297.jpg")
HEROKU_MODE = getenv("HEROKU_MODE", None)
