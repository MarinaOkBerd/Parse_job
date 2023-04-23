import os
from abc import ABC, abstractmethod
from connector import Connector

import requests


class Engine(ABC):
    @abstractmethod
    def get_request(self):
        raise NotImplementedError

    @staticmethod
    def get_connector(file_name: str) -> Connector:
        return Connector(file_name)


class HH(Engine):
    url = 'https://api.hh.ru/'
    per_page = 20

    def get_vacancies(self, name_vacancy, page):
        responce = requests.get(f'{self.url}vacancies?text={name_vacancy} & page={page}')
        if responce.status_code == 200:
            return responce.json()
        return None

    def get_request(self, name_vacancy, count_vacancy):
        page = 0
        result = []
        while self.per_page * page <= count_vacancy:
            tmp_result = self.get_vacancies(name_vacancy, page)
            if tmp_result:
                result += tmp_result.get('items')
                page += 1
            else:
                break
        return result


class SuperJob(Engine):
    url = 'https://api.superjob.ru/2.0'
    api_key: str = os.getenv('SUPERJOB_API_KEY')
    per_page = 20

    def _send_request(self, name_vacancy, page):
        url = f'{self.url}/vacancies/?page={page}&keyword={name_vacancy}'
        headers = {
            'X-Api-App-Id': self.api_key,
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        responce = requests.get(url=url, headers=headers)
        if responce.status_code == 200:
            return responce.json()
        return None

    def get_request(self, name_vacancy, count_vacancy):
        page = 0
        result = []
        while self.per_page * page <= count_vacancy:
            tmp_result = self._send_request(name_vacancy, page)
            if tmp_result:
                result += tmp_result.get('objects')
                page += 1
            else:
                break
        return result