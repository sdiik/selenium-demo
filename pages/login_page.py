from selenium.webdriver.common.by import By
from pages.page_base import BasePage

class LoginPage(BasePage):
    def go_to(self):
        self.driver.get("https://www.facebook.com/login")

    def login(self, username, password):
        username_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "pass")
        login_button = self.driver.find_element(By.ID, "loginbutton")

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()