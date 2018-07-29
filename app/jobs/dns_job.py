from app.models import Score
from app.checks import DNS
import logging
from celery.decorators import periodic_task
from celery.task.schedules import crontab

logger = logging.getLogger(__name__)

def check_dns(host, team):
    current_number = utils.get_current_check(team, 'dns')
    score = Score(team=team, check_name='dns', check_number=current_number+1)
    logger.info('starting dns check for {}'.format(team))
    try:
        result = DNS.check(host, 'wakanda.{}.benron'.format(team))
        if result:
            logger.debug('{} dns result: {}'.format(team, result))
            score.success == True
    except Exception as e:
        logger.error('{} dns failed with {}'.format(team, e))
    logger.info('finished dns check for {}'.format(team))
    second_check = utils.get_current_check(team, 'dns')
    if second_check != current_number:
        score.current_number = second_check + 1
    db.session.add(score)
    db.session.commit()

@periodic_task(run_every=crontab(minute='*/10'))
def check_dns_team1():
    check_dns('10.120.1.10', 'team1')

@periodic_task(run_every=crontab(minute='*/10'))
def check_dns_team2():
    check_('10.120.2.10', 'team2')