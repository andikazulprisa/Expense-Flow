from flask import Flask
from app.extensions import db, migrate, jwt, cors
from config import Config
from app.models import *
from app.routes.auth_routes import auth_bp
from app.routes.protected_routes import protected_bp

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

    # Protected routes
    app.register_blueprint(protected_bp, url_prefix='/user')

    # Create tables (for dev only)
    with app.app_context():
        db.create_all()

    return app
