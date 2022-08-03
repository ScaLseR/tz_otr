"""fixtures for choosing which browser to work with"""
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    """choosing browser"""
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    """fixture for choosing a browser for tests, default browser -> GoogleChrome"""
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        ffp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=ffp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    browser.quit()
