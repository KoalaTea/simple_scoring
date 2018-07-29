import logging
import os
from app.models import Score

logger = logging.getLogger()

def check_ping_team1():
    logger.info('checking ping for team 1')
    servers = ['10.120.1.11', '10.120.1.13', '10.120.1.10', '10.120.1.12']
    score = Score(team='team1', check_name='ping', check_number=1)
    score.success = True
    for server in servers:
        result = os.system('ping -c 1 ' + '127.0.0.1')
        # for host try 3 times, if all pass it passes
        if result:
            logger.debug('team 1 host {} failed ping check'.format(server))
            score.success = False
    if score.success:
        logger.debug('team 1 passed ping check')
        
    logger.info('finished checking ping for team 1')

def check_ping_team2():
    logger.info('checking ping for team 2')
    servers = ['10.120.2.11', '10.120.2.13', '10.120.2.10', '10.120.2.12']
    score = Score(team='team2', check_name='ping', check_number=1)
    result = os.system('ping -c 1 ' + '127.0.0.1')
    score.success = True
    for server in servers:
        result = os.system('ping -c 1 ' + '127.0.0.1')
        # for host try 3 times, if all pass it passes
        if result:
            logger.debug('team 2 host {} failed ping check'.format(server))
            score.success = False
    if score.success:
        logger.debug('team 2 passed ping check')

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    #check_ping_local()