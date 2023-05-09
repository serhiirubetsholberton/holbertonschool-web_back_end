#!/usr/bin/env python3
"""
Filtered logger module
"""

import re
import logging
from typing import List
from os import getenv
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    """Description: Implement a get_logger function
    that takes no arguments and returns a logging.Logger object."""
    log = logging.getLogger("user_data")
    log.setLevel(logging.INFO)
    log.propagate = False

    sh = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    sh.setFormatter(formatter)
    log.addHandler(sh)

    return log


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    connection_db = mysql.connector.connection.MySQLConnection(
        user=getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=getenv("PERSONAL_DATA_DB_NAME"),
    )

    return connection_db


def main():
    """obtain a database connection using get_db and retrieve all rows in the
    users table and display each row under a filtered format"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    result = cursor.fetchall()
    for row in result:
        message = (
            f"name={row[0]}; "
            + f"email={row[1]}; "
            + f"phone={row[2]}; "
            + f"ssn={row[3]}; "
            + f"password={row[4]};"
        )
        print(message)
        log_record = logging.LogRecord(
            "my_logger", logging.INFO, None, None, message, None, None
        )
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    cursor.close()
    db.close()


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
        """Filters values in incoming log records using filter_datum"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super(RedactingFormatter, self).format(record),
            self.SEPARATOR,
        )


if __name__ == "__main__":
    main()
