from django.urls import path
from . import views
app_name = 'course'
urlpatterns = [
    path('index',views.course_index,name ='index'),
    path('detail',views.course_detail,name = 'detail'),
    path('course_detail/<int:course_id>',views.course_detail,name = 'course_detail'),
    path('course_token',views.course_token,name = 'course_token'),
    path('course_order_key',views.course_order_key,name = 'course_order_key'),
    path('notify_view',views.notify_view,name = 'notify_view'),
    path('course_pay/<int:course_id>',views.course_pay,name = 'course_pay'),
    path('login_requireds',views.login_requireds,name = 'login_requireds'),
]