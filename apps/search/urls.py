from django.urls import path,include
from . import views
app_name = 'search'
urlpatterns = [
    # path('index',include('haystack.urls'),name='index'),
    path('index',views.SearchPagi.as_view(),name='index'),
]