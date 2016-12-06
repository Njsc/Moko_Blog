from flask import Flask
from view import bp
from model import db
from admin import create_admin
from flask.ext.login import LoginManager
from app.filter import my_format_datetime, babel


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprints(app)
    init_login(app)
    register_database(app)
    create_admin(app)
    register_babel(app)
    register_jinjia_filters(app)
    return app


def register_blueprints(app):
    app.register_blueprint(bp)


def register_database(app):
    db.init_app(app)


def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from app.model import User
        return User.objects(id=user_id).first()


def register_babel(app):
    babel.init_app(app)


def register_jinjia_filters(app):
    app.jinja_env.filters['my_format_datetime'] = my_format_datetime
