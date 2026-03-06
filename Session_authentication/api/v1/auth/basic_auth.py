#!/usr/bin/env python3
"""
Basic Authentication module for the API.

This module provides the BasicAuth class that implements HTTP Basic
Authentication for the API endpoints. It extends the base Auth class
to provide Basic Authentication specific functionality.
"""
from api.v1.auth.auth import Auth
from models.user import User
from models.base import Base
import base64


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
        Additional methods will be implemented for Basic Auth.
    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
    ) -> str:
        """
        Extract the Base64 part of the Authorization header.

        This method takes an Authorization header and extracts the
        Base64-encoded credentials portion after the "Basic " prefix.

        Args:
            authorization_header (str): The full Authorization header
                value (e.g., "Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==").

        Returns:
            str: The Base64-encoded credentials string if valid,
                 None if the header is invalid, None, not a string,
                 or doesn't start with "Basic ".
        """
        if not authorization_header:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
    ) -> str:
        """
        Decode a Base64-encoded authorization header.

        This method takes a Base64-encoded string and decodes it to
        retrieve the original credentials string (typically in the
        format "email:password").

        Args:
            base64_authorization_header (str): The Base64-encoded
                authorization string to decode.

        Returns:
            str: The decoded string containing the credentials if
                 successful, None if the input is invalid, not a
                 string, or if Base64 decoding fails.

        Examples:
            >>> decode_base64_authorization_header(
                    "QWxhZGRpbjpvcGVuIHNlc2FtZQ=="
                )
            "Aladdin:open sesame"
            >>> decode_base64_authorization_header(None)
            None
            >>> decode_base64_authorization_header("invalid_base64")
            None
        """
        if not base64_authorization_header:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            bytes_string64 = base64_authorization_header.encode(
                "utf-8"
            )
            bytes_string = base64.b64decode(bytes_string64)
            decoded = bytes_string.decode('utf-8')
            return decoded
        except Exception:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        allo alloallo
        """
        if not decoded_base64_authorization_header:
            return (None, None)
        elif type(decoded_base64_authorization_header) is not str:
            return (None, None)
        elif len(decoded_base64_authorization_header.split(":")) < 2:
            return (None, None)
        else:
            credentials = decoded_base64_authorization_header.split(":")
            email = credentials[0]
            password = credentials[1]
            return (email, password)

    def user_object_from_credentials(self, user_email: str, user_pwd: str):
        """
        hello world
        """
        if not user_email or type(user_email) is not str:
            return None
        if not user_pwd or type(user_pwd) is not str:
            return None
        User.load_from_file()
        found_users = User.search({"email": user_email})
        if len(found_users) == 0 or found_users is None:
            return None
        if not found_users[0].is_valid_password(user_pwd):
            return None
        return found_users[0]

    def current_user(self, request=None) -> User:
        """
        Retrieve the authenticated User instance for a request.

        This method orchestrates the complete Basic Authentication
        flow by:
        1. Extracting the Authorization header from the request
        2. Extracting the Base64 portion from the Authorization header
        3. Decoding the Base64 string to get credentials
        4. Parsing the credentials to extract email and password
        5. Validating the credentials against the database
        6. Returning the authenticated User object

        Args:
            request: The Flask request object containing the HTTP
                     request data. Defaults to None if not provided.

        Returns:
            User: The authenticated User object if credentials are
                  valid and the user exists in the database.
            None: If any step in the authentication process fails:
                  - Missing or invalid Authorization header
                  - Invalid Base64 encoding
                  - Invalid credential format
                  - User not found in database
                  - Invalid password

        Examples:
            >>> # Assuming a valid request with Basic Auth header
            >>> user = basic_auth.current_user(request)
            >>> print(user.email)
            'user@example.com'

            >>> # Invalid or missing auth header
            >>> user = basic_auth.current_user(request)
            >>> print(user)
            None

        Note:
            This method chains multiple authentication steps. If any
            step returns None, subsequent steps will also return None,
            providing a fail-safe authentication pipeline.
        """
        auth_header = self.authorization_header(request)
        b64_header = self.extract_base64_authorization_header(auth_header)
        credentials_string = self.decode_base64_authorization_header(
            b64_header
        )
        user_credentials = self.extract_user_credentials(
            credentials_string
        )
        user = self.user_object_from_credentials(
            user_credentials[0],
            user_credentials[1]
        )
        return user
