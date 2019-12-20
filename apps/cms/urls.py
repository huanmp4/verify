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
    path('image_upload_to_local',views.image_upload_to_local,name = 'image_upload_to_local'),
    path('category_modify',views.category_modify,name = 'category_modify'),
    path('category_delete',views.category_delete,name = 'category_delete'),
    path('thumbnail_process',views.thumbnail_process,name = 'thumbnail_process'),
    path('banner_control',views.banner_control,name = 'banner_control'),
    path('banner_cms_manager_get', views.banner_cms_manager_get, name='banner_cms_manager_get'),
    path('banner_cms_manager_add', views.banner_cms_manager_add, name='banner_cms_manager_add'),
    path('banner_cms_manager_edit', views.banner_cms_manager_edit, name='banner_cms_manager_edit'),
    path('banner_cms_manager_delete', views.banner_cms_manager_delete, name='banner_cms_manager_delete'),
    path('news_cms_manager', views.news_cms_manager, name='news_cms_manager'),
]+static(settings.CLIENTIMAGE_ROOT,document_root = settings.CLIENTIMAGE_ROOT)