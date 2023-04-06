import nfc_check as nc


def test_settings():
    assert nc.conf.dict() == {
        "app_name": "BoltRing - Authenticity Check",
        "logo_url": "/images/bolt-ring-logo.png",
        "vendor_key": "0" * 128,
    }
