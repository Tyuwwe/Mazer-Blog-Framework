# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123456@localhost/MazerDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'mbf_secret_key_salt'
    STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
