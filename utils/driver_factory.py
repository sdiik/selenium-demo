from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import shutil

def create_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Temukan lokasi chromedriver
    chrome_driver_path = shutil.which("chromedriver") or "/usr/lib/chromium/chromedriver"
    service = Service(executable_path=chrome_driver_path)

    driver = webdriver.Chrome(service=service, options=options)
    
    print("✅ Chrome version:", driver.capabilities.get('browserVersion'))
    print("✅ Chromedriver version:", driver.capabilities.get('chrome', {}).get('chromedriverVersion'))
    
    return driver