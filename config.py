from dataclasses import dataclass
from environs import Env

@dataclass
class DataBase:
    database: str

@dataclass
class TgBot:
    token: str
    
    
@dataclass
class Curency:
    url: str
    
@dataclass
class Config:
    tg_bot: TgBot
    curency: Curency
    database: DataBase
    
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(env('BOT_TOKEN')),
                  curency=Curency(url=env('URL')),
                  database=DataBase(database=env('DATABASE')))
    