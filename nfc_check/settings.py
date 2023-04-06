# -*- coding: utf-8 -*-
from pydantic import BaseSettings, Field

__all__ = ["conf"]


class NfcCheckSettings(BaseSettings):
    app_name: str = Field("BoltRing - Authenticity Check")
    logo_url: str = Field("/images/bolt-ring-logo.png")


conf = NfcCheckSettings()
