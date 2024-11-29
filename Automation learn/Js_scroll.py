import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
webdriver_options= webdriver.ChromeOptions()
webdriver_options.add_argument("headless")
webdriver_options.add_argument("--ignore-certificate-errors")


Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\Automation learn\CHROMEDRIVER.EXE")
driver = webdriver.Chrome(service=Service_obj, options= webdriver_options)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.execute_script("window.scrollBy(0,700)")

driver.get_screenshot_as_file("screen.png")

time.sleep(5)