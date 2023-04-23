import json


class Vacancy:
    name_class = 'Vacancy'
    __slots__ = ('name', 'url', 'description', 'salary')

    def __init__(self, name, url, description, salary):
        self.name = name
        self.url = url
        self.description = description
        self.salary = salary

    def __str__(self):
        not_salary = 'не указана'
        return f'{self.name}, зарплата: {self.salary if self.salary else not_salary} руб/мес'

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __iter__(self):
        self.value = 0
        return self.value

    def __next__(self):
        if self.value < len(self.vacancies):
            self.value += 1
        else:
            raise StopIteration


class CountMixin:
    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        with open(self.file, 'r') as f:
            my_file = json.load(f)
            for i in my_file:
                for item in i:
                    self.count += 1
        return self.count


class HHVacancy(Vacancy, CountMixin):  # add counter mixin
    """ HeadHunter Vacancy """
    vacancies = []
    file = 'hh.json'

    def __init__(self, name, url, description, salary):
        super().__init__(name, url, description, salary)
        self.name = name
        self.count = CountMixin.get_count_of_vacancy

    @classmethod
    def instantiate_from_json(cls, file):
        with open(f'{file}') as f:
            file_opened = json.load(f)
            for i in file_opened:
                for item in i:
                    n = item.get('name')
                    u = item.get('url')
                    d = item.get('snippet').get('responsibility')
                    try:
                        s = item.get('salary').get('from')
                        if s == None: s = 0
                    except AttributeError:
                        s = 0
                    cls.vacancies.append(HHVacancy(n, u, d, s))


class SJVacancy(Vacancy, CountMixin):
    """ SuperJob Vacancy """
    vacancies = []
    file = 'sj.json'

    def __init__(self, name, url, description, salary):
        super().__init__(name, url, description, salary)
        self.url = url
        self.count = CountMixin.get_count_of_vacancy

    @classmethod
    def instantiate_from_json(cls, file):
        with open(f'{file}') as f:
            file_opened = json.load(f)
            for i in file_opened:
                for item in i:
                    p = item.get('profession')
                    l = item.get('link')
                    d = item.get('candidat')
                    try:
                        s = item.get('payment_from')
                        if s == None: c = 0
                    except AttributeError:
                        s = 0
                    cls.vacancies.append(SJVacancy(p, l, d, s))


def sorting(vacancies):
    """ Должен сортировать любой список вакансий по ежемесячной оплате (gt, lt magic methods) """
    vacancies = sorted(vacancies, reverse=True)
    return vacancies


def get_top(vacancies, top_count):
    """ Должен возвращать {top_count} записей из вакансий по зарплате (iter, next magic methods) """
    try:
        for i in range(top_count):
            print(vacancies[i])
    except IndexError:
        print(f'{top_count} все вакансии')

