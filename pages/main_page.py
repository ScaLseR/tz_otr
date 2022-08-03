"""Main Page Module"""
from .base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """class for work with main page"""
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def header_is_exist(self):
        """find header"""
        return self.is_element_present(*MainPageLocators.HEADER)

    def footer_is_exist(self):
        """find footer"""
        return self.is_element_present(*MainPageLocators.FOOTER)
