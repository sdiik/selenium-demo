from pages.login_page import LoginPage

def test_login_page_success(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.go_to()

    login_page.login("tohamindes@gmail.com", "Sukses111!!!")

    assert "Facebook" in setup_driver.title