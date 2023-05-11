#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authorithation"""
        if (
            path is None
            or excluded_paths is None
            or not len(excluded_paths)
        ):
            return True
        if path[-1] != "/":
            path += "/"
        for i in excluded_paths:
            if i.endswith("*"):
                if path.startswith(i[:1]):
                    return False
        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """Method that handles authorization header"""
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar("User"):
        """Validates current user"""
        return None
