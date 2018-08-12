from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('logged_out', views.logged_out, name='logged_out'),
]