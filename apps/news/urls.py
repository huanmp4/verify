from django.urls import path
from .import views

app_name = 'news'
urlpatterns = [
    path('',views.index,name='index'),
    path('discover',views.Discover_Process.as_view(),name='discover'),
]