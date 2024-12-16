import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Set up the WebDriver
Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\Automation learn\CHROMEDRIVER.EXE")
driver = webdriver.Chrome(service=Service_obj)
driver.maximize_window()
driver.implicitly_wait(5)

# Open the website
driver.get("https://nextdev.netryde.com/")
print(driver.title)

# Perform login actions
driver.find_element(By.XPATH, "(//div[contains(@class,'burger-icon-white')])[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "(//button[@class='btn btn-black'][normalize-space()='Sign In'])[1]").click()
driver.find_element(By.XPATH, "(//input[contains(@class,'form-control username')])[1]").send_keys("11@test.zprodev.com")
password_field = driver.find_element(By.XPATH, "(//input[@placeholder='Password'])[1]")
password_field.send_keys("Test@123")
show_password = driver.find_element(By.XPATH, "(//input[contains(@type,'checkbox')])[1]")
show_password.click()

# Pause for CAPTCHA completion
print("Please complete the CAPTCHA manually and press Enter to continue...")
input("Press Enter after completing CAPTCHA...")

# Submit login
submit_login = driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]")
submit_login.click()

# Wait for the dashboard to load
WebDriverWait(driver, 10).until(
    EC.url_to_be("https://nextdev.netryde.com/customer/book")
)

# Navigate to Trips page
humburger_icon = driver.find_element(By.XPATH, "(//span[@class='burger-icon-bottom'])[1]")
humburger_icon.click()
Trips = driver.find_element(By.XPATH, "(//a[normalize-space()='Trips'])[1]")
Trips.click()

# Wait for the Trips page to load
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "(//h6[contains(text(),'Trips')])[2]"))
)

# Locate and interact with the "Pending Trips" checkbox
try:
    # Wait for the checkbox to appear
    pending_trips = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[label/span[contains(text(),'Pending')]]//input[@type='checkbox']"))
    )

    # Scroll to the checkbox
    driver.execute_script("arguments[0].scrollIntoView(true);", pending_trips)

    # Ensure the checkbox is interactable
    is_interactable = driver.execute_script(
        "return arguments[0].offsetParent !== null && !arguments[0].disabled;", pending_trips
    )
    print(f"Is Pending Trips interactable? {is_interactable}")

    # Click the checkbox using JavaScript or ActionChains
    if is_interactable:
        driver.execute_script("arguments[0].click();", pending_trips)
        print("Successfully clicked Pending Trips using JavaScript.")
    else:
        ActionChains(driver).move_to_element(pending_trips).click().perform()
        print("Successfully clicked Pending Trips using ActionChains.")
except Exception as e:
    print(f"Failed to interact with Pending Trips: {e}")
    driver.save_screenshot("pending_trips_debug.png")
    print("Screenshot saved as 'pending_trips_debug.png'.")

# Wait for user verification (optional for debugging)
# time.sleep(5)
# print("Successfully displayed trip list.")
# pending_trips_details= driver.find_element(By.XPATH,"a:nth-child(1) .d-flex > .p-2")
# # WebDriverWait(driver, 10).until(
# #     EC.visibility_of_element_located((By.XPATH, "(//div)[66]"))
# # )
# pending_trips_details.click()
time.sleep(15)


# Close the browser
driver.quit()
