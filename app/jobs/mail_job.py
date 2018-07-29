from app.checks import SMTP
from app.checks import IMAP
from app.models import Score
#from app import celery
from app import db
from app import utils
from celery.decorators import periodic_task
from celery.task.schedules import crontab
import logging

logger = logging.getLogger(__name__)

def check_smtp(host, team):
    current_number = utils.get_current_check(team, 'smtp')
    score = Score(team=team, check_name='smtp', check_number=current_number+1)
    logger.info('starting smtp check for {}'.format(team))
    try:
        result = SMTP.check(host, 25, 'test', '{}.benron'.format(team), 'password')
        if result:
            logger.debug('{} smtp result: {}'.format(team, result))
            score.success == True
    except Exception as e:
        logger.error('{} smtp failed with {}'.format(team, e))
    logger.info('finished smtp check for {}'.format(team))
    second_check = utils.get_current_check(team, 'smtp')
    if second_check != current_number:
        score.current_number = second_check + 1
    db.session.add(score)
    db.session.commit()

def check_imap(host, team):
    current_number = utils.get_current_check(team, 'imap')
    score = Score(team=team, check_name='imap', check_number=current_number+1)
    logger.info('starting imap check for {}'.format(team))
    try:
        result = IMAP.check(host, 143, 'test', 'password')
        if result:
            logger.debug('{} imap result: {}'.format(team, result))
            score.success == True
    except Exception as e:
        logger.error('{} imap failed with {}'.format(team, e))
    logger.info('finished imap check for {}'.format(team))
    second_check = utils.get_current_check(team, 'imap')
    if second_check != current_number:
        score.current_number = second_check + 1
    db.session.add(score)
    db.session.commit()


@periodic_task(run_every=crontab(minute='*/10'))
def check_smtp_team1():
    check_smtp('10.120.1.13', 'team1')

@periodic_task(run_every=crontab(minute='*/10'))
def check_smtp_team2():
    check_smtp('10.120.2.13', 'team2')

@periodic_task(run_every=crontab(minute='*/10'))
def check_imap_team1():
    check_imap('10.120.1.13', 'team1')

@periodic_task(run_every=crontab(minute='*/10'))
def check_imap_team2():
    check_imap('10.120.2.13', 'team2')