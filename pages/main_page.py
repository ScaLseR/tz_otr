"""Main Page Module"""
from .base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """class for work with main page"""

    links = []

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def header_is_exist(self):
        """find header"""
        return self.is_element_present(*MainPageLocators.HEADER)

    def footer_is_exist(self):
        """find footer"""
        return self.is_element_present(*MainPageLocators.FOOTER)

    def all_links_code_200(self):
        """check all links for status code 200"""
        self.get_all_links()
        for link in MainPage.links:
            self.check_link_code(link)

    def get_all_links(self):
        """gets all links from the page"""
        self.scroll_page()
        temp_links = []
        elements = self.find_elements(*MainPageLocators.LINK)
        for elem in elements:
            temp_links.append(elem.get_attribute("href"))
        temp_set = set(temp_links)
        print('Ссылок всего: ', len(temp_links))
        MainPage.links = list(temp_set)
        print('Уникальных ссылок: ', len(MainPage.links))

    def all_links_url_check(self):
        """check link and url in browser"""
        for link in MainPage.links:
            self.check_open_page(link)
