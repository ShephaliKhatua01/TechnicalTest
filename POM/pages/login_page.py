from selenium.webdriver.common.by import By


class Login:

    def __init__(self, driver):
        self.driver = driver
        self.log_in_button = (By.ID, "login2")
        self.username_textbox = (By.ID, "loginusername")
        self.password_textbox = (By.ID, "loginpassword")
        self.login_button = (By.XPATH, '//button[contains(text(), "Log in")]')

    def open_url(self, url):
        self.driver.get(url)

    def click_log_in(self):
        self.driver.find_element(*self.log_in_button).click()

    def login(self, username, password):
        self.driver.find_element(*self.username_textbox).send_keys(username)
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
