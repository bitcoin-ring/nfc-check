# -*- coding: utf-8 -*-
import pytest
import nfc_check as nc


TEST_UID = "5215fbdd756359"
ENC_UID = "d91dca601be6e377d585277bc1022b8040b79393d07747"


def test_generate_key():
    key = nc.generate_key()
    assert isinstance(key, str)
    assert len(key) == 128
    assert len(bytes.fromhex(key)) == 512 / 8


def test_encrypt_uid():
    enc = nc.encrypt_uid(TEST_UID)
    assert enc == "d91dca601be6e377d585277bc1022b8040b79393d07747"


def test_encrypt_uid_invalid_hex():
    with pytest.raises(ValueError):
        nc.encrypt_uid("g215fbdd756359")


def test_encrypt_uid_invalid_hex_length():
    with pytest.raises(ValueError):
        nc.encrypt_uid("5215fbdd7563")


def test_decrypt_uid():
    dec = nc.decrypt_uid(ENC_UID)
    assert dec == TEST_UID


def test_decrypt_uid_invalid():
    token = "d91dca601be6e377d585277bc1022b8040b79393d07748"
    dec = nc.decrypt_uid(token)
    assert dec is None


def test_decrypt_uid_invalid_length():
    token = "d91dca601be6e377d585277bc1022b8040b79393d077"
    dec = nc.decrypt_uid(token)
    assert dec is None


def test_decrypt_uid_invalid_hex():
    token = "g91dca601be6e377d585277bc1022b8040b79393d07748"
    dec = nc.decrypt_uid(token)
    assert dec is None
