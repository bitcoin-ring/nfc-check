from datetime import datetime
from blacksheep import Application
import nfc_check as nc
import pathlib


HERE = pathlib.Path(__file__).parent.absolute()

__all__ = ["app"]

app = Application()

app.serve_files(f"{HERE}/images", root_path="images")


@app.route("/")
def home():
    return f"{nc.conf.app_name}"
