#!/usr/bin/env python3
"""Hello world"""

import uuid
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

    def _generate_uuid(self):
        """generates an uuid for user session id
        """

        id1 = uuid.uuid1()
        id1_str = str(id1)
        return id1_str

    def create_session(self, email) -> str:
        """create a session for an user, using the generated uuid
        """
        try:
            user = self._db.find_user_by(email=email)
            user_uid = self._generate_uuid()
            user.session_id = user_uid
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User | None:
        """Method to retrieve user by session_id, it uses find_user_by method
        """

        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """put session_id field to user at None
        """
        user = self._db.find_user_by(user_id=user_id)
        user.session_id = None
