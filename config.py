import os

class Config:
    SECRET_KEY = os.environ.get('SECRET KEY')
    SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Users\JAGANNATH\db\mydb.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False