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
    Service_obj = Service(r"C:\Users\bons\Documents\Website_projects\python learn\netryde\CHROMEDRIVER.EXE")

    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login_and_trip_list(driver):
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)

    # Perform login actions
    driver.find_element(By.XPATH, "(//div[contains(@class,'burger-icon-white')])[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//button[@class='btn btn-black'][normalize-space()='Sign In'])[1]").click()
    driver.find_element(By.XPATH, "(//input[contains(@class,'form-control username')])[1]").send_keys(
        "cawela8559@nalwan.com")
    password_field = driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[1]")
    password_field.send_keys("Test@123")
    show_password = driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[1]")
    show_password.click()

    # Wait for CAPTCHA completion
    print("Please complete the CAPTCHA manually and press Enter to continue...")
    input("Press Enter after completing CAPTCHA...")

    # Submit login
    submit_login = driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]")
    submit_login.click()

    # Wait for page to load
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://nextdev.netryde.com/customer/book")
    )

    # Navigate to the Trips page
    humburger_icon = driver.find_element(By.XPATH, "(//span[@class='burger-icon-bottom'])[1]")
    humburger_icon.click()
    time.sleep(5)
    change_password = driver.find_element(By.XPATH, "(//a[normalize-space()='Change Password'])[1]")
    change_password.click()
    time.sleep(5)

    current_password = driver.find_element(By.XPATH,"(//input[@placeholder='Current Password'])[1]")
    current_password.send_keys("Test@123")
    time.sleep(2)

    new_password = driver.find_element(By.XPATH, "(//input[contains(@placeholder,'***********')])[1]")
    new_password.send_keys("Test@123")
    time.sleep(2)

    confirm_password = driver.find_element(By.XPATH, "(//input[contains(@placeholder,'***********')])[2]")
    confirm_password.send_keys("Test@123")

    time.sleep(2)

    # Wait for CAPTCHA completion
    print("Please complete the CAPTCHA manually and press Enter to continue...")
    input("Press Enter after completing CAPTCHA...")

    submit_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Submit'])[1]")

    submit_button.click()

    # success_message_element = WebDriverWait(driver, 10).until(
    #     EC.visibility_of_element_located((By.XPATH, "(//div[@class='popup-container'])[1]"))
    #     # Replace By.ID and "success-message" with the appropriate locator
    # )
    #
    # # Retrieve the text from the success message element
    # actual_message = success_message_element.text
    #
    # # Assert that the actual message matches the expected message
    # expected_message = "Password reset successfully!"
    # assert actual_message == expected_message, f"Expected message: '{expected_message}', but got: '{actual_message}'"



    # Wait for trips section to load


    # Optionally, sleep to allow manual verification
    time.sleep(15)
