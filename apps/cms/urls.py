from django.urls import path
from . import views
app_name = 'cms'
urlpatterns = [
    path('home',views.home,name = 'home'),
    path('news_release',views.news_release,name = 'news_release'),
    path('release_news',views.ReleaseNews,name = 'release_news'),
    path('category',views.category,name = 'category'),
    path('category_thumbnail',views.category_thumbnail,name = 'category_thumbnail'),

]