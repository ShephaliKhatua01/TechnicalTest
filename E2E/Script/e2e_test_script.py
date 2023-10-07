import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Test Case - 1 : Login
def login(username, password):
    try:
        # Open URL
        driver.get("https://www.demoblaze.com/")

        # Click on "Log in" button
        driver.find_element(By.ID, "login2").click()
        time.sleep(3)

        # Enter Username and Password
        username_input = driver.find_element(By.ID, "loginusername")
        username_input.send_keys(username)
        password_input = driver.find_element(By.ID, "loginpassword")
        password_input.send_keys(password)
        time.sleep(3)

        # Click the login button to submit
        driver.find_element(By.XPATH, '//button[contains(text(), "Log in")]').click()
        time.sleep(5)

        # Assert if Log out button is displayed after login
        logout_button = driver.find_element(By.ID, "logout2")
        logout_button.is_displayed()

        # 2nd way of assertion:
        # assert "Log out" in driver.page_source

        print("Test Case 1 (Login) - Passed")
    except:
        print("Test Case 1 (Login) - Failed")


# Test Case - 2: Add an Item to the Cart

def add_item_to_cart(product_category, product_name):
    try:

        # Finding Laptop option from Category list and clicking on it
        categories = driver.find_element(By.XPATH, "//div[@class='list-group']")
        subcategories = categories.find_elements(By.TAG_NAME, "a")
        for item in subcategories:
            print(item.text)
            if item.text == product_category:
                item.click()
                time.sleep(5)
                assert "Sony vaio i7" in driver.page_source
                print("Product category name is" + " " + product_category)
                break
            else:
                print("Product category name is" + " " + item.text)

        # Selecting Macbook air from the list
        list_of_items = driver.find_element(By.XPATH, "//div[@id='tbodyid']")
        items = list_of_items.find_elements(By.TAG_NAME, "a")
        for item in items:
            if item.text == product_name:
                item.click()
                time.sleep(5)
                assert "Add to cart" in driver.page_source
                print(product_name + "page is displayed")
                break
            else:
                print(item.text + " " + "is not equal to" + " " + product_name)

        # Clicking on Add to cart option
        add_to_cart = (driver.find_element(By.LINK_TEXT, "Add to cart"))
        add_to_cart.click()
        time.sleep(5)

        # Accept the alert
        alert = driver.switch_to.alert
        alert.accept()

        # Assert one entry has been added to the products list in checkout page
        driver.find_element(By.XPATH, "//a[@id='cartur']").click()
        table = driver.find_element(By.TAG_NAME, "table")
        rows = driver.find_elements(By.TAG_NAME, "tr")
        assert len(rows) >= 1
        print("Test Case 2 (Add to Cart) - Passed")

    except:
        print("Test Case 2 (Add to Cart) - Failed")


# Test Case - 3 - Place an order from the cart page and complete a purchase
def place_order(name_input, country_input, city_input, card_input, month_input, year_input):
    try:

        # Click on Place Order button
        place_order_button = driver.find_element(By.XPATH, '//button[contains(text(),"Place Order")]')
        place_order_button.click()
        time.sleep(4)

        # Fill the details in the form
        name = driver.find_element(By.ID, "name")
        name.send_keys(name_input)
        country = driver.find_element(By.ID, "country")
        country.send_keys(country_input)
        city = driver.find_element(By.ID, "city")
        city.send_keys(city_input)
        card = driver.find_element(By.ID, "card")
        card.send_keys(card_input)
        month = driver.find_element(By.ID, "month")
        month.send_keys(month_input)
        year = driver.find_element(By.ID, "year")
        year.send_keys(year_input)
        time.sleep(5)

        # Click on Purchase
        purchase_button = driver.find_element(By.XPATH, '//button[contains(text(),"Purchase")]')
        purchase_button.click()
        time.sleep(5)

        # Asset Success Message and Click OK
        success_message = driver.find_element(By.XPATH, '//h2[normalize-space()="Thank you for your purchase!"]')
        print(success_message.text)
        driver.find_element(By.XPATH, "//button[contains(text(), OK)]")
        print("Test Case 3 (Place Order) - Passed")
    except:
        print("Test Case 3 (Place Order) - Failed")
