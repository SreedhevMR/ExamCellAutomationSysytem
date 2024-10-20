from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 
  
  path('admin_page/',views.admin_page,name='admin_page'),
  path('admin_student',views.admin_student,name='a_student'),
  path('admin_teacher',views.admin_teacher,name='a_teacher')

] 



