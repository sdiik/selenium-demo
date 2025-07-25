import pytest
from pages.soucedemo_login_page import SoucedemoLoginPage

def test_soucedemo_login_page(setup_driver, base_url):
    print("Base URL:", base_url)
    login_page = SoucedemoLoginPage(setup_driver, base_url)
    login_page.go_to()

    login_page.login(username="standard_user", password="secret_sauce")

    if login_page.is_login_successful():
        print("Login successful")
        login_page.click_menu_button()

        status = login_page.get_menu_aria_hidden_status()

        if status:
            print("menu is hidden", status)
            login_page.logout_clicked()
            if login_page.is_logout_successful():
                print("success logout")
        else:
            print("menu is hidden")
    else:
        print("Login failed")

    

