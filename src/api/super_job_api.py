import os
import requests

from src.api.base_api import BaseAPI


class SuperJobAPI(BaseAPI):
    """Класс запроса вакансий на SuperJob API"""
    url: str = "https://api.superjob.ru/2.0"

    def __init__(self, url: str = url):
        """
        Инициализация класса SuperJobAPI.

        :param url: URL для запросов к SuperJob API.
        """
        super().__init__(url)

    def search_vacancies(self, job_title: str) -> list:
        """
        Поиск вакансий на SuperJob API.

        :param job_title: Заголовок вакансии для поиска.
        :return: Список найденных вакансий.
        """
        url = f"{self._base_url}/vacancies/"
        headers = {
            "X-Api-App-Id": os.getenv("API_SUPERJOB_KEY")
        }
        params = {
            "keywords": [[1, job_title]],
            "count": self._number_of_vacancies,
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        return data.get("objects", [])
