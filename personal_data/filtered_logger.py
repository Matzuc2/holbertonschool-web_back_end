#!/usr/bin/env python3

"""
Module for filtering and redacting sensitive information in logs.

This module provides utilities to obfuscate personally identifiable
information (PII) in log messages to comply with data protection
regulations like GDPR.
"""

import re
import logging
import typing


PII_FIELDS = ("name", "email", "phone", "ssn", "password")
"""tuple: Fields considered as PII that should be redacted in logs."""


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message.

    Uses regex substitution to replace field values with a redaction string
    while preserving field names and message structure.

    Args:
        fields (typing.List[str]): List of field names to obfuscate.
        redaction (str): String to replace sensitive values with.
        message (str): The log message containing field=value pairs.
        separator (str): Character separating field=value pairs.

    Returns:
        str: The message with specified field values replaced by redaction.

    Example:
        >>> filter_datum(["password"], "***", "name=Bob;password=secret", ";")
        'name=Bob;password=***'
    """
    for field in fields:
        pattern = f"{field}=[^{separator}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Custom logging formatter that redacts sensitive information.

    This formatter automatically obfuscates specified fields in log messages
    before formatting them. It's designed to protect PII in application logs.

    Attributes:
        REDACTION (str): Default string used to replace sensitive values.
        FORMAT (str): Log message format string with placeholders.
        SEPARATOR (str): Default separator character for field=value pairs.
        fields (typing.List[str]): List of field names to redact.

    Example:
        >>> formatter = RedactingFormatter(fields=["email", "password"])
        >>> handler = logging.StreamHandler()
        >>> handler.setFormatter(formatter)
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        """
        Initialize the RedactingFormatter.

        Args:
            fields (typing.List[str]): List of field names to redact in logs.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record with sensitive fields redacted.

        This method intercepts the log message, applies field obfuscation,
        then delegates to the parent formatter for final formatting.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log message with sensitive data redacted.
        """
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.getMessage(), self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Create and configure a logger for user data with PII redaction.

    Creates a logger named 'user_data' configured to:
    - Log up to INFO level
    - Not propagate messages to parent loggers
    - Use RedactingFormatter to obfuscate PII fields
    - Output to console via StreamHandler

    Returns:
        logging.Logger: Configured logger instance with PII protection.

    Example:
        >>> logger = get_logger()
        >>> logger.info("name=John;email=john@mail.com;password=secret")
        [HOLBERTON] user_data INFO 2026-02-23: name=***;email=***;password=***
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=list(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
