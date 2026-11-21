# 读取.env
from pydantic_settings import BaseSettings,SettingsConfigDict
from pathlib import Path

Base_Dir = Path(__file__).resolve().parent.parent # resolve.()将当前文件路径转换为绝对路径

# 定义Setting类以读取各种.env中的配置
class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str
    JWT_EXPIRE_HOURS: int
    JWT_ALGORITHM: str

    model_config = SettingsConfigDict(
        env_file=Base_Dir/'.env',   #
        env_file_encoding='utf-8'
    )

settings = Settings()