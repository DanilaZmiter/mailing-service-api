from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field

PATH: Path = Path(__file__).parent.parent  # need to have an correct path of project


class DBConfig(BaseModel):
    """class that storage .env arguments for database"""

    HOST: str
    NAME: str
    PASSWORD: str
    USER: str
    PORT: int

    def get_url(self) -> str:
        """method to get url like string from .env file"""
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.NAME}"


class Config(BaseSettings):
    db: DBConfig = Field(
        init=False
    )  # BaseSettings automatically take env arguments form .env/ init false because pylance is swearing
    DEBUG: bool = False  # True if need to debug of project

    model_config = SettingsConfigDict(  # class that configurate BaseSettings class
        env_file=f"{PATH}/.env",
        env_nested_delimiter="__",  # configuration: where take .env file, and delimeter for db arguments
    )


config = Config()  # need to import in different methods and use .env arguments
