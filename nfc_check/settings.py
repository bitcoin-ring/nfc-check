# -*- coding: utf-8 -*-
from pydantic import BaseSettings, Field

__all__ = ["conf"]


class NfcCheckSettings(BaseSettings):
    app_name: str = Field("BoltRing - Authenticity Check")


conf = NfcCheckSettings()
