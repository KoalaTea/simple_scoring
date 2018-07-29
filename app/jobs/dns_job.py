from app.models import Score
from app.checks import DNS

def check_dns_team1():
    logger.info('checking dns for team 1')
    score = Score(team='team1', check_name='dns', check_number=1)
    result = DNS.check('1.1.1.1', 'domain')
    if result:
        logger.debug('dns for team 1 passed')
        score.success = True
    logger.info('finished checking dns for team 1')

def check_dns_team1():
    logger.info('checking dns for team 2')
    score = Score(team='team2', check_name='dns', check_number=1)
    result = DNS.check('1.1.1.1', 'domain')
    if result:
        logger.debug('dns for team 2 passed')
        score.success = True
    logger.info('finished checking dns for team 2')