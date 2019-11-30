from django.urls import path
from . import views
app_name = 'course'
urlpatterns = [
    path('index',views.course_index,name ='index'),
    path('detail',views.course_detail,name = 'detail'),
]