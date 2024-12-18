import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="class")
# to define custom browser options
# def pytest_addoption(parser):
#     parser.addoption("--custom-option", action="store", default="default_value", help="Description of the custom option.")

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )
def setup(request):
     # Set up Chrome WebDriver
    request.config.getoptions("browser_name")
    Service_obj = Service(
        r"C:\Users\bons\Documents\Website projects\python learn\netryde\chromedriver-win64\CHROMEDRIVER.EXE")
    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)
    driver.implicitly_wait(5)
    request.cls.driver = driver
    yield driver
    driver.quit()