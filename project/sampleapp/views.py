from django.views import generic
from scalender.views import MonthCalendarMixin, WeekCalendarMixin, WeekWithScheduleMixin

# Create your views here.

class MonthCalendar(MonthCalendarMixin, generic.TemplateView):
    template_name = 'sampleapp/month.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = self.get_month_calendar()
        return context

class WeekCalendar(WeekCalendarMixin, generic.TemplateView):
    template_name = 'sampleapp/week.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['week'] = self.get_week_calendar()
        return context
    
class WeekWithScheduleCalendar(WeekWithScheduleMixin, generic.TemplateView):
    template_name = 'sampleapp/week_with_schedule.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        week = self.get_week_calendar()
        context['week'] = week
        context['week_row'] = zip(
            week['week_names'],
            week['days'],
            week['schedule_list']
        )
        return context