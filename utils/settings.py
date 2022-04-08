from typing import Any

from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    bot_token: str
    base_url: str
    web_port: int = 443
    prefix_tg: str = "/tg"
    prefix_webhook: str = "/webhook"

    db_driver: str = None
    db_host: str = None
    db_port: int = 3306
    db_user: str = None
    db_pass: str = None
    db_name: str = None

    admins: list = []
    reply_max_tries = 5

    def __init__(self, **values: Any):
        super().__init__(**values)
        self.base_url = self.base_url.strip('/')
        self.prefix_tg = '/' + self.prefix_tg.strip('/')
        self.prefix_webhook = '/' + self.prefix_webhook.strip('/')

    webhook_url_cached: str = ""
    @property
    def webhook_url(self) -> str:
        if not self.webhook_url_cached:
            joined = '/'.join(s.strip('/') for s in (
                str(self.web_port),
                self.prefix_tg,
                self.prefix_webhook,
                self.bot_token
            )).replace('//', '/')
            base_url = self.base_url.strip('/')
            if "://" not in base_url:
                self.webhook_url_cached = f"https://{base_url}:{joined}"
            else:
                self.webhook_url_cached = f"{base_url}:{joined}"
        return self.webhook_url_cached


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
