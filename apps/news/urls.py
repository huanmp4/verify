from django.urls import path
from .import views

app_name = 'news'
urlpatterns = [
    path('',views.index,name='index'),
    path('discover',views.Discover_Process,name='discover'),
    path('news_list',views.news_list,name='news_list'),
    path('news_detail/<int:news_id>',views.news_detail,name='news_detail'),
    path('news_comment',views.news_comment,name='news_comment'),

]