import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from colorama import init, Fore
init(autoreset=True)

db = SQLAlchemy()
DB_NAME = "flight_reservation_system"
# DB_CONFIGS = {
#     'user': 'alimussifar',
#     'password': os.getenv('mysql-db-password'),
#     'host': '103.217.110.133',
#     'port': 4040,
#     'database': DB_NAME,
# }


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("my-app-key")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    # app.config["SQLALCHEMY_DATABASE_URI"] = (
    #     f"mysql+pymysql://{DB_CONFIGS['user']}:{DB_CONFIGS['password']}"
    #     f"@{DB_CONFIGS['host']}:{DB_CONFIGS['port']}/{DB_NAME}")
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///static/{DB_NAME}.db"
    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix="/")
    from .auth import auth
    app.register_blueprint(auth, url_prefix="/")
    from .admin import admin
    app.register_blueprint(admin, url_prefix="/admin")

    login_manager = LoginManager()
    login_manager.login_view = "views.home"
    login_manager.init_app(app)

    from .models import User
    create_database(app)

    @login_manager.user_loader
    def load_user(email):
        return User.query.get(email)

    from .filters import create_filters
    create_filters(app)

    return app


def create_database(app):
    if not os.path.exists(f"website/static/{DB_NAME}.db"):
        db.create_all(app=app)
        print(f"{Fore.GREEN}>>> Database Created! <<<")
