#!/usr/bin/env python3

"""User module for database models."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """User model for SQLAlchemy ORM.

    Attributes:
        id: User ID (primary key).
        email: User email address.
        hashed_password: Hashed user password.
        session_id: Current session ID.
        reset_token: Password reset token.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
