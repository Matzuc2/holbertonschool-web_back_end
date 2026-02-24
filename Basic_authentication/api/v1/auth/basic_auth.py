#!/usr/bin/env python3
"""
Basic Authentication module for the API.

This module provides the BasicAuth class that implements HTTP Basic
Authentication for the API endpoints. It extends the base Auth class
to provide Basic Authentication specific functionality.
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class for handling Basic Authentication.

    This class inherits from the Auth base class and implements
    HTTP Basic Authentication scheme. It will provide methods to:
    - Extract and decode Base64 authorization headers
    - Validate user credentials
    - Authenticate users based on email and password

    Attributes:
        Inherits all attributes from the Auth base class.

    Methods:
        Inherits all methods from the Auth base class.
        Additional methods will be implemented for Basic Authentication.
    """
    def extract_base64_authorization_header(self, authorization_header: str):
        """
        Extract the Base64 part of the Authorization header for base auth

        This method takes an Authorization header and extracts the
        Base64-encoded
        credentials portion after the "Basic " prefix.

        Args:
            authorization_header (str): The full
            Authorization header value
            (e.g., "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==").

        Returns:
            str: The Base64-encoded credentials string if valid,
                 None if the header is invalid, None, not a string,
                 or doesn't start with "Basic ".
            None
        """
        if not authorization_header:
            return None
        if type(authorization_header) is str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header.split(" ")[1]
