from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.myview, name='myview'),
    path('logged_out', views.logged_out, name='logged_out'),
]