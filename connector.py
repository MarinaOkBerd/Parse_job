import json
import logging
import os


class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, df):
        self.__data_file = df
        self.__connect()

    def __connect(self):
        """
        Проверка на существование файла с данными и
        создание его при необходимости
        Также проверить на деградацию и возбудить исключение
        если файл потерял актуальность в структуре данных
        """
        try:
            if self.__data_file not in os.listdir('.'):
                with open(self.__data_file, 'w') as file:
                    file.write(json.dumps([]))
        except Exception as ex:
            logging.critical(ex)

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(self.__data_file, 'r') as f:
            r_data = json.load(f)
            r_data.append(data)
        with open(self.__data_file, 'w') as w:
            json.dump(r_data, w)

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение, например:
        {'price': 1000}, должно отфильтровать данные по полю price
        и вернуть все строки, в которых цена 1000
        """
        data_from_file = []
        with open(self.__data_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not query:
            return data

        for item in data:
            for key, value in query.items():
                if item[key] == value:
                    data_from_file.append(item)
        return data_from_file

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select
        """
        try:
            with open('df.json', 'r') as f:
                data = json.load(f)

            with open('df.json', 'w') as f:
                result = None
                for key in query.keys():
                    result = [*filter(lambda el: el[key] != query[key], result if result else data)]
                json.dump(result, f)

        except Exception as ex:
            logging.critical(ex)








