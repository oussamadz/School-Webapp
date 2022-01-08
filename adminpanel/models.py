from django.db import models
from django.utils import timezone 
import datetime
class dailyPaiments(models.Model):
    day = models.DateField(default=datetime.date.today)
    count = models.FloatField()
    

# Create your models here.
