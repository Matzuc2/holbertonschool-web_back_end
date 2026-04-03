#!/usr/bin/env python3
import uuid
import bcrypt
from user import User
from db import DB
from sqlalchemy.exc import NoResultFound, InvalidRequestError


def _hash_password(password: str) -> bytes:
    """Hash user password and return it.

    Args:
        password: The plain text password to hash.

    Returns:
        The hashed password as bytes.
    """
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        """Initialize Auth instance with database connection."""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user in the database.

        Args:
            email: User email address.
            password: User password (plain text).

        Returns:
            The created User object.

        Raises:
            ValueError: If a user with that email already exists.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {user.email} already exists.")
        except NoResultFound:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email=email, hashed_password=hashed_pwd)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Validate user login credentials.

        Args:
            email: User email address.
            password: Plain text password to validate.

        Returns:
            True if credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            password_bytes = password.encode('utf-8')
            verif = bcrypt.checkpw(password_bytes, user.hashed_password)
            return verif
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """Generate a UUID for user session ID.

        Returns:
            A string representation of a UUID.
        """
        id1 = uuid.uuid1()
        id1_str = str(id1)
        return id1_str

    def create_session(self, email: str) -> str | None:
        """Create a session for a user using a generated UUID.

        Args:
            email: User email address.

        Returns:
            The session ID string, or None if user not found.
        """
        try:
            user = self._db.find_user_by(email=email)
            user_uid = self._generate_uuid()
            user.session_id = user_uid
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User | None:
        """Retrieve user by session ID.

        Args:
            session_id: The session ID to look up.

        Returns:
            The User object if found, None otherwise.
        """
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy user session by setting session_id to None.

        Args:
            user_id: The ID of the user whose session to destroy.
        """
        user = self._db.find_user_by(user_id=user_id)
        user.session_id = None
