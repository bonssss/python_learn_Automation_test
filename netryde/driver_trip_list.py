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


def test_login_and_trip_list(driver):
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)

    # Perform login actions
    driver.find_element(By.XPATH, "(//div[contains(@class,'burger-icon-white')])[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//button[@class='btn btn-black'][normalize-space()='Sign In'])[1]").click()
    driver.find_element(By.XPATH, "(//input[contains(@class,'form-control username')])[1]").send_keys(
        "10@test.zprodev.com")
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

    time.sleep(10)  # Wait for the page to load and show the result

    print("Login successful!")

    # Optionally, you can add assertions or additional steps to verify the login

    # Now, let's proceed to the trip status filters test
    filter_checkboxes = {
        "All": "(//span[@class='checkmark'])[8]",
        "Pending": "(//span[@class='checkmark'])[9]",
        "Requested": "(//span[@class='checkmark'])[10]",
        "Booked": "(//span[@class='checkmark'])[11]",
        "Started": "(//span[@class='checkmark'])[12]",
        "Completed": "(//span[@class='checkmark'])[13]",
        "Canceled": "(//span[@class='checkmark'])[14]"
    }

    # Navigate to the trip list page
    driver.get("https://nextdev.netryde.com/driver/trips")  # Update with the correct URL

    # Iterate over each filter checkbox
    for filter_option, xpath in filter_checkboxes.items():
        filter_checkbox = driver.find_element(By.XPATH, xpath)

        # Ensure the checkbox is not selected before clicking
        if not filter_checkbox.is_selected():
            filter_checkbox.click()

        # Wait for the page to refresh and reflect the filter
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "(//h6[normalize-space()='Status'])[1]"))
            # Ensure trip status list is visible
        )

        # Verify the displayed trips match the selected filter
        trip_statuses = driver.find_elements(By.XPATH, "(//h6[normalize-space()='Status'])[1]")  # Adjust the XPath accordingly

        for trip_status in trip_statuses:
            assert filter_option.lower() in trip_status.text.lower(), f"Expected status '{filter_option}' but found {trip_status.text}"

        # Deselect the filter to test the next one
        if filter_checkbox.is_selected():
            filter_checkbox.click()

        # Allow time for page refresh before testing the next filter
        time.sleep(1)

    print("All filters passed successfully!")
