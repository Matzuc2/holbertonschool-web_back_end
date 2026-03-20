#!/usr/bin/env python3
"""Session authentication module for the API."""
from api.v1.auth.auth import Auth
from uuid import uuid4
import uuid
from api.v1.views import app_views

from models.user import User


class SessionAuth(Auth):
    """Session-based authentication class."""

    user_id_by_session_id: dict = {}

    def create_session(self, user_id: str = None) -> str:
        """comment"""

        if not user_id:
            return None
        if type(user_id) is not str:
            return None
        else:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """hello world"""

        if not session_id:
            return None
        if type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Hello friends"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)
        user = User.get(user_id)
        return user
