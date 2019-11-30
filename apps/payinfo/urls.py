from django.urls import path
from . import views
app_name = 'pay'
urlpatterns = [
    path('payinfo',views.payinfo,name='payinfo')
]