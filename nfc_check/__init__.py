import importlib.metadata

__version__ = importlib.metadata.version("nfc_check")

from nfc_check.settings import *
from nfc_check.server import *
