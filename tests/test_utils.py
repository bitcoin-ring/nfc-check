import nfc_check as nc


def test_normalize_uid():
    uid = "5215fBDD756359"
    assert nc.normalize_uid(uid) == "52:15:fb:dd:75:63:59"
