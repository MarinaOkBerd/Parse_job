import json
from typing import Optional

class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    def __init__(self, file_path: str):
        self.data_file = file_path

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value: str):
        self.__data_file = value
        self.__connect()

    def __connect(self):
        try:
            data = self._read_json()
            assert isinstance(data, list)
            for item in data:
                assert isinstance(item, dict)
        except Exception:
            self._save_json([])

    def _save_json(self, data: list) -> None:
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def _read_json(self) -> list:
        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def insert(self, data: dict) -> None:
        file_data: list = self._read_json()
        file_data.append(data)
        self._save_json(file_data)

    def select(self, query: Optional[dict] = None) -> list:
        file_data: list = self._read_json()
        if not query:
            return file_data

        result = []
        for entry in file_data:
            if all(entry.get(key) == value for key, value in query.items()):
                result.append(entry)

        return result








