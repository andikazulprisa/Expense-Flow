import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'yumesekai')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///expenseflow.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'yumesekai')
    CORS_HEADERS = 'Content-Type'