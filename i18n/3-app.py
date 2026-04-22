#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext as babel_gettext


class Config():
    """Config class with class variables for i18n."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale():
    """Select the best language match from the request."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def gettext(message):
    """Translate a message using Flask-Babel."""
    return babel_gettext(message)


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

gettext("home_title")
gettext("home_header")


@app.route("/")
def index():
    """Return basic html template."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
