from selenium.webdriver.common.by import By
from pages.page_base import BasePage
from utils.element import get_button

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to(self):
        self.driver.get("https://www.facebook.com/login")

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "pass")
        login_button = get_button(self.driver, "loginbutton")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()