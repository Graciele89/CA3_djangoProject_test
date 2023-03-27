from django.contrib.auth.models import User
from django.db import models
import datetime
from django.utils import timezone
#from sorl.thumbnail import ImageField

class PostExercise(models.Model):
    text_exercise_type = models.CharField(max_length=300, blank=False, null=False)
    text_workout_plan = models.CharField(max_length=500, blank=False, null=False)
    text_week_day = models.CharField(max_length=20, blank=False, null=False)
    text_time = models.TimeField(blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #image = ImageField()


    