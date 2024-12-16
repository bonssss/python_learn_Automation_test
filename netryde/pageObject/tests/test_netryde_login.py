import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass



class TestNetryde(BaseClass):

    def test_login(self):
        driver = self.driver

        # Open the menu
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//div[contains(@class,'burger-icon-white')])[1]"))
        ).click()

        # Click the Sign In button
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-black'][normalize-space()='Sign In'])[1]"))
        ).click()

        # Enter username
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//input[contains(@class,'form-control username')])[1]"))
        ).send_keys("11@test.zprodev.com")

        # Enter password
        password_field = driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[1]")
        password_field.send_keys("Test@123")

        # Show password
        show_password = driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[1]")
        show_password.click()

        # Wait for manual CAPTCHA completion
        print("Please complete the CAPTCHA manually and press Enter to continue...")
        input("Press Enter after completing CAPTCHA...")

        # Submit login
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Login'])[1]"))
        ).click()

        # Verify the target page URL
        WebDriverWait(driver, 20).until(
            EC.url_to_be("https://nextdev.netryde.com/customer/book")
        )

        assert "customer/book" in driver.current_url, "Login failed or incorrect page loaded."
        print("Login successful!")
