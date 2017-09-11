from unittest import TestCase

from datetime import date

from cats.birthday import calc_age_uptoday, YEARS, MONTHS, DAYS


class TestCalcAgeUpToDay(TestCase):
    def test_clc_uptoday_from_30_10_2017_to_1_2_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 2, 1)
        check = {YEARS: 0, MONTHS: 3, DAYS: 2}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_27_2_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 2, 27)
        check = {YEARS: 0, MONTHS: 3, DAYS: 28}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_28_2_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 2, 28)
        check = {YEARS: 0, MONTHS: 4, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_1_3_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 3, 1)
        check = {YEARS: 0, MONTHS: 4, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_29_3_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 3, 29)
        check = {YEARS: 0, MONTHS: 4, DAYS: 29}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_30_3_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 3, 30)
        check = {YEARS: 0, MONTHS: 5, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_31_3_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 3, 31)
        check = {YEARS: 0, MONTHS: 5, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_29_10_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 10, 29)
        check = {YEARS: 0, MONTHS: 11, DAYS: 29}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_30_10_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 10, 30)
        check = {YEARS: 1, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_30_10_2017_to_1_11_2018(self):
        start_date = date(2017, 10, 30)
        end_date = date(2018, 11, 1)
        check = {YEARS: 1, MONTHS: 0, DAYS: 2}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_12_1993(self):
        start_date = date(1993, 12, 31)
        end_date = date(1993, 12, 31)
        check = {YEARS: 0, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_1_1994(self):
        start_date = date(1993, 12, 31)
        end_date = date(1994, 1, 1)
        check = {YEARS: 0, MONTHS: 0, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_12_2017(self):
        start_date = date(1993, 12, 31)
        end_date = date(2017, 12, 30)
        check = {YEARS: 23, MONTHS: 11, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_12_2017(self):
        start_date = date(1993, 12, 31)
        end_date = date(2017, 12, 31)
        check = {YEARS: 24, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_1_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 1, 1)
        check = {YEARS: 24, MONTHS: 0, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_1_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 1, 30)
        check = {YEARS: 24, MONTHS: 0, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_1_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 1, 31)
        check = {YEARS: 24, MONTHS: 1, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_2_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 2, 1)
        check = {YEARS: 24, MONTHS: 1, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_27_2_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 2, 27)
        check = {YEARS: 24, MONTHS: 1, DAYS: 27}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_28_2_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 2, 28)
        check = {YEARS: 24, MONTHS: 2, DAYS: 28}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_3_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 3, 1)
        check = {YEARS: 24, MONTHS: 2, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_3_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 3, 30)
        check = {YEARS: 24, MONTHS: 2, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_3_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 3, 31)
        check = {YEARS: 24, MONTHS: 3, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_4_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 4, 1)
        check = {YEARS: 24, MONTHS: 3, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_4_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 4, 30)
        check = {YEARS: 24, MONTHS: 4, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_5_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 5, 1)
        check = {YEARS: 24, MONTHS: 4, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_5_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 5, 30)
        check = {YEARS: 24, MONTHS: 4, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_5_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 5, 31)
        check = {YEARS: 24, MONTHS: 5, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_6_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 6, 1)
        check = {YEARS: 24, MONTHS: 5, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_6_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 6, 30)
        check = {YEARS: 24, MONTHS: 6, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_7_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 7, 1)
        check = {YEARS: 24, MONTHS: 6, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_30_7_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 7, 30)
        check = {YEARS: 24, MONTHS: 6, DAYS: 30}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_31_7_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 7, 31)
        check = {YEARS: 24, MONTHS: 7, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_31_12_1993_to_1_8_2018(self):
        start_date = date(1993, 12, 31)
        end_date = date(2018, 8, 1)
        check = {YEARS: 24, MONTHS: 7, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_26_2_1993_to_29_2_2016(self):
        start_date = date(1993, 2, 26)
        end_date = date(2016, 2, 29)
        check = {YEARS: 23, MONTHS: 0, DAYS: 3}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_26_2_1993_to_25_2_2016(self):
        start_date = date(1993, 2, 26)
        end_date = date(2016, 2, 25)
        check = {YEARS: 22, MONTHS: 11, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_29_2_1996_to_28_2_2016(self):
        start_date = date(1996, 2, 29)
        end_date = date(2016, 2, 28)
        check = {YEARS: 19, MONTHS: 12, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_29_2_1996_to_29_2_2016(self):
        start_date = date(1996, 2, 29)
        end_date = date(2016, 2, 29)
        check = {YEARS: 20, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_29_2_1996_to_1_3_2016(self):
        start_date = date(1996, 2, 29)
        end_date = date(2016, 3, 1)
        check = {YEARS: 20, MONTHS: 0, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_26_2_1993_to_28_2_2017(self):
        start_date = date(1993, 2, 26)
        end_date = date(2017, 2, 28)
        check = {YEARS: 24, MONTHS: 0, DAYS: 2}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_26_2_1993_to_25_2_2017(self):
        start_date = date(1993, 2, 26)
        end_date = date(2017, 2, 25)
        check = {YEARS: 23, MONTHS: 11, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_29_2_1996_to_28_2_2017(self):
        start_date = date(1996, 2, 29)
        end_date = date(2017, 2, 28)
        check = {YEARS: 21, MONTHS: 0, DAYS: 0}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

    def test_clc_uptoday_from_29_2_1996_to_1_3_2017(self):
        start_date = date(1996, 2, 29)
        end_date = date(2017, 3, 1)
        check = {YEARS: 21, MONTHS: 0, DAYS: 1}
        m = 'month check - birthday: {b}, date: {d}'
        res = calc_age_uptoday(start_date, end_date)
        self.assertDictEqual(res, check, msg=m.format(b=start_date, d=end_date))

