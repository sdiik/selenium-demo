from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def create_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--headless")  # gunakan default
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    return driver