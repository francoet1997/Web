
from crypt import methods
from flask import Flask, render_template, Blueprint
import os

'''
app = Flask(__name__)

app.config.from_mapping(
    SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
)

app.register_blueprint(portfolio, url_prefix='')


@app.route('/')
def index():
    from portfolio import portfolio
    app.config.from_mapping(
    SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),
)
    return app'''


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(SENDGRID_KEY=os.environ.get('SENDGRID_KEY'),)

    from portfolio import bp

    app.register_blueprint(bp, url_prefix='')

    return app