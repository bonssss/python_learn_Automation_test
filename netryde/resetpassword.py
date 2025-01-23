import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    Service_obj = Service(r"C:\Users\servi\Documents\Netryde_selenium\python_learn_Automation_test\netryde\CHROMEDRIVER.EXE")
    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_and_reset(driver):
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)

    driver.find_element(By.XPATH, "//header[@class='header sticky-bar ']//div[3]").click()
    signin_button = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-black')][normalize-space()='Sign In'])[1]")
    signin_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//a[normalize-space()='Forgot password?'])[1]"))
    )
    forget_password_button = driver.find_element(By.XPATH, "(//a[normalize-space()='Forgot password?'])[1]")
    forget_password_button.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@placeholder='Enter your email'])[1]"))
    )
    enter_email = driver.find_element(By.XPATH, "(//input[@placeholder='Enter your email'])[1]")
    enter_email.send_keys("11@test.zprodev.com")

    print("Please complete the CAPTCHA manually and press Enter to continue...")
    input("Press Enter after completing CAPTCHA...")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Send Reset Link'])[1]"))
    )
    send_resetlink_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Send Reset Link'])[1]")
    send_resetlink_button.click()

    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.XPATH, "//h4[contains(.,'reset link')]"))
    )
    success_message = driver.find_element(By.XPATH, "//h4[contains(.,'reset link')]")
    assert success_message.is_displayed(), "Success message is not displayed"
    assert "reset link" in success_message.text, f"Unexpected message: {success_message.text}"
    time.sleep(4)

    print("Test Passed: Success message displayed.")
