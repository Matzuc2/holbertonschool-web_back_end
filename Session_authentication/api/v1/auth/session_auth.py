#!/usr/bin/env python3
"""Session authentication module for the API."""
from api.v1.auth.auth import Auth
from uuid import uuid4
import uuid


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
