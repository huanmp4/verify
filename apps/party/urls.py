from django.urls import path
from .import views

app_name = 'party'
urlpatterns = [
    path('',views.index,name='index'),
    path('comment',views.comment,name='comment'),
    path('write',views.write,name='write'),
    path('delete',views.delete,name='delete'),
]