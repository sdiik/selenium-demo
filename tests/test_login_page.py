import pytest
from pages.login_page import LoginPage


def test_login_page_success(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.go_to()

    login_page.login("tohamindes@gmail.com", "Sukses111!!!")


    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    WebDriverWait(setup_driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body")))
    
    home_headers = setup_driver.find_elements(By.XPATH, "//div[@aria-label='']")

    print("Jumlah header 'Home':", len(home_headers))
    for header in home_headers:
        print("Header ditemukan:", header.text)
    