from . import app
from . import forms
from flask import render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from flask_login import login_required
from .models import Auth, Score, SSHCreds
from .models import db
from app import utils
from app import login

@login.user_loader
def load_user(id):
    return Auth.query.get(int(id))

@app.route('/')
def index():
    return '<html><body><a href="./score">score</a><br><a href="./change_ssh">change ssh pass</a><br><a href="./the_ssh_creds">view ssh creds</a></body></html>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = forms.LoginForm()
    if form.validate_on_submit():
        user = Auth.query.filter_by(name=form.username.data).first()
        if user is None or user.password != form.password.data:
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)

@app.route('/the_ssh_creds')
@login_required
def get_all_creds():
    creds = SSHCreds.query.filter(SSHCreds.team == current_user.name)
    text = ''
    for cred in creds:
        text += ' {} - password:"{}", '.format(cred.team, cred.password)
    return text

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
    text += '</p><h1>Past Checks</h1>'
    for i in range(1, current_check_team1):
        text += '<a href="./score/{}">{}</a><br>'.format(i, i)
    text += '</body></html>'
    return text

@app.route('/score/<int:past_check>')
def specific_score(past_check):
    scores = Score.query.all()
    current_check_team1 = utils.get_current_check('team1', 'ping')
    team1 = ['{} {} -'.format(score.check_name, score.success) for score in scores if score.team == 'team1' and score.check_number == past_check]
    team2 = ['{} {} -'.format(score.check_name, score.success) for score in scores if score.team == 'team2' and score.check_number == past_check]
    text = '<html><body><p>'
    text += '<h1>Check #{}</h1>'.format(current_check_team1)
    text += '{}={}'.format('team1', ' '.join(team1))
    text += '</p>\n<p>'
    text += '{}={}'.format('team2', ' '.join(team2))
    text += '</p><h1>All Checks</h1>'
    for i in range(1, current_check_team1+1):
        text += '<a href="./{}">{}</a><br>'.format(i, i)
    text += '</body></html>'
    return text

@app.route('/start')
def start():
    team1 = Auth('team1', 'team2')
    db.session.add(team1)
    team2 = Auth('team2', 'team1')
    db.session.add(team2)
    team1_ssh = SSHCreds('team1', 'Ritsec123*')
    team2_ssh = SSHCreds('team2', 'Ritsec123*')
    db.session.add(team1_ssh)
    db.session.add(team2_ssh)
    db.session.commit()
    return 'fine'

@app.route('/change_ssh', methods=['GET', 'POST'])
@login_required
def change_ssh():
    form = forms.ChangeForm()
    if form.validate_on_submit():
        cred = SSHCreds.query.filter(SSHCreds.team == current_user.name).first()
        cred.password = form.password.data
        db.session.add(cred)
        db.session.commit()
        return redirect(url_for('get_all_creds'))
    return render_template('change_creds.html', team=current_user.name, form=form)

@app.route('/logout')
def logout():
    logout_user()
    return 'logout'
