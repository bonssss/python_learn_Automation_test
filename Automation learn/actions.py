import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\Automation learn\CHROMEDRIVER.EXE")
driver = webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
action= ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
time.sleep(4)
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

time.sleep(5)
