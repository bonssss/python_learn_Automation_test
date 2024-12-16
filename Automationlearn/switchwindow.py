import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\Automation learn\CHROMEDRIVER.EXE")
driver = webdriver.Chrome(service=Service_obj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
print(driver.title)

driver.find_element(By.LINK_TEXT,"Cli ck Here").click()
print(driver.find_element(By.TAG_NAME,"h3").text)
widowopened=driver.window_handles
driver.switch_to.window(widowopened[1])

print(driver.find_element(By.TAG_NAME,"h3").text)

