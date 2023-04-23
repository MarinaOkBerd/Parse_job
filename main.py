from engine_classes import HH, SuperJob
from jobs_classes import HHVacancy, SJVacancy
from jobs_classes import get_top, sorting


if __name__ == '__main__':
    name_website = int(input("Выберите сайт для поиска: для HeadHunter - 1, для SuperJob - 2"))
    name_vacancy = input("Введите название вакансии:")
    count_vacancy = int(input('Сколько вакансий показывать'))
    sort = int(input("Отсортировать вакансии: да - 1: нет - 2"))
    while True:
        vacancies_count = 100
        if name_website == 1:
            hh_engine = HH()
            hh = hh_engine.get_request(name_vacancy, vacancies_count)
            hh_ = HH.get_connector('hh.json')
            hh_.insert(hh)
            HHVacancy.instantiate_from_json('hh.json')
            if sort == 2:

                get_top(HHVacancy.vacancies, count_vacancy)
                print(HHVacancy.get_count_of_vacancy)
            else:
                sort_list = sorting(HHVacancy.vacancies)
                get_top(sort_list, count_vacancy)
                print(HHVacancy.get_count_of_vacancy)

        if name_website == 2:
            sj_engine = SuperJob()
            sj = sj_engine.get_request(name_vacancy, vacancies_count)
            sj_ = SuperJob.get_connector('sj.json')
            sj_.insert(sj)
            SJVacancy.instantiate_from_json('sj.json')
            if sort == 2:
                get_top(SJVacancy.vacancies, count_vacancy)
                print(SJVacancy.get_count_of_vacancy)
            else:
                sort_list = sorting(SJVacancy.vacancies)
                get_top(sort_list, count_vacancy)
                print(SJVacancy.get_count_of_vacancy)

        break

