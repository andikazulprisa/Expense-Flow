from flask import Flask
from app.extensions import db, migrate, jwt, cors
from config import Config
from app.models import *
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Create tables (for dev only)
    with app.app_context():
        db.create_all()

    return app
