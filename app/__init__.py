from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os.path
from celery import Celery

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
class Config():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config.from_object(Config)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = Celery(__name__, broker='redis://localhost:6379')
db = SQLAlchemy(app)
db.init_app(app)
#db.create_all()
migrate = Migrate(app, db)

from . import views
from .jobs import ping_job
from .jobs import ssh_job
