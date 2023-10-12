from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/parcial_web"
app.config['SQLALCHEMY_TRACK_MODIFACATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
