"""test cases module"""
from pages.main_page import MainPage


_URL = 'https://www.mos.ru/'


def test_search_in_ya(browser):
    """test case mos"""
    page = MainPage(browser, _URL)
    page.open()
    assert page.header_is_exist(), 'Отсутствует header'
    assert page.footer_is_exist(), 'Отсутствует footer'

