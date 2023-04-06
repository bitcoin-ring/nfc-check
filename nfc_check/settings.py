# -*- coding: utf-8 -*-
from pydantic import BaseSettings, Field, constr


__all__ = ["conf"]


class NfcCheckSettings(BaseSettings):
    class Config:
        # environment variables will always take priority over values loaded from a dotenv file
        env_file = "env.example", ".env.test", ".env"  # .env takes priority
        env_file_encoding = "utf-8"

    vendor_key: constr(min_length=128, max_length=128)
    app_name: str = Field("BoltRing - Authenticity Check")
    logo_url: str = Field("/images/bolt-ring-logo.png")


conf = NfcCheckSettings()
