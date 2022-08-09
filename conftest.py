"""fixtures for choosing which browser to work with"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    """default browser -> GoogleChrome"""
    s = Service('C:/chromedriver/chromedriver.exe')
    browser = webdriver.Chrome(service=s)

    yield browser
    browser.quit()
