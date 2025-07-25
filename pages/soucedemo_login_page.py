from selenium.webdriver.common.by import By
from pages.page_base import BasePage
from utils.element import get_button
from utils.element import get_input_field
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SoucedemoLoginPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def go_to(self):
        self.driver.get(self.base_url)

    def login(self, username, password):
        username_field = get_input_field(self.driver, "user-name")
        password_field = get_input_field(self.driver, "password")

        login_button = get_button(self.driver, "login-button")

        if username_field and password_field and login_button:
            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button.click()
        else:
            print("One or more fields could not be found.")

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, "react-burger-menu-btn"))
            )
            return True
        except Exception as e:
            print("Login failed:", e)
            return False
    
    def click_menu_button(self):
        try:
            menu_btn = self.driver.find_element(By.ID, "react-burger-menu-btn")
            if menu_btn.is_displayed():
                print("Menu button is displayed.")
                menu_btn.click()
                print("Button 'react-burger-menu-btn' clicked.")
            else:
                print("Menu button is not displayed.")
        except Exception as e:
            print("Error finding or clicking the menu button:", e)

    def get_menu_aria_hidden_status(self):
        try:
            menu_wrap = self.driver.find_element(By.CLASS_NAME, "bm-menu-wrap")
            if menu_wrap.is_displayed():
                aria_hidden = menu_wrap.get_attribute("aria-hidden")
                print("Status aria-hidden pada menu:", aria_hidden)
                return aria_hidden
        except Exception as e:
            print("Gagal menemukan elemen menu atau atribut aria-hidden:", e)
            return None

    def logout_clicked(self):
        try:
            # Tunggu tombol logout benar-benar terlihat
            logout_btn = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, "logout_sidebar_link"))
            )
            logout_btn.click()
            print("button logout_sidebar_link logout")
        except Exception as e:
            print("Error finding or clicking the logout button:", e)
            
    def is_logout_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "login_container"))
            )
            return True
        except Exception as e:
            return False