import json


class Vacancy:
    __slots__ = ('name', 'url', 'description', 'salary')

    def __init__(self, data):
        self.name = data['name']
        self.url = data['url']
        self.description = data['description']
        self.salary = data.get('salary')

    def __str__(self):
        pass


class CountMixin:

    @staticmethod
    def get_count_of_vacancy(file):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        with open(file, encoding='utf-8') as f:
            data = json.load(f)
            return len(data)



class HHVacancy(Vacancy, CountMixin):
    """ HeadHunter Vacancy """
    def __init__(self, data, name, url, description, salary):
        super().__init__(name, url, description, salary)
        self.name = data['items']['name']
        self.url = data['items']['apply_alternate_url']
        self.description = data['items']['snippet']['responsibility']
        self.salary = data['items']['salary']['from']

    # def sorting(vacancies_hh):
    #     sort_hh = []
    #     for i in range(len(vacancies_hh)):
    #         if vacancies_hh[i]['salary'] is not None:
    #             sort_hh.append(vacancies_hh[i])
    #     sort_hh = sorted(key=lambda x: x['salary']['from'], reverse=True)
    #     return sort_hh
    #
    # def get_top(vacancies_hh, top_count):
    #     sort_hh = sorted(key=lambda x: x['salary']['from'], reverse=True)
    #     vac_hh_top = []
    #     for i in range(top_count):
    #         vac_hh_top.append(sort_hh[i])
    #     return sort_hh

    def __str__(self):
        return f'HH: {self.name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy, CountMixin):
    """ SuperJob Vacancy """
    def __init__(self, data, name, url, description, salary):
        super().__init__(name, url, description, salary)
        self.name = data['objects']['profession']
        self.url = data['objects']['link']
        self.description = data['objects']['candidat']
        self.salary = data['objects']['payment_from']

    def sorting(vacancies_sj):
        sort_sj = []
        for i in range(len(vacancies_sj)):
            if vacancies_sj[i]['payment_from'] is not None:
                sort_sj.append(vacancies_sj[i])
        sort_sj = sorted(key=lambda x: x['payment_from'], reverse=True)
        return sort_sj

    def get_top(vacancies_hh, top_count):
        sort_sj = sorted(key=lambda x: x['salary']['from'], reverse=True)
        vac_sj_top = []
        for i in range(top_count):
            vac_sj_top.append(sort_sj[i])
        return sort_sj

    def __str__(self):
        return f'SJ: {self.name}, зарплата: {self.salary} руб/мес'


