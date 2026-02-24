from flask import request
from models import user
class Auth():


    def require_auth(self, path: str, excluded_paths: list[str]) -> bool:
        return False
    

    def authorization_header(self, request=None) -> str:
        return None
    

    def current_user(self, request=None) -> user.User:
        return None
