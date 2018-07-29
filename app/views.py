from . import app
from .models import Auth, Score
from .models import db

@app.route('/')
def index():
    return 'hi'

@app.route('/login')
def login():
    users = Auth.query.all()
    return '{}'.format(users)

@app.route('/score')
def score():
    scores = Score.query.all()
    team1 = [score for score in scores if score.team == 'team1']
    team2 = [score for score in scores if score.team == 'team1']
    return 'score'

@app.route('/start')
def start():
    team1 = Auth('team1', 'team2')
    db.session.add(team1)
    team2 = Auth('team2', 'team1')
    db.session.add(team2)
    db.session.commit()
    return 'fine'

@app.route('/change_ssh')
def change_ssh():
    return 'ssh'

@app.route('/logout')
def logout():
    return 'logout'