#!/usr/bin/env python3
"""Basic flask app"""


from flask import Flask, render_template
from flask_babel import Babel


class Config():
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
babel = Babel(
    app,
    locale_selector=Config.BABEL_DEFAULT_LOCALE,
    timezone_selector=Config.BABEL_DEFAULT_TIMEZONE
    )


if __name__ == "__main__":
    app.run(debug=True)
