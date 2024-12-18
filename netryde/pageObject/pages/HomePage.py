from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver


    humburgers_icon = (By.XPATH,"(//div[contains(@class,'burger-icon-white')])[1]")
    signin_button =(By.XPATH,"(//button[@class='btn btn-black'][normalize-space()='Sign In'])[1]")

    def loginpage(self):
        return self.driver.find_element(*HomePage.humburgers_icon)
    def signin(self):
        return  self.driver.find_element(*HomePage.signin_button)