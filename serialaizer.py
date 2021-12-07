import json

class SerialaizeWriter:
    """Класс для записи в файл"""

    def __init__(self, file_path) -> None:
        """Конструктор класса, на вход принимает путь к файлу"""

        self.path = file_path

    def write_file(self, array) -> None:
        """Функция записи в файл, принимает на вход сам массив для записи"""
        with open(self.path, 'w') as write_file:
            json.dump(array, write_file)

class SerialaizeReader:
    """Класс для чтения из файла"""

    def __init__(self, file_path) -> None:
        """Конструктор класса, на вход принимает путь к файлу"""

        self.path = file_path

    def read_file(self) -> list:
        """Функция чтения из файла, возвращает массив считаных значений"""

        with open(self.path, 'rb') as read_file:
            return json.load(read_file)