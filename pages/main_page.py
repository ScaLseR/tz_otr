"""Main Page Module"""
from .base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """class for work with main page"""
    _links = []

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
        count = 0
        for link in self._links:
            if self.check_link_code(link):
                count += 1
        print('count== ', count)
        if count == len(self._links):
            return True
        return False

    def get_all_links(self):
        """gets all links from the page"""
        elements = self.find_elements(*MainPageLocators.LINK)
        for elem in elements:
            self._links.append(elem.get_attribute("href"))
        temp_set = set(self._links)
        self._links = list(temp_set)
