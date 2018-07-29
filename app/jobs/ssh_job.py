from simple_scoring.checks import SSH
from simple_scoring.models import Score
from simple_scoring.models import SSHCreds

host = '1.1.1.1'
port = '22'
username = 'root'
password = 'changeme'

def cheack_ssh_team1():
    score = Score(team='team1', check_name='ssh', check_number=)
    result = SSH.check(host, port, username, password)
    if result:
        score.success == True

def cheack_ssh_team2():
    score = Score(team='team2', check_name='ssh', check_number=)
    result = SSH.check(host, port, username, password)
    if result:
        score.success == True