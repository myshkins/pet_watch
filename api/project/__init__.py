from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():
        from project.app import api
        import commands

        # db.create_all()
        app.register_blueprint(api.api_bp)
        app.register_blueprint(commands.db_bp)

        return app

