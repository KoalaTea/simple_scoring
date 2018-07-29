from . import db
from flask_login import UserMixin

class Auth(UserMixin, db.Model):
    id = db.Column (db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(6), unique=True, nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f'<Auth name="{self.name}">'

    def __str__(self):
        return f'<Auth name="{self.name}">'

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_name = db.Column(db.String(20))
    check_number = db.Column(db.Integer)
    team = db.Column(db.String(128), nullable=False)
    success = db.Column(db.Boolean())

    def __init__(self, check_name, check_number, team):
        self.check_name = check_name
        self.check_number = check_number
        self.team = team
        self.success = False

    def __repr__(self):
        return f'<Score check="{self.check_name}" number="{self.check_number}" team="{self.team}">'

class SSHCreds(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String)
    password = db.Column(db.String)
    def __init__(self, team, password):
        self.team = team
        self.password = password

    def __repr__(self):
        return f'<SSHCreds team="{self.team}" password="{self.password}"'