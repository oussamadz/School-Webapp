from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import postListView, postDetailView, admission_form, coursDetails, catListView, contact_form

urlpatterns = [
	path('',views.home, name='blog-home'),
	path('about/', views.about, name='about'),
        path('admission/', admission_form.as_view(), name='admission'),
        path('academics/',views.academics, name='academics'),
        path('academics/<int:pk>', views.coursDetails,name='cours-details'),
        path('blog/', postListView.as_view(), name="blog2-home"),
        path('blog/cat/<int:pk>',catListView.as_view(), name='category'),
        path('blog/post/<int:pk>', postDetailView.as_view(), name='post-detail'),
        path('events/', views.eventss, name='events'),
        path('contact/', contact_form.as_view(), name='contact'),
        path('teachers/', views.teachersView, name='blog-teachers'),
        path('teachers/<int:pk>', views.singleTeacher, name="blogTeacherDetails"),
        path('gallery/', views.galleryView, name="gallery"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
