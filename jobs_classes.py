class Vacancy:
    __slots__ = ...

    def __init__(self, data):
        self.name = data['name']
        self.url = data['url']
        self.description = data['description']
        self.salary = data['salary']

    def __str__(self):
        pass



class CountMixin:

    @property
    def get_count_of_vacancy(self):
        """
        Вернуть количество вакансий от текущего сервиса.
        Получать количество необходимо динамически из файла.
        """
        pass



class HHVacancy(Vacancy):  # add counter mixin
    """ HeadHunter Vacancy """

    def __str__(self):
        return f'HH: {self.name}, зарплата: {self.salary} руб/мес'



class SJVacancy(Vacancy):  # add counter mixin
    """ SuperJob Vacancy """

    def __str__(self):
        return f'SJ: {self.name}, зарплата: {self.salary} руб/мес'


