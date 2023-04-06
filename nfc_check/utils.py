__all__ = ["normalize_uid"]


def normalize_uid(uid: str):
    """Normalize UID to format returned by Web NFC Api (lower case & colon separated)"""
    uid = uid.lower()
    return ":".join([uid[i : i + 2] for i in range(0, len(uid), 2)])
