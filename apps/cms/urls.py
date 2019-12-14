from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'cms'
urlpatterns = [
    path('home',views.home,name = 'home'),
    path('news_release',views.news_release,name = 'news_release'),
    path('release_news',views.ReleaseNews.as_view(),name = 'release_news'),
    path('category',views.category,name = 'category'),
    path('category_thumbnail',views.category_thumbnail,name = 'category_thumbnail'),
    path('category_modify',views.category_modify,name = 'category_modify'),
    path('category_delete',views.category_delete,name = 'category_delete'),
    path('thumbnail_process',views.thumbnail_process,name = 'thumbnail_process'),
]+static(settings.CLIENTIMAGE_ROOT,document_root = settings.CLIENTIMAGE_ROOT)