import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    # Set up Chrome WebDriver
    Service_obj = Service(r"C:\Users\bons\Documents\Website projects\python learn\netryde\CHROMEDRIVER.EXE")
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
        "11@test.zprodev.com")
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

    # Wait for page to load
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://nextdev.netryde.com/customer/book")
    )
    print("Login successful!")

    time.sleep(5)

    starting_address = driver.find_element(By.XPATH,
                                           "(//input[@class='address--input-box point-a pac-target-input'])[1]")
    starting_address.send_keys("Hwy 99 Seattle, WA, USA")
    time.sleep(1)
    starting_address.send_keys(Keys.ESCAPE)  # Close Google suggestions
    time.sleep(1)

    # Enter destination address
    destination_address = driver.find_element(By.XPATH,
                                              "(//input[@class='address--input-box point-b pac-target-input'])[1]")
    destination_address.send_keys("seattle,WA,USA")
    time.sleep(1)
    destination_address.send_keys(Keys.ESCAPE)  # Close Google suggestions
    time.sleep(1)

    # Wait for the "Book for" button to be visible
    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[contains(@class, 'btn-black-lg') and contains(text(), 'Book for')]"))
    )


    # Click the button
    book_for_button = driver.find_element(By.XPATH,
                                      "//button[contains(@class, 'btn-black-lg') and contains(text(), 'Book for')]")
    # time.sleep(10)
    book_for_button.click()

    # Wait for the "Book Now" button to become visible and clickable
    book_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'btn btn-gray') and text()='Book Now']"))
    )
    print("address selected")

    # Scroll to the "Book Now" button (if necessary)
    driver.execute_script("arguments[0].scrollIntoView(true);", book_now_button)
    time.sleep(1)  # Ensure the scrolling animation completes



    book_now = driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='Book Now'])[2]")
    book_now.click()

    print("book now button clicked")

    num_passenger= driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='+'])[1]")
    num_passenger.click()
    print("numberof passebger selected")
    date_time_picker = driver.find_element(By.XPATH,"//button[@aria-label='Choose date']//*[name()='svg']")
    date_time_picker.click()

    time.sleep(2)

    date= driver.find_element(By.XPATH,"(//button[normalize-space()='24'])[1]")
    date.click()

    hour =driver.find_element(By.XPATH,"(//li[@aria-label='2 hours'])[1]")
    hour.click()
    minute= driver.find_element(By.XPATH,"(//li[@aria-label='10 minutes'])[1]")
    minute.click()

    merian = driver.find_element(By.XPATH,"(//li[@aria-label='PM'])[1]")
    merian.click()
    time.sleep(5)

    ok_button= driver.find_element(By.XPATH,"//button[contains(@class, 'MuiButton-root') and contains(text(), 'OK')]")
    ok_button.click()


    time.sleep(5)  # Wait for the page to load and show the result

    print("date and time selected")

    Tips = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//label[normalize-space()='25%'])[1]"))
    )
    print("Address selected")

    Tips = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//label[normalize-space()='25%'])[1]"))
    )

    # Scroll to the "tips" button (if necessary)
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Tips)
    time.sleep(1)  # Optionally, wait for the scroll animation to complete

    Tip = driver.find_element(By.XPATH,"(//label[normalize-space()='25%'])[1]")

    Tip.click()

    continue_to_checkout= driver.find_element(By.XPATH,"(//button[normalize-space()='Continue to checkout'])[1]")
    continue_to_checkout.click()

    time.sleep(3)

    moveto_paynow = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Pay now'])[1]"))
    )

    # Scroll to the "tips" button (if necessary)
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", moveto_paynow)
    time.sleep(1)

    Pay_now_button = driver.find_element(By.XPATH,"(//button[normalize-space()='Pay now'])[1]")
    Pay_now_button.click()


    time.sleep(20)

    card_num = driver.find_element(By.XPATH,"(//input[@id='cardNumber'])[1]")
    card_num.send_keys("4111111111111111")

    expiration_date = driver.find_element(By.XPATH,"(//input[@id='cardExpiry'])[1]")
    expiration_date.send_keys("1225")

    cvc_num= driver.find_element(By.XPATH,"(//input[@id='cardCvc'])[1]")
    cvc_num.send_keys("123")

    holder_name= driver.find_element(By.XPATH,"(//input[@id='billingName'])[1]")
    holder_name.send_keys("John")

    complete_payment = driver.find_element(By.XPATH,"(//div[@class='SubmitButton-IconContainer'])[1]")
    complete_payment.click()

    time.sleep(20)
    # Wait for the "Booking Confirmation" h6 element to be present
    booking_confirmation_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h6[normalize-space(text())='Booking Confirmation']"))
    )

    # Assert that the text in the <h6> tag is "Booking Confirmation"
    assert booking_confirmation_element.text == "Booking Confirmation", "Booking Confirmation not found!"
    print("Booking Confirmation page is displayed.")

    print("Booking completed")
    #
    #
    #
    #
    #
    #
    #




