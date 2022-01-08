from django import forms 
from school.models import Student, niveaux 
from courses.models import Course
from courses.models import Course 

class ValidateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    birthdate = forms.DateField()
    niveau = forms.ChoiceField(choices = niveaux.Levels)
    telephone = forms.IntegerField()
    cours_in = forms.ModelChoiceField(Course.objects)
    class Meta:
        model = Student
        fields = [
                'first_name',
                'last_name',
                'birthdate',
                'niveau',
                'telephone',
                'cours_in',
                'cours_start']


    
