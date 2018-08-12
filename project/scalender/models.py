import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Schedule(models.Model):
    summary = models.CharField('Title', max_length=50)
    description = models.TextField('Descripition', blank=True)
    start_time = models.TimeField('Start time', default=datetime.time(7, 0, 0))
    end_time = models.TimeField('End time', default=datetime.time(7, 0, 0))
    date = models.DateField('Date')
    created_at = models.DateTimeField('Created', default=timezone.now)
    
    def __str__(self):
        return self.summary