#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checking on the file path and authorization"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if path[-1] != "/":
            path = path + "/"

        for exclp in excluded_paths:
            if exclp[-1] == "*":
                exclp = exclp[0:-1]

            if exclp in path:
                return False

        if path not in excluded_paths:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """Method that handles authorization header"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Validates current user"""
        return None

    def session_cookie(self, request=None):
        """returns a cookie value from a request"""
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name)
