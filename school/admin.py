from django.contrib import admin
from .models import Student, Admission, Post,Categories, Events, Cmessage, galleryImages 

admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Admission)
admin.site.register(Categories)
admin.site.register(Events)
admin.site.register(Cmessage)
admin.site.register(galleryImages)
# Register your models here.
