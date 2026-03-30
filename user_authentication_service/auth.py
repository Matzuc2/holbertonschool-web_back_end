#!/usr/bin/env python3
import bcrypt
from user import User
from db import DB
from sqlalchemy.exc import NoResultFound, InvalidRequestError


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
        """Register a user in db
        """

        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {user.email} already exists.")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hashed_pwd)
            return user

    def valid_login(self, email, password) -> bool:
        try:
            user = self._db.find_user_by(email=email)
            password_bytes = password.encode('utf-8')
            verif = bcrypt.checkpw(password_bytes, user.hashed_password)
            return verif
        except NoResultFound:
            return False
