from django.urls import path
from . import views

app_name = 'sampleapp'

urlpatterns = [
    path('month/', views.MonthCalendar.as_view(), name='month'),
    path('month/<int:year>/<int:month>/', views.MonthCalendar.as_view(), name='month'),
    path('', views.WeekCalendar.as_view(), name='week'),
    path('week/<int:year>/<int:month>/<int:day>/', views.WeekCalendar.as_view(), name='week'),
    path('week_with_schedule/', views.WeekWithScheduleCalendar.as_view(), name='week_with_schedule'),
    path('week_with_schedule/<int:year>/<int:month>/<int:day>/', views.WeekWithScheduleCalendar.as_view(), name='week_with_schedule'),
]