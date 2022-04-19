from typing import Any, Dict

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

    fiat_config = {
        "deposit_interest": "3.50%",  # Наличными в Москве
        "withdraw_interest": "3.50%",
        "min_sum_deposit": "350'000",
        "min_sum_withdraw": "350'000",
        "deposit_rate": "98.00",  # Онлайн по курсу 1 USD = руб
        "withdraw_rate": "75.00",
        "min_sum_bank": "30000",
        "deposit_stablecoins": "0%",
        "withdraw_stablecoins": "2%",
        "binance": "0.75%",
    }

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
