"""Flask application factory module"""
from flask import Flask
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
import click
from config import Config

db = SQLAlchemy()

def create_app():
    """application factory method"""
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from models import Temp
        from .app import api

        @click.command('create_db')
        def create_db():
            db.create_all()

        app.cli.add_command(create_db)

        return app
