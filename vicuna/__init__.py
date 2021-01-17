# coding=utf-8
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import config

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'vicuna.sqlite'),
    )
    app.config.from_object(config)

    # if test_config is None:
    #     load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from vicuna.auth.auth import init_login, init_admin, MyAdminIndexView, MyModelView, User
    init_login(app)

    # from . import db
    db.init_app(app)

    # from flask_login import LoginManager
    # login_manager = LoginManager()
    # login_manager.init_app(app)

    # Flask views
    @app.route('/')
    def index():
        return render_template('index.html')

    from flask_admin import Admin
    admin = Admin(app, name=u'样例', template_mode='bootstrap3', index_view=MyAdminIndexView(), base_template='my_master.html')
    # Add view
    admin.add_view(MyModelView(User, db.session))

    from vicuna.views import auth
    app.register_blueprint(auth.bp)

    from vicuna.views import blog
    app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')

    # from vicuna.views import admin
    # app.register_blueprint(admin.bp)

    # from vicuna.views import index
    # app.register_blueprint(index.bp)

    return app
