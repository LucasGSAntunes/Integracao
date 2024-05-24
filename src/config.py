from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict 
import os

load_dotenv()

class Settings(BaseSettings):
    API_VERSION: str = "1.0.0"
    