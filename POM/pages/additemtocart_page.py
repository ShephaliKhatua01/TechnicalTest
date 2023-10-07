import time

from selenium.webdriver.common.by import By


class AddItem:
    def __init__(self, driver):
        self.driver = driver
        self.categories_list = (By.XPATH, "//div[@class='list-group']")
        self.subcategories_link = (By.TAG_NAME, "a")
        self.available_items_list = (By.XPATH, "//div[@id='tbodyid']")
        self.item_link = (By.TAG_NAME, "a")
        self.add_to_cart_button = (By.LINK_TEXT, "Add to cart")
        self.cart_link = (By.XPATH, "//a[@id='cartur']")
        self.product_table = (By.TAG_NAME, "table")
        self.rows_in_table = (By.TAG_NAME, "tr")

    def select_category(self, product_category):
        product_type_list = self.driver.find_element(*self.categories_list).find_elements(*self.subcategories_link)
        for item in product_type_list:
            print(item.text)
            if item.text == product_category:
                item.click()
                time.sleep(5)
                print("Product category name is" + " " + product_category)
                break
            else:
                print("Product category name is" + " " + item.text)

    def select_item(self, product_name):
        product_name_list = self.driver.find_element(*self.available_items_list).find_elements(*self.item_link)
        for item in product_name_list:
            if item.text == product_name:
                item.click()
                time.sleep(5)
                print(product_name + "page is displayed")
                break
            else:
                print(item.text + " " + "is not equal to" + " " + product_name)

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

#  #Assertions Method
    def assert_product_in_cart(self):
        self.driver.find_element(*self.cart_link).click()
        rows = self.driver.find_element(*self.product_table).find_elements(*self.rows_in_table)
        assert len(rows) >= 1

