from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

USER = os.getenv('DBUSER')
PASSWORD = os.getenv('DBPASS')
HOST = os.getenv('DBHOST')
PORT = os.getenv('DBPORT')
SCHEMA = os.getenv('DBSCHEMA')

dbURI = "mysql+pymysql://"+USER+":"+PASSWORD+"@"+HOST+":"+PORT+"/"+SCHEMA

app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SQLALCHEMY_TRACK_MODIFACATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
