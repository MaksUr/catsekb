# TODO: delete this file
from datetime import date
from dateutil.rrule import rrule, YEARLY, MONTHLY, DAILY




def get_time_delta(date, round=ROUND_DAY):
    """

    :type round: str
    :type date: datetime
    """


birthday = date(year=2015, month=9, day=6)
now = date.today()
delta = now - birthday
print('Лет', rrule(YEARLY, dtstart=birthday, until=now).count())
print('Месяцев', rrule(MONTHLY, dtstart=birthday, until=now).count())
print('Дней', rrule(DAILY, dtstart=birthday, until=now).count())

print('Дней: ', delta)









