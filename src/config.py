from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Config(BaseSettings):
    bot_token: str
    api_token: str
    api_url: str
