#!/usr/bin/env python3
import logging

"""
Filtered logger module
"""

import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
    ) -> str:
        """[summary]
        Args:
            fields: (List[str])
            redaction: str
            message: str
            separator: str
        Returns:
            str: log message obfuscated
        """
        for item in fields:
            message = re.sub(
                rf"{item}=.+?{separator}",
                f"{item}={redaction}{separator}",
                message,
            )
        return message
