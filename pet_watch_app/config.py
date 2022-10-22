import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env.local.dev"))

class Config(object):
    FLASK_APP = os.environ.get("FLASK_APP")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_DEBUG = os.environ.get("FLASK_DEBUG")

    # Database               
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False      #if 'True', logs all database activity to Python's stderr for debugging.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "password"
    POSTGRES_DB = "chanchtemps"
