#!/usr/bin/env python3
"""Basic flask app"""


from flask import Flask
from flask_babel import Babel


class Config():
    """Config class with class variables for i18n"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(
    app
    )
app.config.from_object(Config)


if __name__ == "__main__":
    app.run(debug=True)
