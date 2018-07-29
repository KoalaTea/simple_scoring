import logging
import os
from app.models import Score

logger = logging.getLogger()

def check_ping_local():
    logger.info('checking ping for team 1')
    score = Score(team='team1', check_name='http', check_number=1)
    result = os.system('ping -c 1 ' + '127.0.0.1')
    # for host try 3 times, if all pass it passes
    if not result:
        logger.debug('team 1 passed ping check')
        score.success = True
    logger.info('finished checking ping for team 1')

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG')
    check_ping_local()