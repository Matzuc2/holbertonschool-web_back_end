#!/usr/bin/env python3
"""Provide authentication helpers for user registration and sessions."""

import uuid
import bcrypt
from sqlalchemy.exc import NoResultFound
from typing import Optional

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hash a plain text password and return its bcrypt digest."""
    password_bytes = password.encode("utf-8")
    hashed_pwd = bcrypt.hashpw(password=password_bytes, salt=bcrypt.gensalt())
    return hashed_pwd


def _generate_uuid() -> str:
    """Generate and return a unique session identifier string."""
    return str(uuid.uuid4())

class Auth:
    """Handle authentication operations backed by the database layer."""

    def __init__(self) -> None:
        """Initialize the authentication service with a database instance."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user or raise an error when the email exists."""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {user.email} already exists.")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hashed_pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Return True when credentials match an existing user."""
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                return False
            password_bytes = password.encode('utf-8')
            verif = bcrypt.checkpw(password_bytes, user.hashed_password)
            if verif is False:
                return False
            if verif is True:
                return True
        except NoResultFound:
            return False


    def create_session(self, email: str) -> Optional[str]:
        """Create and persist a session id for a user identified by email."""
        try:
            user = self._db.find_user_by(email=email)
            user_uid = _generate_uuid()
            user.session_id = user_uid
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: Optional[str])\
            -> Optional[User]:
        """Retrieve user by session ID."""
        if not session_id:
            return None
        else:
            try:
                user = self._db.find_user_by(session_id=session_id)
                return user
            except NoResultFound:
                return None

    def destroy_session(self, user_id: int) -> None:
        """Invalidate the active session for the given user id."""
        self._db.update_user(user_id, session_id=None)
