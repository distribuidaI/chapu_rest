from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db_global = None


class DatabaseConfig():

    def __init__(self):
        self.db = SQLAlchemy()
        self.ma = Marshmallow()


def setup_database():
    global db_global
    db_global = DatabaseConfig()


setup_database()





