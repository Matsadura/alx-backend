#!/usr/bin/env python3
"""
This file we'll Create a single
/ route and an index.html template that simply outputs
“Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>)
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """This class has a LANGUAGES class attribute
    equal to ["en", "fr"]"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Gets locale for a web page"""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index() -> str:
    """renders 0-index.html"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
