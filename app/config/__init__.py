from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    FLASK_ENV=os.environ.get('FLASK_ENV')
    SECRET_KEY=os.environ.get('SECRET_KEY')
    DB_HOST=os.environ.get('DB_HOST')
    DB_USER=os.environ.get('DB_USER')
    DB_PASSWORD=os.environ.get('DB_PASSWORD')
    DB_NAME=os.environ.get('DB_NAME')
class ProductionConfig(Config):
    DEBUG= False
class DevelopmentConfig(Config):
    DEBUG= True
config = {
    'developement':DevelopmentConfig,
    'poduction':ProductionConfig
}

