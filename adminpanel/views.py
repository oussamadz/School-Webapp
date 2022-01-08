import datetime, os
from calendar import monthrange
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.forms.widgets import SelectDateWidget
from django.forms import DateInput, DateTimeInput
from django.utils import timezone 

from school.models import Student, Post, Categories, Admission, Events, galleryImages, Cmessage  
from teachers.models import Professor
from courses.models import Course, Salle
from .models import dailyPaiments
from .forms import ValidateForm 

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, TemplateView

def timetable(request):
    return render(request,'adminpanel/timetable.html', {'courses': Course.objects.all()})

def chart_data():
    m_days = monthrange(timezone.now().year, timezone.now().month)[1]
    labels = ['Primaire', "Moyenne", "Secondaire", 'N/A']
    months = ['Jan','Fev','Mar','Avr','Mai','Jun','Jul','Aout','Sep','Oct','Nov','Dec']
    days = [0] * m_days 
    data2 = [0] * 12
    data3 = [0] * 12
    data4 = [0] * m_days 
    data = [0] * 4
    stds = Student.objects.all()
    for std in stds:
        if 'primaire' in std.niveau:
            data[0]+=1
        elif 'moyenne' in std.niveau:
            data[1]+=1
        elif 'secondaire' in std.niveau:
            data[2]+=1
        elif 'N/A' in std.niveau:
            data[3]+=1
        if std.sub_date.month == 1:
            data2[0]+=1
        elif std.sub_date.month == 2:
            data2[1]+=1
        elif std.sub_date.month == 3:
            data2[2]+=1
        elif std.sub_date.month == 4:
            data2[3]+=1
        elif std.sub_date.month == 5:
            data2[4]+=1
        elif std.sub_date.month == 6:
            data2[5]+=1
        elif std.sub_date.month == 7:
            data2[6]+=1
        elif std.sub_date.month == 8:
            data2[7]+=1
        elif std.sub_date.month == 9:
            data2[8]+=1
        elif std.sub_date.month == 10:
            data2[9]+=1
        elif std.sub_date.month == 11:
            data2[10]+=1
        elif std.sub_date.month == 12:
            data2[11]+=1
        
    for pnt in dailyPaiments.objects.all():
        if pnt.day.month == 1:
            data3[0]+= pnt.count
        elif pnt.day.month == 2:
            data3[1]+= pnt.count
        elif pnt.day.month == 3:
            data3[2]+= pnt.count
        elif pnt.day.month == 4:
            data3[3]+= pnt.count
        elif pnt.day.month == 5:
            data3[4]+= pnt.count
        elif pnt.day.month == 6:
            data3[5]+= pnt.count
        elif pnt.day.month == 7:
            data3[6]+= pnt.count
        elif pnt.day.month == 8:
            data3[7]+= pnt.count
        elif pnt.day.month == 9:
            data3[8]+= pnt.count
        elif pnt.day.month == 10:
            data3[9]+= pnt.count
        elif pnt.day.month == 11:
            data3[10]+= pnt.count
        elif pnt.day.month == 12:
            data3[11]+= pnt.count
    for i in range(m_days):
        days[i] = i+1
        for pnt in dailyPaiments.objects.filter(day__year = datetime.date.today().year, day__month = datetime.date.today().month):
            if pnt.day.day == i+1:
                data4[i]+=pnt.count
            



    return [labels, months, days, data, data2, data3, data4]




def pie_chart(request):

    return render(request,'adminpanel/charts.html', {'labels':chart_data()[0], 'data':chart_data()[3], 'months':chart_data()[1], 'data2':chart_data()[4], 'data3':chart_data()[5],'days':chart_data()[2], 'data4':chart_data()[6]})

def set_presence(request, pk):
    stdn = Student.objects.get(pk=pk)
    date_string = ',' + str(datetime.date.today())
    stdn.presence += date_string
    stdn.save()
    messages.success(request, f'Student {stdn.first_name} {stdn.last_name} present.')
    return redirect('cours-detail',pk=(stdn.cours_in.id))


def reset_paiment(request, pk):
    stdn = Student.objects.get(pk=pk)
    stdn.cours_start = stdn.cours_start + relativedelta(months=1)
    stdn.save()

    if dailyPaiments.objects.filter(day = datetime.date.today()).count() != 0:
        existing_paiment = dailyPaiments.objects.filter(day = datetime.date.today())[0]
        existing_paiment.count += stdn.cours_in.price
        existing_paiment.save()
    else:
        todaycount = dailyPaiments(day=datetime.date.today(), count = stdn.cours_in.price)
        todaycount.save()
    return redirect('cours-detail',pk=(stdn.cours_in.id))

def reset_cours_start(request, pk):
        cours = Course.objects.get(pk=pk)
        cours.cours_start = cours.cours_start + relativedelta(months=1)
        cours.save()
        return redirect('cours-detail', pk=cours.id)


