import logging
from app.checks import HTTP
from app.models import Score

logger = logging.getLogger(__name__)

def check_http_team1():
    logger.info('checking http for team 1')
    score = Score(team='team1', check_name='http', check_number=1)
    result = HTTP.check('1.1.1.1', '5')
    logger.debug('')
    if result:
        logger.debug('team1 http passed')
        score.success = True
    logger.info('finished checking http for team 1')

def check_http_team2():
    logger.info('checking http for team 2')
    score = Score(team='team1', check_name='http', check_number=1)
    result = HTTP.check('1.1.1.1', '5')
    if result:
        logger.debug('team2 http passed')
        score.success = True
    logger.info('finished checking http for team 2')