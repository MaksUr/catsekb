from unittest import TestCase

from datetime import date

from cats.birthday import calc_age_uptoday, YEARS, MONTHS, DAYS


class TestCalcAgeUpToDay(TestCase):
    def test_clc_uptoday_from_30_10_2017_to_01_02_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 2, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 3, DAYS: 2}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_27_02_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 2, 27)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 3, DAYS: 28}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_28_02_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 2, 28)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 3, DAYS: 29}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_01_03_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 3, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 4, DAYS: -1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_29_03_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 3, 29)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 4, DAYS: 27}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_30_03_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 3, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 5, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_31_03_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 3, 31)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 5, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_29_10_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 10, 29)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 11, DAYS: 29}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_30_10_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 10, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 1, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_01_11_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 11, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 1, MONTHS: 0, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_12_1993(self):
        start_date = date(1993, 12, 31)
        end_date = date(1993, 12, 31)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_01_1994(self):
        start_date = date(1993, 12, 31)
        end_date = date(1994, 1, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 0, MONTHS: 0, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_12_2017(self):
        start_date = date(1993, 12, 31)
        end_date = date(2017, 12, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 23, MONTHS: 11, DAYS: 29}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_12_2017(self):
        start_date = date(1993, 12, 31)
        end_date = date(2017, 12, 31)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_01_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 1, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 0, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_01_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 1, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 0, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_01_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 1, 31)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 1, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_02_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 2, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 1, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_27_02_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 2, 27)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 1, DAYS: 27}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_28_02_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 2, 28)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 1, DAYS: 28}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_03_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 3, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 2, DAYS: -2}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_03_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 3, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 2, DAYS: 27}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_03_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 3, 31)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 3, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_04_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 4, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 3, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_04_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 4, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 3, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_05_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 5, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 4, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_05_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 5, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 4, DAYS: 29}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_05_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 5, 31)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 5, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_06_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 6, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 5, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_06_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 6, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 5, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_07_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 7, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 6, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_07_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 7, 30)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 6, DAYS: 29}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_07_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 7, 31)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 7, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_01_08_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 8, 1)
        res = calc_age_uptoday(start_date, end_date)
        check = {YEARS: 24, MONTHS: 7, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

