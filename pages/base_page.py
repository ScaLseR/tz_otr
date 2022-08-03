"""Base Page Module"""
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from time import sleep
import requests
import logging

logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('test.log')
fh.setLevel(logging.WARNING)
logger.addHandler(fh)


class BasePage:
    """base class for all pages"""
    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)

    def open(self, link):
        """opens the page"""
        self.browser.get(link)

    def close(self):
        """close the page"""
        self.browser.close()

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

    @staticmethod
    def check_link_code(link):
        """check link for code 200"""
        try:
            _ = requests.request(method='get', url=link)
        except requests.exceptions.ConnectionError as cne:
            logging.error(cne, exc_info=True)
        except requests.exceptions.Timeout as toe:
            logging.error(toe, exc_info=True)

    def check_open_page(self, link):
        """checking opened pdge url """
        try:
            self.open(link)
            br_url = self.get_page_url()
            if link != br_url:
                logger.warning(link + 'открывается другая страница -> ' + br_url)
                print(link, 'открывается другая страница -> ', br_url)
        except WebDriverException as wde:
            logging.error(wde, exc_info=True)

    def go_to_new_window(self):
        """go to new window in browser"""
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def get_page_url(self):
        """get current url"""
        return self.browser.current_url

    def scroll_page(self):
        """scroll page by steps"""
        for i in range(6):
            self.browser.execute_script("scrollBy(0,+1000);")
            sleep(0.5)
