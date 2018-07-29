from simple_scoring.checks import SSH
from simple_scoring.models import Score
from simple_scoring.models import SSHCreds
import logging

logger = logging.getLogger(__name__)


port = '22'
username = 'root'
password = 'changeme'

def cheack_ssh_team1():
    score = Score(team='team1', check_name='ssh', check_number=)
    result = SSH.check('10.120.1.13', port, username, password)
    if result:
        logger.debug('team 1 ssh result: {}'.format(result))
        score.success == True

def cheack_ssh_team2():
    score = Score(team='team2', check_name='ssh', check_number=)
    result = SSH.check('10.120.2.13', port, username, password)
    if result:
        logger.debug('team 2 ssh result: {}'.format(result))
        score.success == True