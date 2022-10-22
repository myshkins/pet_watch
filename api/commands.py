from flask import Blueprint
from flask.cli import with_appcontext
import click
from project.models import db


db_bp = Blueprint('db_bp', __name__)

@db_bp.cli.command('create_db')
def create_db():
    '''create database tables'''
    db.create_all()
    click.echo("Create all tables")

