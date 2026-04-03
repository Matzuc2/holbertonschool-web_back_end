#!/usr/bin/env python3
"""Database access layer built on SQLAlchemy for user records."""

from typing import Any, Optional

from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """Provide helper methods to create, query, and update users."""

    def __init__(self) -> None:
        """Initialize the engine, recreate tables, and prepare the session."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Return a memoized SQLAlchemy session bound to the engine."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: bytes) -> User:
        """Create and persist a new user, then return that user object."""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs: Any) -> User:
        """Return the first user matching provided filters"""
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        else:
            return user

    def update_user(self, user_id: int, **kwargs: Any) -> None:
        """Update attributes of a user by id and commit the transaction."""
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
