from flask import Flask
from flask_sqlalchemy import SQLAlchemy

App = Flask(__name__)
App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\Zenaide\\Documents\\dev\\Projeto\\teste.db"
db = SQLAlchemy(App)

from Routes import *
from Services import *
from templates import *

if __name__ == "__main__":
    App.run(port=80)

