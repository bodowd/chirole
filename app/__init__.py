from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
# Page to redirect to if not logged in. Use with the @login_required decorator
login_manager.login_view = 'main.home'
login_manager.login_message_category = 'info'  # info is bootstrap class for a nice blue alert

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    login_manager.init_app(app)

    from app import models
    db.init_app(app)
    migrate.init_app(app, db)

    from app.main.routes import main
    app.register_blueprint(main)

    from app.posts.routes import posts
    app.register_blueprint(posts)

    from app.user.routes import user
    app.register_blueprint(user)

    return app
