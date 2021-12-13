from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SECRET_KEY"] = "13f9d18375c494a4561aff0a0fd2d66d"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bp = Bcrypt(app)

from app import routes
