from abc import ABC, abstractmethod
import requests
import os

from requests import Response

from connector import *


class Engine(ABC):

    @abstractmethod
    def get_request(self):
        raise NotImplementedError

    @staticmethod
    def get_connector(file_name: str) -> Connector:
        return Connector(file_name)


class HH(Engine):

    def __init__(self, name_vacancy: str, page: int = 0):
        self.url: str = 'https://api.hh.ru/vacancies'
        self.params = {'text': name_vacancy, 'page': 0, 'per_page': 100}

    def get_request(self):
        response = requests.get(self.url, params=self.params)
        return response.json()

    def get_vacancy_info(self, data):
        vacancy_info = {'name': data['name'], 'url': data['alternate_url'],
                       'description': data.get('snippet').get('responsibility'), 'salary': data.get('salary')
        }
        return vacancy_info

    def get_vacancies(self):
        vacancies = []
        page = 0
        if len(vacancies) >= 500:
            self.params['page'] = page
            data = self.get_request()
            for vacancy in data.get('items'):
                if vacancy.get('salary') is not None and vacancy.get('salary').get('currency') is not None:
                    if vacancy.get('salary').get('currency') == 'RUR':
                        vacancy.append(self.get_vacancy_info(vacancy))
                    else:
                        continue
                else:
                    vacancy.append(self.get_vacancy_info(vacancy))





class SuperJob(Engine):
    api_key: str = os.getenv('SUPERJOB_API_KEY')
    headers = {"X-Api-App-Id": api_key}


    def __init__(self, name_vacancy: str):
        self.url: str = "https://api.superjob.ru/2.0/vacancies/"
        self.params = {'text': name_vacancy, 'count': 100, 'page': 1}



    def get_request(self):
        response = requests.get(url=self.url, params=self.params, headers=self.headers)
        return response.json()

    def get_vacancy_info(self, data):
        salary = {'from': data['payment_from'], 'to': data['payment_to'], 'currency': data['currency']}
        vacancy_info={
            'name': data['profession'], 'url': data['link'],
            'description': data.get('objects').get('candidat'), 'salary': salary
        }
        return vacancy_info
