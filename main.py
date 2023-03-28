def run():
    while True:
        name_vacancy = input("Введите название вакансии.")
        count_vacancy = input("Сколько вакансий показывать ")
        experience = input("Выберите опыт работы: с опытом - 1, без опыта - 2")
        name_website = input("Выберите сайт для поиска: для HeadHunter - 1, для SuperJob - 2")
        if name_website == 1:
            vac_hh = HHVacancy()


        elif name_website == 2:
            vac_sj = SJVacancy()

        else:
            print("Ввод не верен")


if __name__ == "__main__":
    run()
