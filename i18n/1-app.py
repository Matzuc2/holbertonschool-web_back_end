#!/usr/bin/env python3
"""Basic flask app"""


from flask import Flask, render_template
from flask_babel import Babel


class Config():
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
babel = Babel(
    app,
    locale_selector=Config.LANGUAGES[0], timezone_selector="UTC"
    )


if __name__ == "__main__":
    app.run(debug=True)
