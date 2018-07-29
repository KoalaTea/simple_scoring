from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config.from_object(Config)
db = SQLAlchemy(app)
db.init_app(app)
#db.create_all()
migrate = Migrate(app, db)

from . import views
