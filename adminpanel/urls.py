from django.contrib.auth.decorators import login_required
from django.urls import path                           
from . import views                                    
from .views import (DashBoard, studentsListView,studentupdate, StudentProfile, TeachersListView, 
TeacherProfile, TeacherUpdateView ,coursListView, coursDetailView, salleListView ,newStudent, 
delStudent, newTeacher, delTeacher, newCourse, updateCourse, delCourse, newSalle, delSalle, 
scheduleView, coursList, deletePost, PostUpdateView, NewPost, deleteSub, Cmessages, DeleteMessage, 
catUpdate, catCreate, createEvent, eventUpdate, eventDelete, newImage)

urlpatterns = [                                        
	path('', DashBoard.as_view(), name='dashboard'),
	path('students/', login_required(views.studentsListView.as_view()), name='students'),
	path('students/<int:pk>/', StudentProfile.as_view(), name='detail-student'),
	path('students/new', newStudent.as_view(), name='new-student'),
	path('students/<int:pk>/update',studentupdate.as_view(), name='update-student'),
	path('students/<int:pk>/delete', delStudent.as_view(), name='delete-student'),
        path('students/<int:pk>/validate', login_required(views.validateSub), name="validate-student"),
        path('teachers/', TeachersListView.as_view(), name='teachers'),
        path('teachers/<int:pk>/', TeacherProfile.as_view(), name='detail-teacher'),
        path('teachers/new', newTeacher.as_view(), name='new-teacher'),
        path('teachers/<int:pk>/update',TeacherUpdateView.as_view(), name='update-teacher'),
        path('teachers/<int:pk>/delete', delTeacher.as_view(), name='delete-teacher'),
	path('courses/', coursListView.as_view(), name = 'courses'),
	path('courses/new', newCourse.as_view(), name='new-course'),
        path('courses/<int:pk>/update', updateCourse.as_view(), name = 'update-course'),
	path('courses/<int:pk>/delete', delCourse.as_view(), name='delete-course'),
        path('inscriptions/', login_required(views.subList), name="inscriptions"),
        path('inscriptions/<int:pk>/delete', deleteSub.as_view(), name='delete-inscriptions'),
	path('salles/', salleListView.as_view(), name='salles'),
	path('salles/new', newSalle.as_view(),name='new-salle'),
	path('salles/<int:pk>/delete', delSalle.as_view(), name='delete-salle'),
	path('schedule/', scheduleView.as_view(), name='schedule'),
	path('schedule/<int:pk>/',coursDetailView.as_view(),name='cours-detail'),
	path('charts/', login_required(views.pie_chart), name="charts"),
        path('resetpaiment/<int:pk>', login_required(views.reset_paiment), name='reset-paiment'),
        path('resetcours/<int:pk>', login_required(views.reset_cours_start), name='reset-cours-start'),
        path('setpresence/<int:pk>', login_required(views.set_presence), name='set-presence'),
        path('posts/', login_required(views.blogPosts), name="blog-posts"),
        path('posts/new', NewPost.as_view(), name='new-post'),
        path('posts/<int:pk>/delete', deletePost.as_view(), name="delete-post"),
        path('posts/<int:pk>/update', PostUpdateView.as_view(), name="update-post"),
        path('categories/', login_required(views.catView), name='categories'),
        path('categories/new', catCreate.as_view(), name='create-cat'),
        path('categories/<int:pk>/update', catUpdate.as_view(), name="cat-update"),
        path('categories/<int:pk>/delete', login_required(views.catDelete), name="category-delete"),
        path('events/', login_required(views.eventView), name="events-admin"),
        path('events/new', createEvent.as_view(), name = 'create-event'),
        path('events/<int:pk>/details', login_required(views.eventDetail), name="event-detail"),
        path('events/<int:pk>/update', eventUpdate.as_view(), name="event-update"),
        path('events/<int:pk>/delete', eventDelete.as_view(), name="event-delete"),
        path('gallery/', views.GalleryView, name='gallery'),
        path('gallery/new', newImage.as_view(), name='new-image'),
        path('gallery/<int:pk>/delete', views.delImage, name='delete-image'),
        path('messages/', Cmessages.as_view(), name="messages"),
        path('messages/<int:pk>/details', login_required(views.MessageView), name = "message-detail"),
        path('messages/<int:pk>/delete', DeleteMessage.as_view(), name="message-delete"),
]
