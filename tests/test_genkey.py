# -*- coding: utf-8 -*-
from nfc_check.genkey import genkey


def test_genkey(capsys):
    genkey()
    captured = capsys.readouterr()
    key = captured.out.strip()
    assert len(key) == 128
    assert len(bytes.fromhex(key)) == 512 / 8
