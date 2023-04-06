import os

from blacksheep import Application
from blacksheep.server.templating import use_templates
from jinja2 import PackageLoader
import nfc_check as nc
import pathlib


HERE = pathlib.Path(__file__).parent.absolute()

__all__ = ["app"]

app = Application()

app.serve_files(f"{HERE}/images", root_path="images")
view = use_templates(app, loader=PackageLoader("nfc_check", "templates"))


@app.route("/")
def home():
    context = dict(
        app_name=nc.conf.app_name,
        logo_url=nc.conf.logo_url,
        uid=nc.normalize_uid(os.urandom(7).hex()),
    )
    return view("check", context)


@app.route("/{token}")
def check(token: str):
    uid = nc.decrypt_uid(token) or os.urandom(7).hex()
    uid = nc.normalize_uid(uid)
    context = dict(app_name=nc.conf.app_name, logo_url=nc.conf.logo_url, uid=uid)
    return view("check", context)
