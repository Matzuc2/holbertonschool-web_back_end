# Personal Data - Protecting Sensitive Information

## Description

This project implements mechanisms to protect personal data in Python application logs. It automatically masks sensitive information (passwords, emails, etc.) before they are written to log files.

## Learning Objectives

- Understand the importance of personal data protection (GDPR compliance)
- Manipulate regular expressions (regex) to filter data
- Use Python's `logging` module securely
- Create custom formatters for logs
- Handle database connections securely

## Files

### `filtered_logger.py`

Contains two main components:

#### 1. `filter_datum()`
Function that obfuscates values of sensitive fields in a message.

**Parameters:**
- `fields`: list of fields to mask
- `redaction`: replacement string (e.g., "***")
- `message`: message to filter
- `separator`: separator character (e.g., ";")

**Example:**
```python
message = "name=Bob;email=bob@mail.com;password=secret"
result = filter_datum(["email", "password"], "***", message, ";")
# Result: "name=Bob;email=***;password=***"
```

#### 2. `RedactingFormatter`
Class inheriting from `logging.Formatter` that automatically applies obfuscation to logs.

**How it works:**
- Intercepts log messages before formatting
- Applies `filter_datum()` to mask sensitive fields
- Delegates final formatting to parent class

## Usage

```python
import logging
from filtered_logger import RedactingFormatter

# Define fields to protect
PII_FIELDS = ("email", "password", "ssn", "phone")

# Create logger with the formatter
logger = logging.getLogger("user_data")
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = RedactingFormatter(fields=PII_FIELDS)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Log data
logger.info("name=John;email=john@example.com;password=secret123")
# Output: [HOLBERTON] user_data INFO 2026-02-23 10:30:00: name=John;email=***;password=***
```

## Key Concepts

### Regex for Obfuscation
```python
pattern = f"{field}=[^{separator}]*"
```
- Finds the specified field
- Captures everything until the next separator
- Allows replacing only the value without affecting other fields

### Inheritance and `super()`
```python
def format(self, record: logging.LogRecord) -> str:
    record.msg = filter_datum(...)  # Modify the message
    return super().format(record)   # Delegate final formatting
```

## Best Practices

✅ **Do:**
- Always mask PII (Personally Identifiable Information) in logs
- Use environment variables for sensitive information
- Log enough information for debugging

❌ **Don't:**
- Log passwords in plain text
- Log credit card numbers
- Log medical data without protection

## Requirements

- Python 3.7+
- No external dependencies (uses standard library only)

## Author

Holberton School - Backend Web Development Project

## License

Educational project