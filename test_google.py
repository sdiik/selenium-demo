from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # tidak membuka jendela browser
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
print("Title:", driver.title)
driver.quit()