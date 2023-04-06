# -*- coding: utf-8 -*-
from typing import Optional
import nfc_check as nc
from loguru import logger as log
from cryptography.hazmat.primitives.ciphers.aead import AESSIV


__all__ = [
    "generate_key",
    "encrypt_uid",
    "decrypt_uid",
]


def generate_key() -> str:
    """Create a random vendor privaty key"""
    return AESSIV.generate_key(bit_length=512).hex()


def encrypt_uid(uid: str) -> str:
    """Encrypt UID with vendor key"""
    if not len(uid) == 14:
        raise ValueError(f"Invalid UID length {len(uid)}")
    key = bytes.fromhex(nc.conf.vendor_key)
    uid_data = bytes.fromhex(uid)
    encryptor = AESSIV(key)
    uid_encrypted = encryptor.encrypt(uid_data, None)
    return uid_encrypted.hex()


def decrypt_uid(ciphertext: str) -> Optional[str]:
    """Decrypt vendor encrypted UID or None on failure."""
    key = bytes.fromhex(nc.conf.vendor_key)

    try:
        data = bytes.fromhex(ciphertext)
    except ValueError:
        log.error(f"Failed hex decoding {ciphertext}")
        return None

    decryptor = AESSIV(key)

    try:
        uid = decryptor.decrypt(data, None)
    except Exception as e:
        log.error(f"Failed decrypting {ciphertext} with {e}")
        return None
    return uid.hex()
