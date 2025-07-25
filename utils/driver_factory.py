from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_driver():
    options = Options()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    options.add_argument("--incognito")
  #  options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver