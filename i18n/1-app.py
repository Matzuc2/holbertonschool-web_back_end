#!/usr/bin/env python3
"""Basic flask app"""


from flask import Flask, render_template
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


@app.route('/')
def index():
    """return basic html template"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
