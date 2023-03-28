
from abc import ABC, abstractmethod
import requests
import os



class Engine(ABC):
    @abstractmethod
    def get_request(self):
        pass

    @staticmethod
    def get_connector(file_name):
        """ Возвращает экземпляр класса Connector """
        pass


class HH(Engine):


    def __init__(self, name_vacancy):
        self.url = "https://api.hh.ru/vacancies"
        self.name_vacancy = name_vacancy


    def get_request(self, name_vacancy, count_vacancy):
        # page = 0
        # posts_per_page = 20
        # vacancies_hh = []
        # while posts_per_page * page < count_vacancy:
        #
        #


class SuperJob(Engine):
    api_key: str = os.getenv('SUPERJOB_API_KEY')
    headers = {"X-Api-App-Id": api_key}
    posts_per_page = 20

    def __init__(self, name_vacancy):
        self.url = "https://api.superjob.ru/2.0/vacancies"
        self.name_vacancy = name_vacancy
    def get_request(self):
        posts_per_page = 20
