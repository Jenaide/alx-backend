#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ a Flask babel config """
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    a function to retrieve the locale from a web page
    """
    strings = request.query_string.decode('utf-8').split('&')
    table = dict(map(lambda x: (x if '=' in x else '{}='.format(x)).split('='), strings))
    if 'locale' in table:
        if table['locale'] in app.config["LANGUAGES"]:
            return table['locale']
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """
    route that outputs hello world
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
