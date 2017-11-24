from unittest import TestCase


from cats.updater.descr_analyzer import get_age_info
from cats.updater.name_analyzer import replace_str_end_at_empty, get_info_from_title, STATUS_HOME, STATUS_SHELTER, \
    STATUS_DIE


class TestDescrAnalyzer(TestCase):
    age_info_tests = [
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
        for test in self.age_info_tests:
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


class TestNameAnalyzer(TestCase):

    def test_get_info_from_title(self):
        get_info_from_title_tests_home = [
            {
                "title": "ПРИСТРОЕН Шкода",
                "name": "Шкода"
            },
            {
                "title": "ПРИСТРОЕН Кроули",
                "name": "Кроули"
            },
            {
                "title": "Орхидея ПРИСТРОЕНА",
                "name": "Орхидея"
            },
            {
                "title": "ПРИСТРОЕНЫ Зефир, Крем, Сливка, Трюфелька",
                "name": "Зефир, Крем, Сливка, Трюфелька"
            },
            {
                "title": "Пристроен_Аль КОТоне",
                "name": "Аль КОТоне"
            },
            {
                "title": "ПРИСТРОЕНА_Мона",
                "name": "Мона"
            },
            {
                "title": "ПРИСТРОЕН_Бритый Кот",
                "name": "Бритый Кот"
            },
            {
                "title": "Грю_ПРИСТРОЕН",
                "name": "Грю"
            },
            {
                "title": "Тимми - ПРИСТРОЕН",
                "name": "Тимми"
            },
            {
                "title": "ПРИСТРОЕНЫ сфинксы Смайл и Ксавьер",
                "name": "сфинксы Смайл и Ксавьер"
            },
            {
                "title": "ПРИСТРОЕНА Клеопатра (бывшая Клюшка)",
                "name": "Клеопатра (бывшая Клюшка"
            },
            {
                "title": "Пристроен Джанго",
                "name": "Джанго"
            },
            {
                "title": "Масечка пристроен!",
                "name": "Масечка"
            },
            {
                "title": "Нарцисс пристроен!",
                "name": "Нарцисс"
            },
            {
                "title": "Пристроена! суслик",
                "name": "суслик"
            },
            {
                "title": "Тимми - ПРИСТРОЕН",
                "name": "Тимми"
            },
        ]

        get_info_from_title_tests_shelter = [
            {"title": "ИСПЫТАЛКА Оливка", "name": 'ИСПЫТАЛКА Оливка'},
            {"title": "Котюня", "name": 'Котюня'},
            {"title": "Дон Батон", "name": 'Дон Батон'},
            {"title": "Фрау Мяу", "name": 'Фрау Мяу'},
            {"title": "Котюня ", "name": 'Котюня'},
            {"title": "Котюня_ ", "name": 'Котюня'},
        ]

        get_info_from_title_tests_die = [
            {"title": "НА РАДУГЕ Эльза", "name": 'Эльза'},
            {"title": "НА РАДУГЕ Рокфор", "name": 'Рокфор'},
        ]

        for status, tests in (
                (STATUS_HOME, get_info_from_title_tests_home),
                (STATUS_SHELTER, get_info_from_title_tests_shelter),
                (STATUS_DIE, get_info_from_title_tests_die),
        ):
            for t in tests:
                et = (status, t["name"])
                res = get_info_from_title(t["title"])
                m = """
\tetalon[status]='{et_status}', etalon[name]='{et_name}'
\tres[status]='{res_status}', res[name]='{res_name}'
"""
                self.assertTupleEqual(et, res, msg=m.format(
                    et_status=status,
                    et_name=t['name'],
                    res_status=res[0],
                    res_name=res[1]
                ))

    def test_replace_str_end_at_empty(self):
        tests = [
            {"title": "  Фрау Мяу_", "name": "Фрау Мяу"},
            {"title": " Мяу   ", "name": "Мяу"},
            {"title": "-___Фрау Мяу   ", "name": "Фрау Мяу"},
            {"title": "- Фрау Мяу ", "name": "Фрау Мяу"},
            {"title": "____Фрау Мяу ", "name": "Фрау Мяу"},
            {"title": ",,,Зефир, Крем, Сливка, Трюфелька    ", "name": "Зефир, Крем, Сливка, Трюфелька"},
            {"title": "Сливка", "name": "Сливка"},
            {"title": "Лас кюня ", "name": "Лас кюня"},
            {"title": "_dsалв ана    ", "name": "dsалв ана"},
            {"title": "аывае нвыавапыа  ", "name": "аывае нвыавапыа"},
            {"title": "_____вапыв апыупыаывимывапнкфуыапывпsd+++++", "name": "вапыв апыупыаывимывапнкфуыапывпsd"},
            {"title": "__2312ывапыцук епуыап ывапфыу   ___---", "name": "2312ывапыцук епуыап ывапфыу"},
            {"title": "   фыв апцй укпак---", "name": "фыв апцй укпак"},
            {"title": "ф ыцфепцу", "name": "ф ыцфепцу"},
        ]
        for test in tests:
            res = replace_str_end_at_empty(test['title'])
            self.assertEqual(test['name'], res)
