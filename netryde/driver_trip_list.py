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

    pending = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='box-collapse scrollFilter d-none d-lg-block']//span[@class='text-sm-medium'][normalize-space()='Pending']"))
    )
    pending.click()

    time.sleep(5)

    requested = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html[1]/body[1]/main[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/label[1]/span[2]"))
    )
    requested.click()



    time.sleep(5)
    booked = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='box-collapse scrollFilter d-none d-lg-block']//span[@class='text-sm-medium'][normalize-space()='Booked']"))
    )
    booked.click()

    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 100);")
    started = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='box-collapse scrollFilter d-none d-lg-block']//span[@class='text-sm-medium'][normalize-space()='Started']"))
    )
    started.click()

    time.sleep(5)
    cancelled = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='box-collapse scrollFilter d-none d-lg-block']//span[@class='text-sm-medium'][normalize-space()='Cancelled']"))
    )
    cancelled.click()

    time.sleep(5)

    completed = WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH,"//div[@class='box-collapse scrollFilter d-none d-lg-block']//span[@class='text-sm-medium'][normalize-space()='Completed']"))
    )

    completed.click()

    time.sleep(5)








    print("Login successful!")



















