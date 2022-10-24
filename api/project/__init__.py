from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask.cli import with_appcontext
import click

db = SQLAlchemy()



def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    
    db.init_app(app)


    with app.app_context():
        from project.app import api
        # import commands

        @click.command('create_db')
        def create_db():
            db.create_all()

        app.cli.add_command(create_db)
        app.register_blueprint(api.api_bp)
        # app.register_blueprint(commands.db_bp)

        return app

