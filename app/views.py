from . import app
from .models import Auth, Score
from .models import db
from app import utils

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
    current_check_team1 = utils.get_current_check('team1', 'ping')
    current_check_team2 = utils.get_current_check('team2', 'ping')
    team1 = ['{} {} -'.format(score.check_name, score.success) for score in scores if score.team == 'team1' and score.check_number == current_check_team1]
    team2 = ['{} {} -'.format(score.check_name, score.success) for score in scores if score.team == 'team2' and score.check_number == current_check_team2]
    text = '<html><body><p>'
    text += '<h1>Check #{}</h1>'.format(current_check_team1)
    text += '{}={}'.format('team1', ' '.join(team1))
    text += '</p>\n<p>'
    text += '{}={}'.format('team2', ' '.join(team2))
    text += '</p></body></html>'
    return text

@app.route('/score/test')
def specific_score():
    return 'hi'

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