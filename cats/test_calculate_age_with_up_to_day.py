from unittest import TestCase

from datetime import date

from cats.birthday import calc_age_uptoday, YEARS, MONTHS, DAYS


class TestCalcAgeUpToDay(TestCase):
    birthday = date(year=1993, month=11, day=9)

    before_birthday = date(year=2017, month=11, day=8)
    now_birthday = date(year=2017, month=11, day=9)
    later_birthday = date(year=2017, month=11, day=10)

    before_month_birthday = date(year=2017, month=10, day=9)
    now_month_birthday = date(year=2017, month=11, day=9)
    later_month_birthday = date(year=2017, month=12, day=9)

    before_year_birthday = date(year=2016, month=11, day=9)
    now_year_birthday = date(year=2017, month=11, day=9)
    later_year_birthday = date(year=2018, month=11, day=9)

    def test_calc_years(self):
        self.assertEqual(calc_age_uptoday(self.birthday, self.before_birthday)[YEARS], 23)
        self.assertEqual(calc_age_uptoday(self.birthday, self.now_birthday)[YEARS], 24)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_birthday)[YEARS], 24)
        self.assertEqual(calc_age_uptoday(self.birthday, self.before_birthday)[YEARS], 23)
        self.assertEqual(calc_age_uptoday(self.birthday, self.now_birthday)[YEARS], 24)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_birthday)[YEARS], 24)
        self.assertEqual(calc_age_uptoday(self.birthday, self.before_birthday)[YEARS], 23)
        self.assertEqual(calc_age_uptoday(self.birthday, self.now_birthday)[YEARS], 24)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_birthday)[YEARS], 24)

    def test_calc_uptodate(self):
        birthday = self.birthday

        now = self.before_birthday
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 23, MONTHS: 11, DAYS: 30}
        m = 'day check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        now = self.now_birthday
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 24, MONTHS: 0, DAYS: 0}
        m = 'day check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        now = self.later_birthday
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 24, MONTHS: 0, DAYS: 1}
        m = 'day check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        now = self.before_month_birthday
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 23, MONTHS: 11, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        now = self.now_month_birthday
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 24, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        now = self.later_month_birthday
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 24, MONTHS: 1, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        # now = date(2017, 9, 7)
        # birthday = date(2016, 10, 31)
        # d1 = calc_age_uptoday(birthday, now)
        # d2 = {YEARS: 24, MONTHS: 1, DAYS: 0}
        # m = 'month check - birthday: {b}, date: {d}'
        # self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        # now = date(2017, 10, 30)
        # birthday = date(2016, 10, 31)
        # d1 = calc_age_uptoday(birthday, now)
        # d2 = {YEARS: 0, MONTHS: 11, DAYS: 30}
        # m = 'month check - birthday: {b}, date: {d}'
        # self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))
        #
        # now = date(2017, 10, 31)
        # birthday = date(2016, 10, 31)
        # d1 = calc_age_uptoday(birthday, now)
        # d2 = {YEARS: 1, MONTHS: 0, DAYS: 0}
        # m = 'month check - birthday: {b}, date: {d}'
        # self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))
        #
        # now = date(2017, 11, 1)
        # birthday = date(2016, 10, 31)
        # d1 = calc_age_uptoday(birthday, now)
        # d2 = {YEARS: 1, MONTHS: 0, DAYS: 1}
        # m = 'month check - birthday: {b}, date: {d}'
        # self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))