class DashBoard(LoginRequiredMixin, ListView):
    model = Cmessage
    template_name = "adminpanel/dashboard.html"
    def get_context_data(self, **kwargs):
        context = super(DashBoard,self).get_context_data(**kwargs)
        context['cmessage'] = Cmessage.objects.filter(read=False)
        context['scount'] = len(Student.objects.all())
        context['pcount'] = len(Professor.objects.all())
        context['ccount'] = len(Course.objects.all())
        context['inscount'] = len(Admission.objects.all())
        context['months'] = chart_data()[1]
        context['labels'] = chart_data()[0]
        context['data']   = chart_data()[3]
        context['data2']  =  chart_data()[4]
        return context
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class studentsListView(LoginRequiredMixin,ListView):
	model = Student
	template_name = 'adminpanel/students.html'
	context_object_name = 'Student'
	#ordering = ['sub_date']

class StudentProfile(LoginRequiredMixin, DetailView):
	model = Student
	template_name = 'adminpanel/studentProfile.html'

class studentupdate(LoginRequiredMixin, UpdateView):
	model = Student
	fields = ['first_name', 'last_name','birthdate','niveau','telephone', 'cours_in', 'cours_start', 'presence', 'image']
	success_url = '/adminpanel/students'
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		student = self.get_object()
		return True

class newStudent(LoginRequiredMixin, CreateView):
    model = Student
    fields = ['first_name', 'last_name','birthdate','niveau','telephone', 'cours_in', 'cours_start', 'image']
    success_url = '/adminpanel/students'
    def get_form(self):
        from django.forms.widgets import SelectDateWidget
        from django.forms import DateInput
        form = super(newStudent, self).get_form()
        form.fields['birthdate'].widget = DateInput(attrs={'type':'date'})
        form.fields['cours_start'].widget = DateInput(attrs={'type':'date'})
        return form

def validateSub(request, pk):
    sub = Admission.objects.get(pk=pk)  
    admission_data = {                  
            'first_name':sub.first_name,
            'last_name':sub.last_name,  
            'birthdate':sub.birthdate,  
            'telephone':sub.telephone,
            'niveau':sub.niveau,        
            'cours_in':sub.cours_in     
            }                           
    new_student = Student
    FR = ValidateForm(request.POST or None, initial=admission_data, instance=Student())
    context = {
            'form': FR,
            }
    if FR.is_valid():
        FR.save()
        Admission.objects.get(pk=pk).delete()
        return redirect('students')
    success_url = '/'
    return render(request, 'adminpanel/validate_sub.html', context)


class delStudent(LoginRequiredMixin, DeleteView):
	model = Student
	success_url = '/adminpanel/students'


class TeachersListView(LoginRequiredMixin, ListView):
	model = Professor
	template_name = 'adminpanel/teachers.html'
	context_object_name = 'Teacher'

class TeacherProfile(DetailView):
        model = Professor
        template_name = 'adminpanel/profProfile.html'


class newTeacher(LoginRequiredMixin, CreateView):
    model = Professor
    fields = ['first_name','last_name','phone','cours_in','cours_start', 'professionalExperience','image']
    success_url = '/adminpanel/teachers'
    def get_form(self):
        form = super(newTeacher, self).get_form()
        form.fields['cours_start'].widget = DateInput(attrs={'type':'date'})
        return form


class TeacherUpdateView(LoginRequiredMixin, UpdateView):
        model = Professor
        fields=['first_name','last_name','phone','cours_in','cours_start', 'professionalExperience','image']
        success_url = '/adminpanel/teachers'
        def form_valid(self,form):
                form.instance.author = self.request.user
                return super().form_valid(form)
        def test_func(self):
                prof = self.get_object()
                return True

class delTeacher(LoginRequiredMixin,DeleteView):
	model = Professor
	success_url = '/adminpanel/teachers'

class coursListView(LoginRequiredMixin,ListView):
	model = Course
	template_name = 'adminpanel/courses.html'
	context_object_name = 'Course'
	paginate_by = 20

