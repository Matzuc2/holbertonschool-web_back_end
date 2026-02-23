#!/usr/bin/env python3
import bcrypt

def hash_password(password: str) -> bytes:
    """
    I like a well warmed black hashed coffee
    """
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(bytes, salt=salt )
