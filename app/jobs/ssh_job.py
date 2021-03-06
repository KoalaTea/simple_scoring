from app.checks import SSH
from app.models import Score
from app.models import SSHCreds
#from app import celery
from app import db
from app import utils
from celery.decorators import periodic_task
from celery.task.schedules import crontab
import logging

logger = logging.getLogger(__name__)


port = '22'
username = 'superadmin'
#password = 'changeme'

@periodic_task(run_every=crontab(minute='*/10'))
def check_ssh_team1():
    current_number = utils.get_current_check('team1', 'ssh')
    the_cred = None
    creds = SSHCreds.query.all()
    for cred in creds:
        if cred.team == 'team1':
            the_cred = cred
    score = Score(team='team1', check_name='ssh', check_number=current_number+1)
    logger.info('starting ssh check for team 1')
    try:
        result = SSH.check('10.120.1.13', port, username, the_cred.password)
        if result:
            logger.debug('team 1 ssh result: {}'.format(result))
            score.success = True
    except Exception as e:
        logger.error('team 1 ssh failed with {}'.format(e))
    logger.info('finished ssh check for team 1')
    second_check = utils.get_current_check('team1', 'ssh')
    if second_check != current_number:
        score.current_number = second_check + 1
    db.session.add(score)
    db.session.commit()

@periodic_task(run_every=crontab(minute='*/10'))
def check_ssh_team2():
    current_number = utils.get_current_check('team2', 'ssh')
    score = Score(team='team2', check_name='ssh', check_number=current_number+1)
    creds = SSHCreds.query.all()
    the_cred = None
    for cred in creds:
        if cred.team == 'team2':
            the_cred = cred
    logger.info('starting ssh check for team 2')
    try:
        result = SSH.check('10.120.2.13', port, username, the_cred.password)
        print(result)
        if result:
            logger.debug('team 2 ssh result: {}'.format(result))
            score.success = True
    except Exception as e:
        logger.error('team 2 ssh failed with {}'.format(e))
    logger.info('finished ssh check for team 2')
    second_check = utils.get_current_check('team2', 'ssh')
    if second_check != current_number:
        score.current_number = second_check + 1
    db.session.add(score)
    db.session.commit()

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    check_ssh_team2()

