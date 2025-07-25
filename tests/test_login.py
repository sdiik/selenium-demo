import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium WebDriver")
    search_box.submit()

    assert "Selenium WebDriver" in driver.page_source
    assert "Google" in driver.title