from flask import Flask
from config import SECRET_KEY, DATABASE_URI
from flask_wtf.csrf import CSRFProtect

# csrf = CSRFProtect()


def create_app():
    """Initialize the core application"""
    app = Flask(__name__)
    # csrf.init_app(app)

    app.app_context().push()
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    from .views import views
    from .models import db, Cafe

    # initialize plugin
    db.init_app(app)

    # create database
    db.create_all()

    # register blueprint
    app.register_blueprint(views, url_prefix="/")

    return app
