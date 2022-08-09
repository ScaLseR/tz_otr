"""test cases module"""
from pages.main_page import MainPage


_URL = 'https://www.mos.ru/'


def test_search_and_check_mos(browser):
    """test case mos"""
    page = MainPage(browser)
    page.open(_URL)
    assert page.header_is_exist(), 'Отсутствует header'
    assert page.footer_is_exist(), 'Отсутствует footer'
    page.all_links_code_200()
    page.all_links_url_check()
