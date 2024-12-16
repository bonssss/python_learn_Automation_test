import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\Automation learn\CHROMEDRIVER.EXE")
    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_password_display(driver):
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)

    # Perform login actions
    driver.find_element(By.XPATH, "(//div[contains(@class,'burger-icon-white')])[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//button[@class='btn btn-black'][normalize-space()='Sign In'])[1]").click()
    driver.find_element(By.XPATH, "(//input[contains(@class,'form-control username')])[1]").send_keys(
        "11@test.zprodev.com")
    password_field = driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[1]")
    password_field.send_keys("Test@123")
    show_password = driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[1]")
    show_password.click()

    # Check if the password input field contains the correct value
    password_value = password_field.get_attribute("value")  # Get the input value
    assert password_value == "Test@123", "Password is not displayed correctly!"

    print("Test Passed: Password is displayed correctly when 'Show Password' is toggled.")

    # Optionally, sleep to allow for manual verification or check on a certain element
    time.sleep(5)

