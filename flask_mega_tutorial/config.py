import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secrets'

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'postgres://postgres:password@postgres:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') or False

    # https://jinja.palletsprojects.com/en/2.11.x/api/#jinja2.Environment
    JINJA_OPTIONS = {'lstrip_blocks': True, 'trim_blocks': True}
