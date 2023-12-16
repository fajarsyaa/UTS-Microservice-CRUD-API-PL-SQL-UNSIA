import os
from re import DEBUG
from dotenv import load_dotenv

# setting .env
dotenv_path = os.path.join(os.path.dirname(__file__),'env')
if os.path.exists(dotenv_path) :
    load_dotenv(dotenv_path)

class Config:
    SECRET_KEY = "inirahasiabanget"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig:
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://rafi.galuh:password999@localhost/microserviceapp'
    SQLALCHEMY_ECHO = True

