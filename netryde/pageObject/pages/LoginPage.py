from selenium.webdriver.common.by import By

from netryde.Customer_trip_list import driver


class LoginPage:

    def __init__(self,driver):
        self.driver= driver

    email = (By.XPATH,"(//input[contains(@class,'form-control username')])[1]")
    password =(By.XPATH,"(//input[@placeholder='Password'])[1]")
    login_button= (By.XPATH,"(//button[normalize-space()='Login'])[1]")


    def email_value(self):
        return self.driver.find_element(*LoginPage.email)

    def password_value(self):
        return  self.driver.find_element(*LoginPage.password)
    def login(self):
        return self.driver.find_element(*LoginPage.login_button)
