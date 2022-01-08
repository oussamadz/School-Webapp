from django.db import models
from django.utils import timezone
import datetime
from dateutil import relativedelta 
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse

class niveaux():
    Levels = [('N/A','N/A'),('1-primaire','1_pri'),('2-primaire','2_pri'),('3-primaire','3_pri'),('4-primaire','4_pri'),('5-primaire','5_pri'),('1-moyenne','1_moy'),('2-moyenne','2_moy'),('3-moyenne','3_moy'),('4-moyenne','4_moy'),('1-secondaire','1_sec'),('2-secondaire','2_sec'),('3-secondaire','3_sec')]


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField()
    address = models.CharField(max_length=150,default='N/A')
    institute = models.CharField(max_length=150,default="N/A")
    niveau = models.CharField(choices=niveaux.Levels,max_length=100, blank=False, default='1-primaire')
    telephone = models.IntegerField()
    cours_in = models.ForeignKey('courses.Course',on_delete=models.CASCADE)
    sub_date = models.DateField(default=timezone.now)
    cours_start = models.DateField(default = timezone.now, verbose_name="Expiration Date")
    presence = models.TextField(default='--')
    image = models.ImageField(default='Default.png', upload_to='students_pics')
    
    def add_presence(self):
        self.presence += ',' + str(datetime.date.today())
    
    def format_p(self):
        result = self.presence.split(',')
        return result

    def month_presence(self):
        date_start = self.cours_in.cours_start
        date_end = date_start + relativedelta.relativedelta(months=1)
        count = 0
        while date_start <= date_end:
            presence_dates = self.presence.split(',')
            for dt in presence_dates:
                if dt in str(date_start):
                    count+=1
            date_start+=datetime.timedelta(days=1)
        return count

    def remove_month(self):
        self.cours_start.month += relativedelta.relativedelta(months=1)
    def period(self):
        return (self.cours_start - timezone.now().date()).days
	#return (self.cours_start - timezone.now().date()).days
    def __str__(self):
        return f'{self.last_name} {self.first_name} -- {self.niveau} -- {self.cours_in.name}'
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Admission(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length= 250)
    birthdate = models.DateField()
    niveau = models.CharField(choices=niveaux.Levels,max_length=100, blank=False, default='1-primaire')
    telephone = models.IntegerField()
    sub_date = models.DateField(default=timezone.now)
    cours_in = models.ForeignKey('courses.Course',on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('school.Categories', on_delete=models.PROTECT)
    votes = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        #return reverse('post-detail', kwargs={'pk':self.pk})
        return reverse('dashboard')

class Categories(models.Model):
    name = models.CharField(max_length = 250)
    def __str__(self):
        return self.name


class Events(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField()
    content = models.TextField()
    photo = models.ImageField(default='default-events.jpg', upload_to='events_pics')
    
    def __str__(self):
        return self.title
    def save(self):
        super().save()
        img = Image.open(self.photo.path) 
        if img.height > 286*2 or img.width > 203*2:
            output_size = (286*2,203*2)
            img.thumbnail(output_size)
            img.save(self.photo.path)


class Cmessage(models.Model):
    writer = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    content =  models.CharField(max_length=300, verbose_name='Text')
    read = models.BooleanField(default=False)
# Create your models here.

class galleryImages(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery_pics")
    def __str__(self):
        return self.title


