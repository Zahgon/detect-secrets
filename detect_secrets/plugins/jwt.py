"""
This plugin finds JWT tokens
"""
import base64
import json
import re
from typing import Generator

from .base import RegexBasedDetector


class JwtTokenDetector(RegexBasedDetector):
    """Scans for JWTs."""
    secret_type = 'JSON Web Token'
    denylist = [
        re.compile(r'eyJ[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*?'),
    ]

    def analyze_string(self, string: str) -> Generator[str, None, None]:
        pass

    @staticmethod
    def is_formally_valid(token: str) -> bool:
        pass