class newCourse(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['name', 'niveau', 'price', 'cours_start', 'time','wday1', 'time2','wday2','sal','prof']
    success_url = '/adminpanel/courses'
    def get_form(self):
        form = super(newCourse, self).get_form()
        form.fields['cours_start'].widget = DateInput(attrs={'type':'date'})
        return form

class updateCourse(LoginRequiredMixin, UpdateView):
    model = Course
    fields = ['name', 'niveau', 'price', 'cours_start', 'time','wday1', 'time2', 'wday2','sal','prof']
    success_url = '/adminpanel/courses'
    def test_func(self):
        course = self.get_object()
        return true


class delCourse(LoginRequiredMixin, DeleteView):
	model = Course
	success_url = '/adminpanel/courses'

class salleListView(LoginRequiredMixin, ListView):
	model = Salle
	template_name = 'adminpanel/salles.html'
	context_object_name = 'Salle'

class newSalle(LoginRequiredMixin, CreateView):
	model = Salle
	fields = ['name', 'capacity']
	success_url = '/adminpanel/salles'

class delSalle(LoginRequiredMixin, DeleteView):
	model = Salle
	success_url = '/adminpanel/salles'

class scheduleView(LoginRequiredMixin, ListView):
	model = Course
	template_name = 'adminpanel/schedule.html'
	context_object_name = 'Course'
	ordering = ["time","time2"]

class coursList(LoginRequiredMixin, DetailView):
        model = Course 
        context_object_name = 'course'
        template_name = 'adminpanel/coursTable.html'
        def get_context_data(self, **kwargs):
                context = super(sallescheduleView,self).get_context_data(**kwargs)
                context['cours'] = Course.objects.all()
                return context

class coursDetailView(LoginRequiredMixin, DetailView):
        model = Course
        template_name = 'adminpanel/cours_details.html'

        def get_context_data(self, **kwargs):
                count = 0
                for std in Student.objects.filter(cours_in=Course.objects.get(pk=self.kwargs['pk'])):
                        count+=std.month_presence()
                result = Course.objects.get(pk=self.kwargs['pk']).calc_paiment(count)

                context = super(coursDetailView, self).get_context_data(**kwargs)
                context['student'] = Student.objects.all()
                context['prof'] = Professor.objects.all()
                context['fuller'] = "{:.2f}".format(result)
                return context

def subList(request):
    subs = Admission.objects.all()
    return render(request, 'adminpanel/inscriptions.html', {'subs':subs})

class deleteSub(LoginRequiredMixin, DeleteView):
    model = Admission
    success_url = "/adminpanel/inscriptions"

def blogPosts(request):
    posts = Post.objects.all().order_by('date_posted')
    return render(request, 'adminpanel/blog_posts.html',{'posts':posts})

class NewPost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'content']
    success_url = '/adminpanel/posts'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class deletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/adminpanel/posts"

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post    
    fields=['title','category','content']
    success_url = '/adminpanel/posts/'
    def form_valid(self,form):
        form.instance.author = self.request.user 
        return super().form_valid(form)                                                    
    def test_func(self):
        post = self.get_object()
        return True

def catView(request):
    cats = Categories.objects.all()
    return render(request, 'adminpanel/categories.html', {'categories':cats})

class catCreate(LoginRequiredMixin, CreateView):
    model = Categories
    fields = ['name']
    success_url = "/adminpanel/categories"

class catUpdate(LoginRequiredMixin, UpdateView):
    model = Categories
    fields = ['name']
    success_url = "/adminpanel/categories"

def catDelete(request,pk):
    cat = Categories.objects.get(pk=pk)
    cat.delete()
    messages.warning(request, f'Category {cat.name} deleted.')
    return redirect('categories')

def eventView(request):
    evs = Events.objects.all()
    return render(request, 'adminpanel/events.html', {'events':evs})

class createEvent(LoginRequiredMixin, CreateView):
    model = Events
    fields = ['title', 'date', 'content', 'photo']
    success_url = "/adminpanel/events"
    def get_form(self):
        form = super(createEvent, self).get_form()
        form.fields['date'].widget = DateTimeInput(attrs={'type':'datetime-local', 'placeholder':'0000-00-00T00:00'})
        return form

class eventUpdate(LoginRequiredMixin, UpdateView):
    model = Events
    fields = ['title', 'date', 'content', 'photo']
    success_url = '/adminpanel/events'
    def get_form(self):
        form = super(eventUpdate, self).get_form()
        form.fields['date'].widget = DateTimeInput(attrs={'type':'datetime-local', 'placeholder':'0000-00-00T00:00'})
        return form

def eventDetail(request, pk):
    ev = Events.objects.get(pk=pk)
    return render(request, 'adminpanel/event-detail.html', {'ev':ev})

class eventDelete(LoginRequiredMixin, DeleteView):
    model = Events
    success_url = '/adminpanel/events'

def GalleryView(request):
    gal = galleryImages.objects.all()
    images_dictionary = []
    for idx, obj in enumerate(gal):
        images_dictionary.append([idx+1, obj])
    return render(request, 'adminpanel/gallery.html', {'gallery':images_dictionary})

class newImage(LoginRequiredMixin, CreateView):
    model = galleryImages
    fields = ['title', 'image']
    success_url = '/adminpanel/gallery'

def delImage(request, pk):
    image = galleryImages.objects.get(pk=pk)
    img_path = image.image.name
    os.remove('profiles_pics/'+img_path)
    image.delete()
    messages.warning(request, f'Image "{image.title}" deleted.')
    return redirect('gallery')

class Cmessages(LoginRequiredMixin, ListView):
    model = Cmessage
    template_name = 'adminpanel/messages.html'
    context_object_name = "cmessages"

def MessageView(request, pk):
    msg = Cmessage.objects.get(pk=pk)
    msg.read=True
    msg.save()
    return render(request, 'adminpanel/message_details.html', {'msg':msg})

class DeleteMessage(LoginRequiredMixin, DeleteView):
    model = Cmessage
    success_url = '/adminpanel/messages'

# Create your views here.
