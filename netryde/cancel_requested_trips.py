import sys
import time
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
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
    Trips = driver.find_element(By.XPATH, "(//a[normalize-space()='Trips'])[2]")
    Trips.click()

    # Wait for trips section to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//h6[contains(text(),'Trips')])[2]"))
    )

    # Verify if the trips section is visible
    trips_element = driver.find_element(By.XPATH, "(//h6[contains(text(),'Trips')])[2]")
    assert trips_element.is_displayed(), "Trips element not found or visible!"

    print("Successfully displayed trip list")

    time.sleep(5)
    requested_checkbok = driver.find_element(By.XPATH,"(//span[@class='text-sm-medium'][normalize-space()='Requested'])[1]")
    requested_checkbok.click()
    time.sleep(3)
    #
    # pending_detail = driver.find_element(By.XPATH,"(//div[@class='item-flight background-card border-1 d-flex'])[1]")
    # pending_detail.click()

    try:
        # Check if there are any pending trips
        requested_detail = driver.find_element(By.XPATH,
                                             "(//div[@class='item-flight background-card border-1 d-flex'])[1]")

        # Click on the first pending trip if it exists
        requested_detail.click()
        print("Requested trip found and clicked.")
    except NoSuchElementException:
        print("No Requested trips available.")
        pytest.fail("No Requested trips available. Exiting test.")
        # driver.quit()  # Close the browser
        # sys.exit("Exiting test due to absence of pending trips.")


    driver.execute_script("window.scrollBy(0, 220);")

    cancel_button = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"(//div[@class='btn border border-dark-subtle w-100 rounded-2 btn-danger'])[1]"))
    )
    cancel_button.click()

    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 260);")

    time.sleep(3)
    driver.execute_script("window.scrollBy(0, 260);")


    reseaon = driver.find_element(By.XPATH,"(//select[@class='form-select'])[1]")
    reseaon.click()

    reseaon.send_keys(Keys.ARROW_DOWN)

    reseaon.send_keys(Keys.ENTER)

    driver.execute_script("window.scrollBy(0, 260);")

    confirm_cancel_button = driver.find_element(By.XPATH,"(//div[@class='btn btn-danger w-100 rounded-2'])[1]")
    confirm_cancel_button.click()
    time.sleep(5)
    # Optionally, sleep to allow manual verification
    expected_url = "https://nextdev.netryde.com/customer/trips"
    current_url = driver.current_url

    assert current_url == expected_url, f"URL assertion failed! Expected: {expected_url}, but got: {current_url}"

    print("Trip cancelled Successfully")
    time.sleep(15)
