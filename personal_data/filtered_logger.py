#!/usr/bin/env python3
"""
Filtered logger module
"""

import re
import logging
from typing import List
import logging

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """returns the log message obfuscated"""
    for item in fields:
        message = re.sub(
            rf"{item}=.+?{separator}",
            f"{item}={redaction}{separator}",
            message,
        )
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = (
        "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    )
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Filters values in incoming log records using filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)

    def get_logger() -> logging.Logger:
        ''' Description: Implement a get_logger function that takes no arguments and returns a logging.Logger object.
        '''
        log = logging.getLogger('user_data')
        log.setLevel(logging.INFO)
        log.propagate = False

        sh = logging.StreamHandler()
        formatter = RedactingFormatter(PII_FIELDS)
        sh.setFormatter(formatter)
        log.addHandler(sh)

        return log