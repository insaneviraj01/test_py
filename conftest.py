import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.ie.service import Service as IeService
from selenium.webdriver.safari.webdriver import Service as SafariService
from urllib3.util import request


@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Viraj", "Swami", "32", "Delhi","insaneviraj01@gmail.com"]

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")

@pytest.fixture(scope="function")
def browserinstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService())
    elif browser_name == "ie":
        driver = webdriver.Ie(service=IeService())
    elif browser_name == "safari":
         driver = webdriver.Safari(service=SafariService())
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield driver
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.quit()




