from django.db import models
from django.utils import timezone
from PIL import Image

class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    cours_in = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    cours_start = models.DateField(default = timezone.now)
    professionalExperience = models.TextField(default='N/A')
    image = models.ImageField(default='Default.png', upload_to='teachers_pics')
	
    def calc_paiment(self):
        return 0
    def __str__(self):                                                         
        return f'{self.last_name} {self.first_name} profile'               
    def save(self):
        super().save()                                                     
		
        img = Image.open(self.image.path)                                  
        if img.height > 300 or img.width > 300:                            
            output_size = (300,300)                                    
            img.thumbnail(output_size)                                 
            img.save(self.image.path)                                  


# Create your models here.
