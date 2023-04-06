from datetime import datetime
from blacksheep import Application
import nfc_check as nc

__all__ = ["app"]

app = Application()


@app.route("/")
def home():
    return f"{nc.conf.app_name}"
