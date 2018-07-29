from app.models import Score

def get_current_check(team, check_name):
    scores = Score.query.filter(Score.team=='team1').filter(Score.check_name=='ping')
    current_number = 0
    for score in scores:
        if current_number < score.check_number:
            current_number = score.check_number
    return current_number