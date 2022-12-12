from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'jqkhciuewhfwzf323f3'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.products import routes
