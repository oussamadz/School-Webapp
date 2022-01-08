from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.widgets import SelectDateWidget
from django.forms import DateInput
from .models import Post, Student, Admission, niveaux, Categories, Events, Cmessage, galleryImages 
from courses.models import Course
from teachers.models import Professor 
import datetime


def home(request):
    Cours = Course.objects.all()
    last_week = datetime.datetime.today() - datetime.timedelta(days=7)
    if Events.objects.filter(date__gt=datetime.datetime.today()).count() != 0:
        upcoming_event = Events.objects.filter(date__gt=datetime.datetime.today()).order_by('date')[0]
    else:
        upcoming_event = Events.objects.order_by('date').first()
    Eventss = Events.objects.all().order_by('date')
    stdn_count = len(Student.objects.all())
    prof_count = len(Professor.objects.all())
    crs_count = len(Course.objects.all())
    top_posts = Post.objects.all().order_by('votes')
    return render(request, 'school/index.html', {
        'Course':Cours, 
        'Eventss':Eventss, 
        'next_event':upcoming_event,
        'stdn_count':stdn_count,
        'prof_count':prof_count,
        'crs_count' :crs_count,
        'topPost'   :top_posts,
        })

def about(request):
    scount = len(Student.objects.all())
    pcount = len(Professor.objects.all())
    ccount = len(Course.objects.all())

    return render(request, 'school/about.html', {'scount':scount,'pcount':pcount,'ccount':ccount})

def eventss(request):
    old_events = Events.objects.filter(date__lt=datetime.datetime.today())
    new_events = Events.objects.filter(date__gt=datetime.datetime.today())
    return render(request, 'school/events.html', {'old_ev':old_events, 'new_ev':new_events})

def teachersView(request):
    return render(request, 'school/our-teachers.html', {'teachers': Professor.objects.all()})

def singleTeacher(request, pk):
    teacher = Professor.objects.get(pk=pk)
    exp = teacher.professionalExperience.split('\n')
    return render(request, 'school/teachers-single.html', {'teacher':teacher, 'experience':exp}) 

def galleryView(request):
    return render(request, 'school/gallery.html',{'gallery':galleryImages.objects.all()})

class admission_form(CreateView):
    model = Admission
    fields = ['first_name', 'last_name', 'birthdate', 'birthdate', 'niveau', 'telephone','cours_in']
    template_name = 'school/admission-form.html'
    success_url = '/'
    def get_form(self):
        form = super(admission_form, self).get_form()
        form.fields['birthdate'].widget = DateInput(attrs={'type':'date'})
        return form

class contact_form(CreateView):
    model = Cmessage
    fields = ['writer', 'email', 'content']
    template_name = 'school/contact.html'
    success_url = '/contact'

def academics(request):
    return render(request, 'school/academics.html',{'levels':niveaux.Levels,'Courses': Course.objects.all()})

def coursDetails(request, pk):
    prof = Professor.objects.get(cours_in__id=pk)
    course = Course.objects.get(pk=pk)
    return render(request, 'school/course-detail.html', {'course':course, 'prof':prof})

class postListView(ListView):
    model = Post
    template_name = "school/blog.html"
    context_object_name = "posts"
    ordering = ['-date_posted']
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(postListView,self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['vote_sorted_posts'] = Post.objects.all().order_by('votes')
        return context

class postDetailView(DetailView):
    model = Post
    template_name = 'school/blog-post.html'
    def get_context_data(self, **kwargs):
        context = super(postDetailView, self).get_context_data(**kwargs)
        context['categories'] = Categories.objects.all()
        context['vote_sorted_posts'] = Post.objects.all().order_by('votes')
        return context

class catListView(ListView):
    model = Post
    context_object_name = "posts"
    def get_queryset(self):
        return Post.objects.all().filter(category__id = self.kwargs.get('pk'))
    template_name = 'school/category.html'
    ordering = ['-date_posted']
    paginate_by = 5
    def get_context_data(self, **kwargs):                                  
        context = super(catListView, self).get_context_data(**kwargs)   
        context['categories'] = Categories.objects.all()                   
        context['vote_sorted_posts'] = Post.objects.all().order_by('votes')
        return context

# Create your views here.
