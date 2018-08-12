from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('create_group/', views.CreateGroup.as_view(), name='create_group'),
    path('detail_group/<str>/', views.DetailGroup.as_view(), name='detail_group'),
    path('logged_out/', views.logged_out, name='logout'),
    path('login/', views.Login.as_view(), name='login'),
]