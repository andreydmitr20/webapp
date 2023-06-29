import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    bot_name = os.getenv("bot_name")
    bot_username = os.getenv("bot_username")
    bot_token = os.getenv("bot_token")


config = Config()


def l(a):
    print(a)
