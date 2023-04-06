# -*- coding: utf-8 -*-
import nfc_check as nc


def genkey():
    print(nc.generate_key())


if __name__ == "__main__":  # pragma: no cover
    genkey()
