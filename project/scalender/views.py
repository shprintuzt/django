import calendar
from collections import deque
import datetime
from .models import Schedule

# Create your views here.

class BaseCalendarMixin:
    first_weekday = 0
    week_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    def setup(self):
        self._calendar = calendar.Calendar(self.first_weekday)
        
    def get_week_names(self):
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        return week_names
    
class MonthCalendarMixin(BaseCalendarMixin):

    @staticmethod
    def get_previous_month(date):
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
        else:
            return date.replace(month=date.month-1, day=1)
        
    @staticmethod
    def get_next_month(date):
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
        else:
            return date.replace(month=date.month+1, day=1)
        
    def get_month_days(self, date):
        return self._calendar.monthdatescalendar(date.year, date.month)
    
    def get_current_month(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month
    
    def get_month_calendar(self):
        self.setup()
        current_month = self.get_current_month()
        calendar_data = {
            'now': datetime.date.today(),
            'days': self.get_month_days(current_month),
            'current': current_month,
            'previous': self.get_previous_month(current_month),
            'next': self.get_next_month(current_month),
            'week_names': self.get_week_names(),
        }
        return calendar_data
    
class WeekCalendarMixin(BaseCalendarMixin):
    
    def get_week_days(self):
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        day = self.kwargs.get('day')
        if month and year and day:
            date = datetime.date(year=int(year), month=int(month), day=int(day))
        else:
            date = datetime.date.today().replace(day=1)
        for week in self._calendar.monthdatescalendar(date.year, date.month):
            if date in week:
                return week
            
    def get_week_calendar(self):
        self.setup()
        days = self.get_week_days()
        first = days[0]
        last = days[-1]
        calendar_data = {
            'now': datetime.date.today(),
            'days': days,
            'previous': first - datetime.timedelta(days=7),
            'next': first + datetime.timedelta(days=7),
            'week_names': self.get_week_names(),
            'first': first,
            'last': last,
        }
        return calendar_data
    
class WeekWithScheduleMixin(WeekCalendarMixin):
    model = Schedule
    date_field = 'date'
    order_field = 'start_time'
    
    def get_week_schedules(self, days):
        for day in days:
            lookup = {self.date_field: day}
            queryset = self.model.objects.filter(**lookup)
            if self.order_field:
                queryset = queryset.order_by(self.order_field)
            yield queryset
            
    def get_week_calendar(self):
        calendar_data = super().get_week_calendar()
        schedules = self.get_week_schedules(calendar_data['days'])
        calendar_data['schedule_list'] = schedules
        return calendar_data