from os import getenv
from dotenv import load_dotenv
from core.config import Settings

load_dotenv(getenv(".env"))

settings = Settings()
