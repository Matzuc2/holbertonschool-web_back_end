#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
from pytz import timezone, UnknownTimeZoneError

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """Config class with class variables for i18n"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_user():
    """get user from url by its id or none"""
    id_user = request.args.get('login_as')
    if id_user:
        user = users.get(int(id_user))
        if user:
            return user
        else:
            return None
    else:
        return None


def get_locale():
    """get locale language from url, or default"""
    locale = request.args.get('locale')
    if locale:
        if locale in app.config['LANGUAGES']:
            return locale
        else:
            return request.accept_languages.best_match(app.config['LANGUAGES'])
    user = g.user
    if user:
        locale = user.get("locale")
        if locale and locale in app.config['LANGUAGES']:
            print(locale)
            return locale
        else:
            return request.accept_languages.best_match(app.config['LANGUAGES'])
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone() -> str:
    '''get locale timezone'''
    timezone_locale = request.args.get('timezone')
    user = g.user
    if timezone_locale:
        try:
            timezone(timezone_locale)
            return timezone_locale
        except UnknownTimeZoneError:
            pass
    if user and user.get('timezone'):
        try:
            timezone(user['timezone'])
            return user['timezone']
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.before_request
def before_request():
    user = get_user()
    if user:
        g.user = user
    else:
        g.user = None


@app.route('/')
def index():
    """return basic html template"""
    if g.user:
        return render_template('5-index.html', user=g.user)
    else:
        return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
