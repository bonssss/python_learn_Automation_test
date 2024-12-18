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
    Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\netryde\CHROMEDRIVER.EXE")
    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_customer_profile(driver):
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

    time.sleep(15)  # Wait for the page to load and show the result

    print("Login successful!")

    driver.find_element(By.XPATH,"(//div[contains(@class,'burger-icon-white')])[2]").click()
    time.sleep(2)
    profile = driver.find_element(By.XPATH,"(//a[normalize-space()='Profile'])[1]")
    profile.click()
    time.sleep(15)

    first_name = driver.find_element(By.XPATH,"(//input[@placeholder='First Name'])[1]")
    first_name.clear()
    first_name.send_keys("fname")
    last_name = driver.find_element(By.XPATH,"(//input[@placeholder='Last Name'])[1]")
    last_name.clear()
    last_name.send_keys("lname")

    phone_number = driver.find_element(By.XPATH,"(//input[@placeholder='Enter phone number'])[1]")
    phone_number.clear()
    phone_number.send_keys("3466234567")

    address = driver.find_element(By.XPATH,"(//input[@placeholder='Enter your address'])[1]")
    address.clear()
    address.send_keys("seattle")
    time.sleep(2)

    save_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Save Profile'])[1]")
    save_button.click()

    alert_success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "alert-success"))
    )

    # Assert the success alert's text
    assert alert_success.text == "Profile updated successfully", \
        f"Expected 'Profile updated successfully', but got '{alert_success.text}'"

    print("profile saved successfully")



