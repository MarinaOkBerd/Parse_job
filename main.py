from engine_classes import HH
from jobs_classes import *
from connector import Connector


def run():
    global hh_engine
    while True:
        name_vacancy = input("Введите название вакансии.")
        count_vacancy = int(input("Сколько вакансий показывать "))
        name_website = input("Выберите сайт для поиска: для HeadHunter - 1, для SuperJob - 2")
        sort = input("Отсортировать вакансии: да - 1: нет - 2")
        top_count = int(input("Сколько вывести лучших вакансий "))
        if name_website == 1:
            hh_engine = HH(name_vacancy)
            hh_connector = hh_engine.get_connector('hh.json')
            vacancies_hh = hh_engine.get_request().json()['items']
            for vacancy in vacancies_hh:
                hh_connector.insert(vacancy)

        while True:
            if count_vacancy > 0:
                vacancies_hh = Connector.select()#??????????
        while True:






        #elif name_website == 2:
        #     vac_sj = SuperJob(name_vacancy)
        #     sj_json = vac_sj.get_request(name_vacancy, count_vacancy)
        #     sj_connector = vac_sj.get_connector('sj.json')
        #     sj_connector.insert(sj_json)
        #     vacancies_sj = SJVacancy(sj_json)
        #     vac_sj_len = vacancies_sj.get_count_of_vacancy('sj_json')
        #     print(f"Вакансии с сайта SuperJob: {vac_sj_len} позиций")
        #     result_sj = sj_connector.select()
        #     for i in result_sj:
        #         print(i)
        #     if sort == 1:
        #         vac_sj_sort = SJVacancy.sorting(result_sj)
        #         result_sj_sort = []
        #         for i in range(len(vac_sj_sort)):
        #             vac = HHVacancy(result_sj_sort[i])
        #             result_sj_sort.append(vac)
        #         for i in result_sj_sort:
        #             print(i)
        #     else:
        #         for i in result_sj:
        #             print(i)
        #     if top_count == 1:
        #         vac_sj_sort = HHVacancy.sorting(result_sj)
        #         vac_sj_top = HHVacancy.get_top(vac_sj_sort, top_count)
        #         for i in vac_sj_top:
        #             print(i)
        #     else:
        #         for i in result_sj:
        #             print(i)
        #     if end == 3:
        #         quit()


if __name__ == "__main__":
    run()
