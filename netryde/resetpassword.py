import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\Automation learn\CHROMEDRIVER.EXE")
    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login_and_reset(driver):
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)


    driver.find_element(By.XPATH,"//header[@class='header sticky-bar ']//div[3]").click()
    signin_button = driver.find_element(By.XPATH,"(//button[contains(@class,'btn btn-black')][normalize-space()='Sign In'])[1]")
    signin_button.click()
    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"(//a[normalize-space()='Forgot password?'])[1]"))
    )
    forget_password_button = driver.find_element(By.XPATH,"(//a[normalize-space()='Forgot password?'])[1]")
    forget_password_button.click()

    WebDriverWait(driver,10).until(
        EC.visibility_of_element_located((By.XPATH,"(//input[@placeholder='Enter your email'])[1]"))
    )
    enter_email = driver.find_element(By.XPATH,"(//input[@placeholder='Enter your email'])[1]")
    enter_email.send_keys("11@test.zprodev.com")

    # Wait for CAPTCHA completion
    print("Please complete the CAPTCHA manually and press Enter to continue...")
    input("Press Enter after completing CAPTCHA...")

    send_resetlink_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Send Reset Link'])[1]")
    send_resetlink_button.click()

    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//h4[normalize-space()='A password reset link has been sent to your email address. Please check your inbox and follow the instructions to reset your password.']")
        )
    )
    success_message = driver.find_element(
        By.XPATH,
        "//h4[normalize-space()='A password reset link has been sent to your email address. Please check your inbox and follow the instructions to reset your password.']"
    )
    assert success_message.is_displayed(), "Success message is not displayed"
    assert "A password reset link has been sent to your email address." in success_message.text, \
        f"Unexpected message: {success_message.text}"

    print("Test Passed: Success message displayed.")

    time.sleep(10)