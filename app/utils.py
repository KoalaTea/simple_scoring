from app.models import Score

def get_current_check(team, check_name):
    scores = Score.query.all()
    scores = [score for score in scores if score.team == team]
    scores = [score for score in scores if score.check_name == check_name]
    current_number = 0
    for score in scores:
        if current_number < score.check_number:
            current_number = score.check_number
    return current_number
