from unittest import TestCase

from cats.vk_api.descr_analyzer import get_age_info


class TestGgetAgeInfo(TestCase):
    tests = [
        {"etalon": {"months": 5}, "text": "5-6 мес"},
        {"etalon": {"years": 2}, "text": "2-3 год"},
        {"etalon": {"years": 1}, "text": "1-2 год"},
        {"etalon": {"years": 1}, "text": "1-1.5 год"},
        {"etalon": {"months": 7}, "text": "6-8 мес"},
        {"etalon": {"months": 7}, "text": "7-8 мес"},
        {"etalon": {"months": 4}, "text": "4-5 мес"},
        {"etalon": {"months": 4}, "text": "3-5 мес"},
        {"etalon": {"years": 1}, "text": "возраст - до года"},
        {"etalon": {"months": 3}, "text": "3-4 мес"},
        {"etalon": {"months": 2}, "text": "2-3 мес"},
        {"etalon": {"months": 6}, "text": "6-7 мес"},
        {"etalon": {"years": 1}, "text": "возраст - около года"},

        {"etalon": {"days": 28}, "text": "4-5 нед"},

        {"etalon": {"years": 2}, "text": "2-3 лет"},
        {"etalon": {"months": 10}, "text": "9-12 мес"},
        {"etalon": {"months": 6}, "text": "5-7 мес"},
        {"etalon": {"years": 3}, "text": "3-4 год"},
        {"etalon": {"months": 9}, "text": "8-10 мес"},
        {"etalon": {"months": 9}, "text": "8 - 10 мес"},
        {"etalon": {"months": 8}, "text": "8-9 мес"},
        {"etalon": {"years": 2}, "text": "2-х лет"},
        {"etalon": {"months": 1}, "text": "1,5-2 мес"},
        {"etalon": {"years": 1}, "text": "1-1,5 год"},
        {"etalon": {"years": 1}, "text": "1,5-2 год"},
        {"etalon": {"years": 1}, "text": "1,5 год"},
        {"etalon": {"years": 1}, "text": "1,5 лет"},
        {"etalon": {"months": 2}, "text": "2,5 мес"},
        {"etalon": {"months": 4}, "text": "4х мес"},
        {"etalon": {"years": 2}, "text": "2 год"},
        {"etalon": {"months": 2}, "text": "2 мес"},
        {"etalon": {"years": 1}, "text": "1 год"},
        {"etalon": {"years": 2}, "text": "2х лет"},
        {"etalon": {"months": 3}, "text": "3 мес"},
        {"etalon": {"months": 5}, "text": "5 мес"},
        {"etalon": {"years": 2}, "text": "2 лет"},
        {"etalon": {"months": 4}, "text": "4 мес"},
        {"etalon": {"years": 1}, "text": "возраст около года"},
        {"etalon": {"months": 9}, "text": "9 мес до 1 год"},
        {"etalon": {"months": 6}, "text": "6 мес"},
        {"etalon": {"months": 9}, "text": "9мес"},
        {"etalon": {"days": 7}, "text": "1 нед"},
        {"etalon": {"years": 1}, "text": "catsekb ;\n✅ возраст ~ до года;\n✅ к людям - л"},
    ]

    def test_get_age_info(self):
        for test in self.tests:
            etalon = test["etalon"]
            res = get_age_info(test["text"])
            self.assertDictEqual(
                etalon,
                res,
                msg='etalon = {et}, res = {res}, text = {txt}'.format(
                    et=etalon,
                    res=res,
                    txt=test["text"]
                )
            )

