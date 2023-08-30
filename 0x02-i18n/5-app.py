#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict


class Config:
    """ a Flask babel config """
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def fetch_user() -> Union[Dict, None]:
    """
    fetches a user based on the user_id
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None

@app.before_request
def before_request() -> None:
    """
    method that checks if user is valid
    """
    user = fetch_user()
    g.user = user

@babel.localeselector
def get_locale():
    """
    a function to retrieve the locale from a web page
    """
    local = request.args.get('locale', '')
    if local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    route that outputs hello world
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
