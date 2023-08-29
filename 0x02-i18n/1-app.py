#!/usr/bin/env python3
"""
Created by Jenaide Sibolie
"""
from flask import Flask, render_template
from flask_babel import Babel



class Config:
    """ a Flask babel config """
    LANGUAGE = ["en", "fr"]
    BABEL_DEFAULT_LOCAL = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"



app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index():
    """
    route that outputs hello world
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
