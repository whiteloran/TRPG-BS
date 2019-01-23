#-*- coding: utf-8 -*-
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
# HOST = "67.230.191.124"
# PORT = "5432"
# DATABASE = "htvdata"
# USERNAME = "aoiyuuki"
# PASSWORD = "wluEnBbOR18s"
# CHARSET = "utf8"
# DB_URI = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}?charset={CHARSET}'

SQLITE = 'sqlite:///trpg-map.db'

class BaseConfig:
    SECRET_KEY = 'TRPG-map'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = SQLITE
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class TestingConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = SQLITE

class ProductionCOnfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = SQLITE
    CSRF_ENABLED = True

config = {
    'develop': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionCOnfig
}