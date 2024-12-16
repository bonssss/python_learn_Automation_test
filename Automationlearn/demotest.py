import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\Automation learn\CHROMEDRIVER.EXE")
driver = webdriver.Chrome(service=Service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
# driver.find_element(By.ID, "checkBoxOption2").click()
options= driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for option in options:
    if option.get_attribute("value")== "option2":
        option.click()
        assert  option.is_selected()
        break

time.sleep(3)
