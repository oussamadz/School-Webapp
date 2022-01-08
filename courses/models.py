from django.db import models
from django.utils import timezone
import datetime
from dateutil import relativedelta

Levels = [('N/A','N/A'),('1-primaire','1_pri'),('2-primaire','2_pri'),('3-primaire','3_pri'),('4-primaire','4_pri'),('5-primaire','5_pri'),
	('1-moyenne','1_moy'),('2-moyenne','2_moy'),('3-moyenne','3_moy'),('4-moyenne','4_moy'),
	('1-secondaire','1_sec'),('2-secondaire','21_sec'),('3-secondaire','31_sec')]


class Course(models.Model):

    weekdays = [('N/A','N/A'),('Dimanche','Dim'),('Lundi','Lun'),('Mardi','Mar'),('Mercredi','Mer'),('Jeudi','Jeu'),('Vendredi','Ven'),('Samedi','Sam')]
    days_en = {'Dimanche':'Sunday', 'Lundi':'Monday', 'Mardi':'Tuesday', 'Mercredi':'Wednesday', 'Jeudi':'Thursday', 'Vendredi':'Friday', 'Samedi':'Saturday', 'N/A':'N/A'}


    name = models.CharField(max_length=200)
    price = models.IntegerField(default = 0)
    desc = models.TextField(max_length=500,default="...")
    cours_start = models.DateField(default = timezone.now)
    time = models.TimeField()
    time2 = models.TimeField(default=timezone.now)
    niveau = models.CharField(choices=Levels, max_length=100,blank=False,default='1_pri')
    prof = models.CharField(max_length=100, default='N/A')
    wday1 = models.CharField(choices=weekdays,max_length=10, blank=False, default='N/A')
    wday2 = models.CharField(choices=weekdays,max_length=10, blank=False, default='N/A')
    sal = models.ForeignKey('courses.Salle',on_delete=models.PROTECT, default=1)

    def end_time(self):
        #delta = timedelta(hours = 2) 
        tm1 = datetime.time(self.time.hour+2,self.time.minute)
        tm2 = datetime.time(self.time2.hour+2,self.time2.minute)
        return [tm1, tm2]

    def calc_paiment(self, presence):
        date_start = self.cours_start
        date_end = datetime.date(date_start.year,date_start.month+1, date_start.day)
        count = 0
        print(f'{date_start} : {date_end}')
        while date_start <= date_end:
            if self.days_en[self.wday1] in date_start.strftime("%A") or self.days_en[self.wday2] in date_start.strftime("%A"):
                count +=1
            date_start += datetime.timedelta(days=1)
        unit = self.price /3
        unit = unit/count
        return unit*presence

    def __str__(self):
        return f'{self.name} : {self.niveau}'

class Salle(models.Model):
    name = models.CharField(max_length=10)
    capacity = models.IntegerField()
    def __str__(self):
        return f'{self.name} : {self.capacity}'

class timeperiod(models.Model):
    weekdays = [('N/A','N/A'),('Dimanche','Dim'),('Lundi','Lun'),('Mardi','Mar'),('Mercredi','Mer'),('Jeudi','Jeu'),('Vendredi','Ven'),('Samedi','Sam')]
    weekday = models.CharField(choices=weekdays, max_length=100,blank=False, default="N/A")
    time= models.TimeField()
    def __str__(self):
	    return f'{self.weekday}  ---    {self.time}'


# Create your models here.
