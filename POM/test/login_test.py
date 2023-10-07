import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from POM.pages.login_page import Login


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.close()
    driver.quit()


# Test Case - 1 : Login
def test_login(driver):
    login_test = Login(driver)
    login_test.open_url("https://www.demoblaze.com/")
    time.sleep(5)
    login_test.click_log_in()
    login_test.login("testuser01!@#", "testpassword")
    login_test.click_login_button()
    time.sleep(5)

    # Assert if Log out button is displayed after login
    assert "Log out" in driver.page_source
