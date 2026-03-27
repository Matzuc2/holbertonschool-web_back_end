#!/usr/bin/env python3
"""Session authentication module for the API."""
from api.v1.auth.auth import Auth
from uuid import uuid4

from models.user import User


class SessionAuth(Auth):
    """Session-based authentication class."""

    user_id_by_session_id: dict = {}

    def create_session(self, user_id: str = None) -> str:
        """Create and store a session ID for a user ID."""

        if not user_id:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a user ID based on a session ID."""

        if not session_id:
            return None
        if not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Return the current user based on the request session cookie."""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """Delete a user session and return operation status."""

        if not request:
            return False
        if not self.session_cookie(request):
            return False

        session_id = self.session_cookie(request)
        print(session_id)
        if not self.user_id_for_session_id(session_id):
            return False
        self.user_id_by_session_id.pop(session_id)
        return True
        