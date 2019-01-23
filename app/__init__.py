# -*- coding: utf-8 -*-
from app.config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'home.index'
csrf = CSRFProtect()


def create_app(config_name):
    myapp = Flask(__name__)
    myapp.config.from_object(config[config_name])
    initialize_extensions(myapp)
    register_blueprints(myapp)
    return myapp

def initialize_extensions(myapp):
    db.init_app(myapp)
    login_manager.init_app(myapp)
    csrf.init_app(myapp)

def register_blueprints(myapp):
    from app.home import home
    from app.admin import admin
    myapp.register_blueprint(admin, url_prefix='/admin/')
    myapp.register_blueprint(home)