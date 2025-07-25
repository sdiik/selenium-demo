import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password", [
    ("tohamindes@gmail.com", "Sukses111!!!"),
    ("invalid_user", "wrong_password"),
    ("invalid_user1", "wrong_password"), 
    ("invalid_user2", "wrong_password"),  
    ("invalid_user3", "wrong_password"),  
    ("invalid_user4", "wrong_password"),   
    ("invalid_user5", "wrong_password")   
])

def test_multiple_login_page_success(setup_driver, username, password):
    login_page = LoginPage(setup_driver)
    login_page.go_to()

    login_page.login(username=username, password=password)

    assert "Facebook" in setup_driver.title
