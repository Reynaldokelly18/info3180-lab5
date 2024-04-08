from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)
app.config['SESSION_TYPE'] = 'sqlalchemy'
db= SQLAlchemy(app)
app.config['SESSION_SQLALCHEMY'] = db
from flask_migrate import Migrate
migrate =  Migrate(app,db)
from . import models 
from app import views