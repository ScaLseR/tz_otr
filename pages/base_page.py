"""Base Page Module"""
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from time import sleep
import requests
import logging


logger = logging.getLogger(__name__)
formatter = logging.Formatter("{asctime}:{levelname}:{name}:{message}", style="{")
file_handler = logging.FileHandler("test.log")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)


class BasePage:
    """base class for all pages"""
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, link):
        """opens the page"""
        self.browser.get(link)

    def is_element_present(self, how, what):
        """finds an element on the page"""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def find_elements(self, how, what):
        """finds the link of the first element in the search results"""
        elements = self.browser.find_elements(how, what)
        return elements

    def check_link_code(self, link):
        """check link for code 200"""
        try:
            _ = requests.request(method='get', url=link)
        except requests.exceptions.ConnectionError:
            text = 'ConnectionError -> ' + link
            self.write_in_log('err', text)
        except requests.exceptions.Timeout:
            text = 'TimeoutError -> ' + link
            self.write_in_log('err', text)

    def check_open_page(self, link):
        """checking opened page url """
        try:
            self.open(link)
            br_url = self.get_page_url()
            if link != br_url:
                text = link + ' открывается другая страница -> ' + br_url
                self.write_in_log('wrn', text)
                print(link, 'открывается другая страница -> ', br_url)
        except WebDriverException:
            text = 'WebDriverException -> ' + link
            self.write_in_log('err', text)

    def get_page_url(self):
        """get current url"""
        return self.browser.current_url

    def scroll_page(self):
        """scroll page by steps"""
        for i in range(6):
            self.browser.execute_script("scrollBy(0,+1000);")
            sleep(0.5)

    @staticmethod
    def write_in_log(lvl, text):
        """write text to log"""
        if lvl == 'wrn':
            logger.warning(text)
        if lvl == 'err':
            logger.error(text)
