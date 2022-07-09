from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import *
from django.utils import timezone
from datetime import timedelta

class SwimRecord(models.Model):    
    
    first_name = models.CharField(max_length=255, validators=[MinLengthValidator(1, 'This field cannot be blank.')])
    last_name = models.CharField(max_length=255, validators=[MinLengthValidator(1, 'This field cannot be blank.')])
    team_name = models.CharField(max_length=255, validators=[MinLengthValidator(1, 'This field cannot be blank.')])
    relay = models.BooleanField(validators=[RegexValidator(r'True|False', "'None' value must be either True or False.")])
    stroke = models.CharField(max_length=15, validators=[RegexValidator('front crawl|butterfly|breast|back|freestyle', f"doggie paddle is not a valid stroke")])
    distance = models.IntegerField(validators=[MinValueValidator(50, "Ensure this value is greater than or equal to 50.")])
    record_date = models.DateTimeField(validators=[MaxValueValidator(timezone.now(), "Can't set record in the future.")])
    record_broken_date = models.DateTimeField(validators=[MinValueValidator(timezone.now(), "Can't break record before record was set.")])
