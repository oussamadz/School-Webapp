from django.contrib import admin
from .models import Course, Salle, timeperiod

admin.site.register(Course)
admin.site.register(Salle)
admin.site.register(timeperiod)
# Register your models here.
