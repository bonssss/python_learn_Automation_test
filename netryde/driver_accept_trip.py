import time
from time import sleep
import os
from dotenv import load_dotenv

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
load_dotenv()
username = os.getenv("NETRYDE_USERNAME")
password = os.getenv("NETRYDE_PASSWORD")


@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    Service_obj = Service(r"C:\Users\bons\Documents\Website_projects\python learn\netryde\CHROMEDRIVER.EXE")

    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_login_and_trip_accept(driver):
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)

    # Perform login actions
    driver.find_element(By.XPATH, "(//div[contains(@class,'burger-icon-white')])[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "(//button[@class='btn btn-black'][normalize-space()='Sign In'])[1]").click()
    driver.find_element(By.XPATH, "(//input[contains(@class,'form-control username')])[1]").send_keys(
        username)
    password_field = driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[1]")
    password_field.send_keys(password)
    show_password = driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[1]")
    show_password.click()

    # Wait for CAPTCHA completion
    print("Please complete the CAPTCHA manually and press Enter to continue...")
    input("Press Enter after completing CAPTCHA...")

    # Submit login
    submit_login = driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]")
    submit_login.click()

    time.sleep(10)

    # Wait for the page to load and show the result
    # humburger_icon = driver.find_element(By.XPATH,"(//div[contains(@class,'burger-icon-white')])[2]")
    # humburger_icon.click()
    # time.sleep(3)
    #
    # change_to_driver = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "(//div[@class='item-icon'])[1]"))
    # )
    #
    # # Scroll the element into view using JavaScript
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", change_to_driver)
    #
    # # Optionally, wait for a short duration to ensure the scrolling has completed
    # time.sleep(1)
    #
    # # Click the element
    # change_to_driver.click()

    # Trips = driver.find_element(By.XPATH,"(//a[normalize-space()='Trips'])[2]")
    # Trips.click()
    # time.sleep(5)
    # pending = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH,
    #                                 "//div[@class='box-collapse scrollFilter d-none d-lg-block']//span[@class='text-sm-medium'][normalize-space()='Pending']"))
    # )
    # pending.click()

    time.sleep(5)

    requested = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html[1]/body[1]/main[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/label[1]/span[2]"))
    )
    requested.click()
    time.sleep(5)

    try:
        requested_trip_box = driver.find_element(By.XPATH,
                                                 "(//div[@class='item-flight background-card border-1 d-flex'])[1]")
        requested_trip_box.click()
        time.sleep(5)
    except NoSuchElementException:
        print("No requested trips available.")
        # Break the test or handle accordingly
        driver.quit()
        exit()

    except TimeoutException:
        print("Requested element not found or not clickable.")
        driver.quit()
        exit()

    time.sleep(4)

    driver.execute_script("window.scrollBy(0, 120);")

    accept_btn = driver.find_element(By.XPATH,"(//div[@class='btn btn-book w-100 rounded-2 '])[1]")
    accept_btn.click()

    time.sleep(5)










    print("Login successful!")



















