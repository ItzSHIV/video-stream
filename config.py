import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "KuramaRobot")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Narutoo06")
ALIVE_NAME = getenv("ALIVE_NAME", "KuramaRobot")
BOT_USERNAME = getenv("BOT_USERNAME", "Kurama9T_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "KuramaMusicAssistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "Kurama_sumpport_groump")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Kurama_sumpport_groump")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/ec8a5cf6ae48516bc352d.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/ab008e2712123d0bf5209.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/a2f9ef0a51907c7a278c9.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/5301814e2e4d97afb7ca7.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/ec8a5cf6ae48516bc352d.jpg")
