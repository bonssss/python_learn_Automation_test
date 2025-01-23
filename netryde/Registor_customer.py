import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    Service_obj = Service(r"C:\Users\servi\Documents\Netryde_selenium\python_learn_Automation_test\netryde\CHROMEDRIVER.EXE")

    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_register(driver):
    # Perform actions
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)
    humburger_icons = driver.find_element(By.XPATH, "(//div[contains(@class,'burger-icon-white')])[1]")
    humburger_icons.click()
    time.sleep(3)

    signup_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Sign Up'])[1]")
    signup_button.click()
    time.sleep(4)

    email = driver.find_element(By.XPATH, "(//input[contains(@class,'form-control email')])[1]")
    email.send_keys("11@test.zprodev.com")

    passwords = driver.find_element(By.XPATH, "(//input[contains(@placeholder,'***********')])[1]")
    passwords.send_keys("Test@123")

    confirm_password = driver.find_element(By.XPATH, "(//input[contains(@placeholder,'***********')])[2]")
    confirm_password.send_keys("Test@123")

    terms_conditions = driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[2]")
    terms_conditions.click()

    # Wait for manual CAPTCHA completion
    print("Please complete the CAPTCHA manually and press Enter to continue...")
    input("Press Enter after completing CAPTCHA...")

    # Click the Register button
    Register_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Create New Account'])[1]")
    Register_button.click()

    # Wait and assert the verification message
    try:
        verification_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "(//h4[normalize-space()='A verification link has been sent to your email'])[1]"))
        )
        assert verification_email.text == "A verification link has been sent to your email", \
            f"Unexpected message: {verification_email.text}"
        print("Verification email message displayed correctly.")
    except Exception as e:
        print(f"Error: {e}")

    time.sleep(10)
    print("Registered successfully")
    driver.quit()


