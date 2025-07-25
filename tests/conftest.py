import pytest
import os
from dotenv import load_dotenv
from utils.driver_factory import create_driver
from pages.login_page import LoginPage

load_dotenv()

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture
def setup_driver():
    driver = create_driver()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(setup_driver):
    driver = setup_driver
    login_page = LoginPage(driver)
    login_page.go_to()
    login_page.login("tohamindes@gmail.com", "Sukses111!!!")
    yield driver