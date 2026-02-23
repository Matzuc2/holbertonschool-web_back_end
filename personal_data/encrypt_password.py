#!/usr/bin/env python3
"""
Module for password encryption using bcrypt.

This module provides utilities to securely hash and validate passwords
using the bcrypt hashing algorithm.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a randomly generated salt.

    Uses bcrypt's secure hashing algorithm to create a salted hash of the
    provided password. The salt is automatically generated and embedded
    in the returned hash.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The hashed password as a byte string, including the salt.

    Example:
        >>> hashed = hash_password("my_secret_password")
        >>> isinstance(hashed, bytes)
        True
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt=salt)

def is_valid(hashed_password, password) -> bool:
    password_bytes = password.encode('utf-8')
    pwd_bool = bcrypt.checkpw(password_bytes, hashed_password)
    return pwd_bool