#!/usr/bin/env python3
import bcrypt


def _hash_password(password) -> bytes:
    """hash user password and returns it
    """

    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password=bytes, salt=salt)
    return hashed_pwd
