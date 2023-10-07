import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from POM.pages.additemtocart_page import AddItem
import login_test
from POM.pages.login_page import Login


@pytest.fixture()
def driver():
    driver1 = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver1.implicitly_wait(5)
    yield driver1
    driver1.close()
    driver1.quit()


def add_item_to_cart():
    login_page = Login(driver)
    login_page.open_url("https://www.demoblaze.com/")
    time.sleep(5)
    login_page.click_log_in()
    login_page.login("testuser01!@#", "testpassword")
    login_page.click_login_button()

    add_item = AddItem(driver)
    add_item.select_category("Laptops")
    add_item.select_item("MacBook air")
    add_item.add_to_cart_button()
    time.sleep(3)
    add_item.assert_product_in_cart()
