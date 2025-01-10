import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    Service_obj = Service(r"C:\Users\bons\Documents\Website_projects\python learn\netryde\CHROMEDRIVER.EXE")
    driver = webdriver.Chrome(service=Service_obj)
    driver.maximize_window()
    yield driver
    driver.quit()



def test_register_driver(driver):
    driver.get("https://nextdev.netryde.com/")
    print(driver.title)

    try:
        # Locate the element
        signup_driver = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Signup as a Driver')]"))
        )

        # Scroll to the element
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", signup_driver)
        print("Scrolled to 'Signup as a Driver' button.")

        # Highlight the element for debugging
        driver.execute_script("arguments[0].style.border='3px solid red'", signup_driver)

        # Wait for the element to become clickable
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Signup as a Driver')]")))

        # Click the element
        signup_driver.click()
        print("Clicked 'Signup as a Driver' successfully!")
    except Exception as e:
        print(f"Error interacting with 'Signup as a Driver': {e}")

    # Add delay for visual confirmation (not recommended for production)
    time.sleep(4)

    driver_email = driver.find_element(By.XPATH, "(//input[@class='form-control email'])[1]")
    driver_email.send_keys("10@test.zprodev.com")

    driver_password = driver.find_element(By.XPATH, "(//input[@placeholder='***********'])[1]")
    driver_password.send_keys("Test@123")

    confirm_password_driver = driver.find_element(By.XPATH, "(//input[@placeholder='***********'])[2]")
    confirm_password_driver.send_keys("Test@123")

    checkbox = driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")
    checkbox.click()
    # Wait for manual CAPTCHA completion
    print("Please complete the CAPTCHA manually and press Enter to continue...")
    input("Press Enter after completing CAPTCHA...")

    Register_driver_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Create Driver Account'])[1]")
    Register_driver_button.click()

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

    time.sleep(15)
    # Quit the browser
    driver.quit()

