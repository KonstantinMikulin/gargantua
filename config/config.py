from dataclasses import dataclass

from environs import Env


@dataclass
class TgBotConfig:
    token: str
    admins_ids: list[int]
    support_ids: list[int]
    users_ids: list[int]
    
    
@dataclass
class Config:
    tg_bot: TgBotConfig
    
    
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    
    return Config(
        tg_bot=TgBotConfig(
            token=env('BOT_TOKEN'),
            admins_ids=list(map(int, env.list('ADMIN_IDS'))),
            support_ids=list(map(int, env.list('SUPPORT_IDS'))),
            users_ids=list(map(int, env.list('USERS_IDS')))
        )
    )
