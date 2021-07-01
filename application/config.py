import json
from configparser import ConfigParser
from pathlib import Path

basedir = Path(__file__).parent.parent
config = ConfigParser()
config.read(Path(basedir, 'config.ini'))


basedir = Path(__file__).parent
DEBUG = json.loads(str(config.get('base', 'DEBUG')).lower())

class Config:
    DEBUG: DEBUG
    PROJECT_NAME = config.get('base', 'project_name')

    # database configs
    DB_NAME = config.get('database', 'name')
    DB_USERNAME = config.get('database', 'user')
    DB_PASSWORD = config.get('database', 'password')
    DB_HOST = config.get('database', 'host', fallback='localhost')
    DB_PORT = config.get('database', 'port', fallback=3306)

    SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

settings = Config()