from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app import models
    db.init_app(app)
    migrate.init_app(app, db)

    from app.main.routes import main
    app.register_blueprint(main)

    from app.posts.routes import posts
    app.register_blueprint(posts)

    return app
