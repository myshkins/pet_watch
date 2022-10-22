from flask import Flask
from flask_assets import Environment, Bundle
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)
    
    db.init_app(app)
    assets = Environment(app)
    assets.init_app(app)
    
    with app.app_context():
        from .assets import compile_assets
        from .home import home
        from .about import about

        app.register_blueprint(home.home_bp)
        app.register_blueprint(about.about_bp)
        compile_assets(assets)
        return app
