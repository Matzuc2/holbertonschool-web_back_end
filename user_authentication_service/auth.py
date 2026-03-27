#!/usr/bin/env python3
import bcrypt
from user import User
from db import DB


def _hash_password(password) -> bytes:
    """hash user password and returns it
    """

    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password=bytes, salt=salt)
    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email, password) -> User:
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {user.email} already exists.")
        else:
            hashed_pwd = _hash_password(password)
            self._db.add_user(email=email, hashed_password=hashed_pwd)
            return user
