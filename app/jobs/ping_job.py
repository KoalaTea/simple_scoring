import logging
import os
from app.models import Score
from app.checks import SSH
from app.models import SSHCreds
#from app import celery
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from app import utils
from app import db

logger = logging.getLogger()

@periodic_task(run_every=crontab(minute='*/10'))
def check_ping_team1():
    logger.info('checking ping for team 1')
    servers = ['10.120.1.11', '10.120.1.13', '10.120.1.10', '10.120.1.12']
    #servers = ['127.0.0.1']
    current_number = utils.get_current_check('team1', 'ping')
    score = Score(team='team1', check_name='ping', check_number=current_number+1)
    try:
        score.success = True
        for server in servers:
            result = os.system('ping -c 1 ' + server)
            # for host try 3 times, if all pass it passes
            if result:
                logger.debug('team 1 host {} failed ping check'.format(server))
                score.success = False
        if score.success:
            logger.debug('team 1 passed ping check')
    except Exception as e:
        logger.error('team 1 ping {}'.format(e))
    
    logger.info('finished checking ping for team 1')
    second_check = utils.get_current_check('team1', 'ping')
    if second_check != current_number:
        score.current_number = second_check + 1
    db.session.add(score)
    db.session.commit()

@periodic_task(run_every=crontab(minute='*/10'))
def check_ping_team2():
    logger.info('checking ping for team 2')
    servers = ['10.120.2.11', '10.120.2.13', '10.120.2.10', '10.120.2.12']
    #servers = ['127.0.0.1']
    current_number = utils.get_current_check('team2', 'ping')
    score = Score(team='team2', check_name='ping', check_number=current_number+1)
    try:
        score.success = True
        for server in servers:
            result = os.system('ping -c 1 ' + server)
            # for host try 3 times, if all pass it passes
            if result:
                logger.debug('team 2 host {} failed ping check'.format(server))
                score.success = False
        if score.success:
            logger.debug('team 2 passed ping check')
    except Exception as e:
        logger.error('team 2 ping {}'.format(e))

    logger.info('finished checking ping for team 2')
    second_check = utils.get_current_check('team2', 'ping')
    if second_check != current_number:
        score.current_number = second_check + 1
    db.session.add(score)
    db.session.commit()

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    #check_ping_local()