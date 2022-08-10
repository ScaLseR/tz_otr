"""test cases module"""
import allure
from pages.main_page import MainPage


_URL = 'https://www.mos.ru/'


@allure.feature("test case mos")
@allure.story('Открываем _URL, проверяем видимость header и footer а так же все ссылки на код ответа 200')
def test_search_and_check_mos(browser):
    """test case mos"""
    page = MainPage(browser)
    page.open(_URL)
    with allure.step("Проверяем видимость header-а"):
        assert page.header_is_exist(), 'Отсутствует header'
    with allure.step("Проверяем видимость footer-а"):
        assert page.footer_is_exist(), 'Отсутствует footer'
    with allure.step('Проверяем все ссылки на status code = 200'):
        page.all_links_code_200()
    with allure.step('Открываем все ссылки и проверяем на соответствие URL в браузере'):
        page.all_links_url_check()
