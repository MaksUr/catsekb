from unittest import TestCase

from datetime import date

from cats.birthday import calc_age_uptoday, YEARS, MONTHS, DAYS


class TestCalcAgeUpToDay(TestCase):
    birthday = date(year=1993, month=11, day=9)

    now_birthday = date(year=2017, month=11, day=9)

    before_birthday = date(year=2017, month=11, day=8)
    later_birthday = date(year=2017, month=11, day=10)

    before_month_birthday = date(year=2017, month=10, day=9)
    later_month_birthday = date(year=2017, month=12, day=9)

    before_year_birthday = date(year=2016, month=11, day=9)
    later_year_birthday = date(year=2018, month=11, day=9)

    def test_calc_one_year(self):
        res = calc_age_uptoday(date(2017, 5, 6), date(2018, 5, 6))
        self.assertEqual(res[YEARS], 1)

    def test_calc_age_uptoday_month(self):
        res = calc_age_uptoday(date(2017, 11, 30), date(2017, 12, 29))
        self.assertEqual(res[MONTHS], 0)

        res = calc_age_uptoday(date(2017, 11, 30), date(2017, 12, 30))
        self.assertEqual(res[MONTHS], 1)

        res = calc_age_uptoday(date(2017, 11, 30), date(2017, 12, 31))
        self.assertEqual(res[MONTHS], 1)

        res = calc_age_uptoday(date(2017, 11, 30), date(2018, 1, 29))
        self.assertEqual(res[MONTHS], 1)

        res = calc_age_uptoday(date(2017, 11, 30), date(2018, 1, 30))
        self.assertEqual(res[MONTHS], 2)

        res = calc_age_uptoday(date(2017, 11, 30), date(2018, 2, 27))
        self.assertEqual(res[MONTHS], 2)
        #
        # res = calc_age_uptoday(date(2017, 11, 30), date(2018, 2, 28))
        # self.assertEqual(res[MONTHS], 3)

        # res = calc_age_uptoday(date(2017, 11, 30), date(2018, 3, 1))
        # self.assertEqual(res[MONTHS], 3)
        #
        # res = calc_age_uptoday(date(2017, 11, 30), date(2018, 3, 29))
        # self.assertEqual(res[MONTHS], 3)
        #
        # res = calc_age_uptoday(date(2017, 11, 30), date(2018, 3, 30))
        # self.assertEqual(res[MONTHS], 4)

    def test_calc_age_uptoday_one_month_before(self):
        res = calc_age_uptoday(date(2016, 11, 30), date(2017, 10, 29))
        self.assertEqual(res[MONTHS], 10)

        res = calc_age_uptoday(date(2016, 11, 30), date(2017, 10, 30))
        self.assertEqual(res[MONTHS], 11)

        res = calc_age_uptoday(date(2016, 11, 30), date(2017, 10, 31))
        self.assertEqual(res[MONTHS], 11)

        res = calc_age_uptoday(date(2016, 11, 30), date(2017, 11, 1))
        self.assertEqual(res[MONTHS], 11)

        res = calc_age_uptoday(date(2016, 11, 30), date(2017, 10, 29))
        self.assertEqual(res[MONTHS], 11)

        res = calc_age_uptoday(date(2016, 11, 30), date(2017, 11, 30))
        self.assertEqual(res[MONTHS], 0)

    def test_calc_one_month_later(self):
        res = calc_age_uptoday(date(2017, 11, 30), date(2017, 12, 31))
        self.assertEqual(res[MONTHS], 1)

    def test_calc_one_day(self):
        res = calc_age_uptoday(date(2017, 12, 30), date(2017, 12, 31))
        self.assertEqual(res[DAYS], 1)

    def test_calc_years(self):
        self.assertEqual(calc_age_uptoday(self.birthday, self.now_birthday)[YEARS], 24)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_birthday)[YEARS], 23)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_birthday)[YEARS], 24)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_month_birthday)[YEARS], 23)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_month_birthday)[YEARS], 24)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_year_birthday)[YEARS], 23)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_year_birthday)[YEARS], 25)


        
    def test_calc_month(self):
        self.assertEqual(calc_age_uptoday(self.birthday, self.now_birthday)[MONTHS], 0)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_birthday)[MONTHS], 11)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_birthday)[MONTHS], 0)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_month_birthday)[MONTHS], 10)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_month_birthday)[MONTHS], 1)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_year_birthday)[MONTHS], 0)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_year_birthday)[MONTHS], 0)

    def test_calc_day(self):
        self.assertEqual(calc_age_uptoday(self.birthday, self.now_birthday)[DAYS], 0)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_birthday)[DAYS], 30)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_birthday)[DAYS], 1)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_month_birthday)[DAYS], 0)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_month_birthday)[DAYS], 0)

        self.assertEqual(calc_age_uptoday(self.birthday, self.before_year_birthday)[DAYS], 0)
        self.assertEqual(calc_age_uptoday(self.birthday, self.later_year_birthday)[DAYS], 0)

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

        now = self.later_month_birthday
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 24, MONTHS: 1, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        #####################
        now = date(2017, 9, 7)
        birthday = date(2016, 10, 31)
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 0, MONTHS: 11, DAYS: 8}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        now = date(2017, 10, 30)
        birthday = date(2016, 10, 31)
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 0, MONTHS: 11, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        now = date(2017, 10, 31)
        birthday = date(2016, 10, 31)
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 1, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))

        now = date(2017, 11, 1)
        birthday = date(2016, 10, 31)
        d1 = calc_age_uptoday(birthday, now)
        d2 = {YEARS: 1, MONTHS: 0, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(d1, d2, msg=m.format(b=birthday, d=now))


