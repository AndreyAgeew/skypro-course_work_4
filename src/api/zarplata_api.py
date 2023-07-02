from src.api.hh_api import HeadHunterAPI


class ZarplataAPI(HeadHunterAPI):
    """Класс запроса вакансий на Zarplata"""
    url: str = 'https://api.zarplata.ru/vacancies'

    def __init__(self, url: str = url):
        """
        Инициализация класса ZarplataAPI.

        :param url: URL для запросов к Zarplata API.
        """
        super().__init__(url)
