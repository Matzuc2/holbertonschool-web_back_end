#!/usr/bin/env python3

"""DB module."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound
from user import Base, User


class DB:
    """DB class to interact with the database."""

    def __init__(self) -> None:
        """Initialize a new DB instance."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object.

        Returns:
            The SQLAlchemy session instance.
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: bytes) -> User:
        """Add a new user to the database.

        Args:
            email: User email address.
            hashed_password: Hashed password as bytes.

        Returns:
            The created User object.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """Find a user by filter criteria.

        Args:
            **kwargs: Field-value pairs to filter by.

        Returns:
            The User object matching the criteria.

        Raises:
            NoResultFound: If no user matches the criteria.
        """
        user = self._session.query(User).filter_by(**kwargs).first()
        if not user:
            raise NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update user fields by user ID.

        Args:
            user_id: The ID of the user to update.
            **kwargs: Field-value pairs to update.

        Raises:
            ValueError: If an invalid field is provided.
        """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
