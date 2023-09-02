# utils.py

from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, events=None):
        self.year = year
        self.month = month
        self.events = events
        super(Calendar, self).__init__()

    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        cell_class = ''

        for event in events_per_day:
            cell_class = 'event-day' if event.start_time.day <= day <= event.end_time.day else ''
            d += f'<li class="{cell_class}"> {event.title} </li>'

            if event:
                cell_class = 'event-day-yes'
            else:
                cell_class = ''

        if day != 0:
            return f"<td class='{cell_class}'><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    def formatweek(self, theweek):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, self.events)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week)}\n'
        return cal