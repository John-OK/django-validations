def first_name_presence(first_name):
    if not first_name:
        raise ValidationError('This field cannot be blank.')

def last_name_presence(last_name):
    if not last_name:
        raise ValidationError('This field cannot be blank.')

def team_name_presence(team_name):
    if not team_name:
        raise ValidationError('This field cannot be blank.')

def relay_presence(relay):
    if not team_name:
        raise ValidationError("'None' value must be either True or False.")

def valid_stroke(stroke):
    legal_strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in legal_strokes:
        raise ValidationError("doggie paddle is not a valid stroke")
