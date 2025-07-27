import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [
    ("tohamindes@gmail.com", "Sukses111!!!"),
   
])

def test_multiple_login_page_success(setup_driver, username, password):
    login_page = LoginPage(setup_driver)
    login_page.go_to()

    login_page.login(username=username, password=password)

    assert "Facebook" in setup_driver.title
