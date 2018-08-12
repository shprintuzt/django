from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.MesIndexView.as_view(), name='index'),
    path('add/', views.MesAddView.as_view(), name='add'),
    path('change/<int:pk>/', views.MesChangeView.as_view(), name='change'),
    path('delete/<int:pk>/', views.MesDeleteView.as_view(), name='delete'),
    path('create_user/', views.UserCreateView.as_view(), name='create_user'),
]