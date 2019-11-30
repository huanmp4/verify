from django.urls import path
from . import views
app_name = 'search'
urlpatterns = [
    path('index',views.search_index,name='index')
]