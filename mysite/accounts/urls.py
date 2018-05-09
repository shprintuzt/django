# -*- coding: utf-8 -*-
"""
Created on Wed May  9 20:22:03 2018

@author: T-GOTOH
"""

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('<int:question_id>/vote/', views.vote, name='vote'),
]